# Lidlar jadvali — ravshancha.uz

CV saytdagi "Loyihaga buyurtma berish" formasi endi mijozning Telegram’ini ochmaydi. Ariza serverga ketadi va
Google Sheets jadvaliga status bilan yoziladi, sizga esa email keladi:

```
forma (site/index.html)
   → site/api/lead.php          tekshiruv, honeypot, bitta manzildan 10 daqiqada 5 ta ariza
        → Apps Script web-ilova (Code.gs)
        │     → "Lidlar" varag‘i: yangi qator, status = "Yangi"
        │     → email: ariza matni + jadvaldagi qatorga havola (Google yuboradi)
        └→ noreply@ravshancha.uz orqali xat: ro‘yxatdagi pochtalarga + nusxasi o‘sha qutining Sent papkasiga
```

Ikkala yo‘l har bir ariza uchun birga ishlaydi, shuning uchun ariza bir vaqtning o‘zida jadvalda, Gmail’da va
domendagi pochtada qoladi. Ikkalasi ham ishlamasa mijozga tayyor matnli "Telegram’da yuborish" tugmasi chiqadi
— ya’ni ariza baribir yo‘qolmaydi.

## Fayllar

```
tools/leads/Code.gs            jadvalga qo‘yiladigan Apps Script (web-ilova)
tools/leads/test-code.js       Code.gs ni Google’siz tekshirish: node tools/leads/test-code.js
tools/leads/mock-sheets.js     lead.php ni lokal sinash uchun soxta web-ilova
site/api/lead.php              forma endpoint’i (serverda ishlaydi)
site/api/lead-config.sample.php  sozlama namunasi; haqiqiysini deploy GitHub’dagi qiymatlardan yozadi
```

## O‘rnatish (bir marta, ~10 daqiqa)

1. Google Sheets’da yangi jadval oching (masalan, "ravshancha.uz lidlar").
2. **Extensions → Apps Script**. Ochilgan `Code.gs` ichini `tools/leads/Code.gs` matni bilan to‘liq almashtiring.
3. `SECRET` qatoridagi `CHANGE_ME` o‘rniga tasodifiy satr yozing (`openssl rand -hex 24`). Standart qiymat bilan
   skript hech narsa qabul qilmaydi.
4. Yuqoridagi ro‘yxatdan `setup` funksiyasini tanlab **Run** bosing. Google ruxsat so‘raydi (jadvalni tahrirlash
   va sizning nomingizdan xat yuborish) — ruxsat bering. "Lidlar" va "Voronka" varaqlari paydo bo‘ladi.
5. **Deploy → New deployment → Web app**: *Execute as* — **Me**, *Who has access* — **Anyone**. Chiqqan
   manzilni (`https://script.google.com/macros/s/…/exec`) nusxalang. Uni brauzerda ochsangiz
   `{"ok":true,"service":"ravshancha.uz leads"}` chiqishi kerak.
6. GitHub → **Settings → Secrets and variables → Actions → Secrets**: `LEAD_SHEETS_URL` (5-qadamdagi manzil) va
   `LEAD_SHEETS_SECRET` (3-qadamdagi satr). Xat boradigan manzilni almashtirmoqchi bo‘lsangiz, **Variables** da
   `LEAD_NOTIFY_EMAIL` ni qo‘shing. Serverdagi `api/lead-config.php` ni deploy har safar o‘zi yozadi — qo‘lda fayl
   yaratish shart emas, qo‘lda yozilgani esa keyingi deploy’da almashtiriladi. Qiymatlar repozitoriyga tushmaydi.
7. Saytdan bitta test ariza yuboring: jadvalda qator, pochtada xat paydo bo‘lishi kerak.

`Code.gs` ni keyin o‘zgartirsangiz: **Deploy → Manage deployments → ✎ → Version: New version → Deploy**.
Manzil o‘zgarmaydi, lekin yangi versiya chiqarilmaguncha eski kod ishlayveradi.

## Xatni kim yuboradi

Hosting `mail()` funksiyasini o‘chirib qo‘ygan (2026-09-20 da aniqlandi: ariza oxirigacha yetib borar, lekin xat
yuborish bosqichida skript uzilib, brauzerga bo‘sh `200` qaytardi). Shuning uchun `lead.php` xatni domenning
o‘z pochtasi orqali SMTP bilan yuboradi:

1. cPanel → Email Accounts: `noreply@ravshancha.uz` (yaratilgan).
2. GitHub → Settings → Secrets and variables → Actions → **Secrets** → `LEAD_SMTP_PASSWORD` — o‘sha pochtaning
   paroli. Faqat shu qo‘yilganda SMTP yoqiladi; parolsiz holatda eski `mail()` yo‘li qoladi.
3. Kerak bo‘lsa **Variables**: `LEAD_SMTP_HOST` (standart `mail.ravshancha.uz`), `LEAD_SMTP_PORT` (`465`),
   `LEAD_SMTP_USER` (`noreply@ravshancha.uz`), `LEAD_SMTP_VERIFY` (`0` — sertifikat nomi mos kelmasa).

Har bir yuborilgan xatning nusxasi `noreply@ravshancha.uz` qutisining **Отправленные** papkasiga ham
yoziladi (IMAP orqali, `mail.ravshancha.uz:993`). SMTP o'zi nusxa saqlamaydi — "Sent" papkasini odatda pochta
mijozi to'ldiradi, shuning uchun buni `lead.php` qo'lda bajaradi. Papka nomini server o'zi aytadi (cPanel'da
`INBOX.Sent`); kerak bo'lsa `LEAD_IMAP_FOLDER`, `LEAD_IMAP_HOST`, `LEAD_IMAP_PORT` o'zgaruvchilari bilan
boshqasini ko'rsatish mumkin. Nusxa saqlanmay qolsa ham ariza yo'qolmaydi — xat baribir yuborilgan bo'ladi.

Ariza bir nechta pochtaga yuborilishi mumkin: `LEAD_NOTIFY_EMAIL` vergul bilan ajratilgan ro‘yxatni qabul
qiladi (5 tagacha). Standart holatda ikkita manzil — Gmail va domendagi `ravshanc@ravshancha.uz`. Domendagi
nusxa bitta server ichida yetkaziladi, shuning uchun Gmail xatni spamga tashlasa ham ariza qo‘lda qoladi:
uni cPanel → Webmail orqali o‘qiysiz. Gmail’ga muntazam yetib borishi uchun cPanel’da **DKIM** yoqilgan va
**SPF** to‘g‘ri bo‘lishi shart (Email Deliverability bo‘limi).

465-port TLS bilan ulanadi, boshqa portlarda parol yuborilishidan oldin STARTTLS talab qilinadi. Nimadir
ishlamasa ariza yo‘qolmaydi: forma Telegram zaxirasini taklif qiladi va sababni kod bilan ko‘rsatadi:

| Kod | Ma’nosi |
| --- | --- |
| `502 smtp_connect` | pochta serveriga ulanib bo‘lmadi — manzil yoki port noto‘g‘ri, yoki chiquvchi port yopiq |
| `502 smtp_tls` | server STARTTLS taklif qilmadi; parol ochiq holda yuborilmaydi |
| `502 smtp_auth` | foydalanuvchi yoki parol qabul qilinmadi |
| `502 smtp_send` | server xatni oxirida rad etdi (masalan, jo‘natuvchi manzilga ruxsat yo‘q) |
| `502 delivery` | SMTP umuman sozlanmagan (parol secret’i yo‘q) va hosting `mail()` ni bermadi |
| `503 not_configured` | serverda `lead-config.php` yo‘q |
| `500 server` | skript kutilmaganda uzildi; hosting xato jurnaliga qarang |

## Jadval bilan ishlash

- `Status` ustuni ro‘yxatdan tanlanadi: Yangi → Bog‘landim → Suhbat o‘tdi → Taklif yuborildi → Shartnoma / Rad etildi.
  `Keyingi qadam`, `Summa`, `Izoh` — qo‘lda to‘ldiriladi.
- "Voronka" varag‘i har bosqichdagi lidlar soni va ulushini o‘zi sanaydi.
- Bosqichlarni o‘zgartirish: `Code.gs` dagi `STATUSES` → `setup` ni qayta ishga tushirish (mavjud qatorlarga tegmaydi,
  "Voronka" qayta chiziladi) → yangi versiyani deploy qilish.
- `Manba` ustuni hozir doim `cv`. Boshqa formalar (sotuv sahifasi, dental) ulanganida shu jadvalga o‘z manbasi bilan tushadi.

## Xavfsizlik

- Web-ilova manzili ochiq, shuning uchun har bir so‘rovda `SECRET` tekshiriladi; u faqat skriptda va serverdagi
  `lead-config.php` da turadi, brauzerga chiqmaydi.
- `=`, `+`, `-`, `@` bilan boshlanadigan matn jadvalga formula emas, oddiy matn bo‘lib yoziladi.
- Google serverlari chet elda joylashgan — shaxsga doir ma’lumotlarni saqlash talablari nuqtayi nazaridan buni o‘zingiz baholang.

## Lokal sinash

Bu Mac’da PHP yo‘q, lekin Docker bor:

```bash
node tools/leads/test-code.js          # Code.gs mantig‘i (soxta Google xizmatlari bilan)
node tools/leads/mock-sheets.js        # soxta web-ilova: http://localhost:8775/exec (… 8775 fail — rad etadi)
docker run --rm -p 127.0.0.1:8776:8080 -v "$PWD/site":/app php:8.3-cli php -S 0.0.0.0:8080 -t /app   # http://localhost:8776/
```

Lokal `site/api/lead-config.php` (git’ga tushmaydi):
`return ['sheets_url' => 'http://host.docker.internal:8775/exec', 'sheets_secret' => 'local-test-secret'];`
