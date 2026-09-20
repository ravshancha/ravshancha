/**
 * ravshancha.uz lidlar jadvali — jadvalga bog‘langan Google Apps Script.
 *
 * Sayt (site/api/lead.php) har bir arizani shu web-ilovaga POST qiladi: "Lidlar" varag‘iga yangi qator
 * qo‘shiladi (status — "Yangi") va egasiga email boradi. "Voronka" varag‘i har bosqichdagi lidlarni sanaydi.
 * O‘rnatish tartibi: tools/leads/README.md
 */

const SECRET = 'CHANGE_ME';   // serverdagi api/lead-config.php → sheets_secret bilan aynan bir xil satr
const NOTIFY_EMAIL = '';      // bo‘sh bo‘lsa, xat skript egasining manziliga boradi

const SHEET_NAME = 'Lidlar';
const FUNNEL_NAME = 'Voronka';
const STATUSES = ['Yangi', 'Bog‘landim', 'Suhbat o‘tdi', 'Taklif yuborildi', 'Shartnoma', 'Rad etildi'];
const HEADERS = ['Sana', 'Manba', 'Til', 'Ism', 'Telefon', 'Loyiha haqida', 'Sahifa', 'Status', 'Keyingi qadam', 'Summa', 'Izoh'];
const STATUS_COLUMN = HEADERS.indexOf('Status') + 1;

/** Bir marta qo‘lda ishga tushiriladi: varaqlar, sarlavhalar, status ro‘yxati va voronka formulalari. */
function setup() {
  const book = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = book.getSheetByName(SHEET_NAME) || book.insertSheet(SHEET_NAME, 0);
  const rows = sheet.getMaxRows() - 1;
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]).setFontWeight('bold');
  sheet.setFrozenRows(1);
  sheet.getRange(2, 1, rows, 1).setNumberFormat('yyyy-mm-dd hh:mm');
  sheet.getRange(2, HEADERS.indexOf('Telefon') + 1, rows, 1).setNumberFormat('@');
  sheet.getRange(2, HEADERS.indexOf('Keyingi qadam') + 1, rows, 1).setNumberFormat('yyyy-mm-dd');
  const statusRule = SpreadsheetApp.newDataValidation().requireValueInList(STATUSES, true).setAllowInvalid(false).build();
  sheet.getRange(2, STATUS_COLUMN, rows, 1).setDataValidation(statusRule);

  // Formulalarda argument ajratgichi yo‘q (SUMPRODUCT, bir argumentli IFERROR): "," va ";" ishlatadigan
  // har ikki til sozlamasida ham bir xil ishlaydi.
  const funnel = book.getSheetByName(FUNNEL_NAME) || book.insertSheet(FUNNEL_NAME, 1);
  const statusRange = "'" + SHEET_NAME + "'!$" + columnLetter(STATUS_COLUMN) + '$2:$' + columnLetter(STATUS_COLUMN);
  const totalRow = STATUSES.length + 2;
  funnel.clear();
  funnel.getRange(1, 1, 1, 3).setValues([['Bosqich', 'Lidlar', 'Ulush']]).setFontWeight('bold');
  STATUSES.forEach(function (status, index) {
    const row = index + 2;
    funnel.getRange(row, 1).setValue(status);
    funnel.getRange(row, 2).setFormula('=SUMPRODUCT((' + statusRange + '=A' + row + ')*1)');
    funnel.getRange(row, 3).setFormula('=IFERROR(B' + row + '/$B$' + totalRow + ')').setNumberFormat('0%');
  });
  funnel.getRange(totalRow, 1).setValue('Jami').setFontWeight('bold');
  funnel.getRange(totalRow, 2).setFormula('=SUM(B2:B' + (totalRow - 1) + ')').setFontWeight('bold');
  funnel.setFrozenRows(1);
}

/** Saytdan kelgan ariza. */
function doPost(e) {
  let data;
  try {
    data = JSON.parse(e.postData.contents);
  } catch (error) {
    return reply({ ok: false, error: 'json' });
  }
  if (SECRET === 'CHANGE_ME' || !data || data.secret !== SECRET) {
    return reply({ ok: false, error: 'secret' });
  }

  const lock = LockService.getScriptLock();
  let sheet;
  let row;
  try {
    lock.waitLock(15000);
    sheet = leadSheet();
    sheet.appendRow([new Date(), text(data.source), text(data.lang), text(data.name), text(data.phone), text(data.info), text(data.page), STATUSES[0]]);
    row = sheet.getLastRow();
  } catch (error) {
    return reply({ ok: false, error: 'sheet' });
  } finally {
    lock.releaseLock();
  }

  // Qator yozildi — xat ketmasa ham lid yo‘qolmaydi, shuning uchun javob baribir ok.
  let mailed = true;
  try {
    MailApp.sendEmail({
      to: NOTIFY_EMAIL || Session.getEffectiveUser().getEmail(),
      subject: 'Yangi ariza: ' + plain(data.name) + ' (' + plain(data.source) + ')',
      body: [
        'Ism: ' + plain(data.name),
        'Telefon: ' + plain(data.phone),
        'Loyiha haqida: ' + plain(data.info),
        'Manba: ' + plain(data.source) + ' · til: ' + plain(data.lang) + ' · sahifa: ' + plain(data.page),
        '',
        'Jadvaldagi qator: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl() + '#gid=' + sheet.getSheetId() + '&range=A' + row,
      ].join('\n'),
    });
  } catch (error) {
    mailed = false;
  }
  return reply({ ok: true, row: row, mailed: mailed });
}

/** Manzilni brauzerda ochib, web-ilova ishlayotganini tekshirish uchun. */
function doGet() {
  return reply({ ok: true, service: 'ravshancha.uz leads' });
}

function leadSheet() {
  const found = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  if (found && found.getLastRow() > 0) return found;
  setup();
  return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
}

function plain(value) {
  return String(value === undefined || value === null ? '' : value).slice(0, 2000);
}

/** Katakka yoziladigan matn: "=", "+", "-", "@" bilan boshlansa, formula bo‘lib ketmasligi uchun apostrof qo‘yiladi. */
function text(value) {
  const clean = plain(value);
  return /^[=+\-@\t\r]/.test(clean) ? "'" + clean : clean;
}

function columnLetter(column) {
  let letter = '';
  for (let n = column; n > 0; n = Math.floor((n - 1) / 26)) {
    letter = String.fromCharCode(65 + ((n - 1) % 26)) + letter;
  }
  return letter;
}

function reply(body) {
  return ContentService.createTextOutput(JSON.stringify(body)).setMimeType(ContentService.MimeType.JSON);
}
