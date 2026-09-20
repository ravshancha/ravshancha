// Runs Code.gs outside Google with stand-ins for SpreadsheetApp, LockService, MailApp and ContentService,
// so the script can be checked before it is pasted into the spreadsheet.
// Usage: node tools/leads/test-code.js
const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SOURCE = fs.readFileSync(path.join(__dirname, "Code.gs"), "utf8");
// Arrays built inside the vm context have another Array prototype; compare them as plain data.
const plain = (value) => JSON.parse(JSON.stringify(value));

function makeSheet(name, id) {
  const cells = {};
  const sheet = {
    name, id, rows: [], formats: {}, formulas: {}, validations: [], frozen: 0,
    getMaxRows: () => 1000,
    getLastRow: () => sheet.rows.length,
    getSheetId: () => id,
    setFrozenRows: (count) => { sheet.frozen = count; },
    clear: () => { sheet.rows = []; sheet.formulas = {}; },
    appendRow: (values) => { sheet.rows.push(values); },
    getRange: (row, column, height = 1, width = 1) => {
      const key = `${row}:${column}`;
      const range = {
        setValues: (values) => { values.forEach((line, offset) => { sheet.rows[row - 1 + offset] = line; }); return range; },
        setValue: (value) => { cells[key] = value; sheet.rows[row - 1] = sheet.rows[row - 1] || []; sheet.rows[row - 1][column - 1] = value; return range; },
        setFormula: (formula) => { sheet.formulas[key] = formula; return range; },
        setFontWeight: () => range,
        setNumberFormat: (format) => { sheet.formats[`${key}:${height}x${width}`] = format; return range; },
        setDataValidation: (rule) => { sheet.validations.push({ row, column, height, rule }); return range; },
      };
      return range;
    },
  };
  return sheet;
}

function load({ secret = "test-secret", mailFails = false, sheets = {} } = {}) {
  const state = { sheets, mails: [], locked: 0, released: 0 };
  const book = {
    getSheetByName: (name) => state.sheets[name] || null,
    insertSheet: (name) => { state.sheets[name] = makeSheet(name, Object.keys(state.sheets).length + 100); return state.sheets[name]; },
    getUrl: () => "https://docs.google.com/spreadsheets/d/TEST/edit",
  };
  const context = {
    SpreadsheetApp: {
      getActiveSpreadsheet: () => book,
      newDataValidation: () => {
        const rule = { list: null, allowInvalid: true };
        const builder = { requireValueInList: (list) => { rule.list = list; return builder; }, setAllowInvalid: (flag) => { rule.allowInvalid = flag; return builder; }, build: () => rule };
        return builder;
      },
    },
    LockService: { getScriptLock: () => ({ waitLock: () => { state.locked += 1; }, releaseLock: () => { state.released += 1; } }) },
    MailApp: { sendEmail: (mail) => { if (mailFails) throw new Error("quota"); state.mails.push(mail); } },
    Session: { getEffectiveUser: () => ({ getEmail: () => "owner@example.com" }) },
    ContentService: { MimeType: { JSON: "json" }, createTextOutput: (body) => ({ body, setMimeType() { return this; } }) },
  };
  vm.createContext(context);
  // The owner edits the SECRET line by hand; the test does the same edit in memory.
  vm.runInContext(SOURCE.replace("const SECRET = 'CHANGE_ME';", `const SECRET = ${JSON.stringify(secret)};`), context);
  const post = (payload) => JSON.parse(context.doPost({ postData: { contents: typeof payload === "string" ? payload : JSON.stringify(payload) } }).body);
  return { context, state, post };
}

const lead = { secret: "test-secret", source: "cv", lang: "uz", name: "Alisher Karimov", phone: "+998901234567", info: "Do‘konim uchun sayt kerak", page: "/" };

{ // a fresh spreadsheet: the first lead builds both sheets, lands in row 2 and is e-mailed
  const { state, post } = load();
  const answer = post(lead);
  assert.deepStrictEqual(answer, { ok: true, row: 2, mailed: true });
  const sheet = state.sheets["Lidlar"];
  assert.deepStrictEqual(plain(sheet.rows[0]), ["Sana", "Manba", "Til", "Ism", "Telefon", "Loyiha haqida", "Sahifa", "Status", "Keyingi qadam", "Summa", "Izoh"]);
  const row = sheet.rows[1];
  assert.strictEqual(Object.prototype.toString.call(row[0]), "[object Date]"); // a Date of the vm realm
  assert.deepStrictEqual(plain(row.slice(1)), ["cv", "uz", "Alisher Karimov", "'+998901234567", "Do‘konim uchun sayt kerak", "/", "Yangi"]);
  assert.strictEqual(sheet.frozen, 1);
  assert.deepStrictEqual(plain(sheet.validations.map((v) => [v.row, v.column, v.rule.list.length, v.rule.allowInvalid])), [[2, 8, 6, false]]);
  assert.strictEqual(state.mails.length, 1);
  assert.strictEqual(state.mails[0].to, "owner@example.com");
  assert.ok(state.mails[0].subject.includes("Alisher Karimov"));
  assert.ok(state.mails[0].body.includes("#gid=100&range=A2"));
  assert.strictEqual(state.locked, 1);
  assert.strictEqual(state.released, 1);
  const funnel = state.sheets["Voronka"];
  assert.strictEqual(funnel.formulas["2:2"], "=SUMPRODUCT(('Lidlar'!$H$2:$H=A2)*1)");
  assert.strictEqual(funnel.formulas["2:3"], "=IFERROR(B2/$B$8)");
  assert.strictEqual(funnel.formulas["8:2"], "=SUM(B2:B7)");
  assert.ok(!Object.values(funnel.formulas).some((formula) => /[,;]/.test(formula)), "formulas must not depend on the locale's argument separator");
  assert.strictEqual(post({ ...lead, name: "Ikkinchi" }).row, 3);
}

{ // wrong or missing secret, broken JSON, and a script left with the default secret
  const { state, post } = load();
  assert.deepStrictEqual(post({ ...lead, secret: "nope" }), { ok: false, error: "secret" });
  assert.deepStrictEqual(post({ name: "x" }), { ok: false, error: "secret" });
  assert.deepStrictEqual(post("not json"), { ok: false, error: "json" });
  assert.deepStrictEqual(Object.keys(state.sheets), []);
  assert.deepStrictEqual(load({ secret: "CHANGE_ME" }).post({ ...lead, secret: "CHANGE_ME" }), { ok: false, error: "secret" });
}

{ // text that a spreadsheet would run as a formula is stored as plain text
  const { state, post } = load();
  post({ ...lead, name: "=IMPORTXML(\"http://evil\",\"//a\")", info: "@SUM(1) va yana matn", page: "-1+1" });
  const row = state.sheets["Lidlar"].rows[1];
  assert.strictEqual(row[3], "'=IMPORTXML(\"http://evil\",\"//a\")");
  assert.strictEqual(row[5], "'@SUM(1) va yana matn");
  assert.strictEqual(row[6], "'-1+1");
}

{ // a failed e-mail does not lose the lead
  const { state, post } = load({ mailFails: true });
  assert.deepStrictEqual(post(lead), { ok: true, row: 2, mailed: false });
  assert.strictEqual(state.sheets["Lidlar"].rows.length, 2);
}

{ // an existing sheet with leads is appended to, not rebuilt
  const existing = makeSheet("Lidlar", 7);
  existing.rows = [["Sana"], ["old lead"]];
  const { state, post } = load({ sheets: { Lidlar: existing } });
  assert.strictEqual(post(lead).row, 3);
  assert.deepStrictEqual(state.sheets["Lidlar"].rows[1], ["old lead"]);
  assert.strictEqual(state.sheets["Voronka"], undefined);
}

{ // the address opened in a browser answers, and column letters go past Z
  const { context } = load();
  assert.deepStrictEqual(JSON.parse(context.doGet().body), { ok: true, service: "ravshancha.uz leads" });
  assert.deepStrictEqual([1, 8, 26, 27, 52, 703].map((n) => context.columnLetter(n)), ["A", "H", "Z", "AA", "AZ", "AAA"]);
}

console.log("Code.gs: all checks passed");
