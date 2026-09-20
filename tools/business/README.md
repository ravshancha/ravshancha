# Sotuvchi sayt — ravshancha.uz/business/

Biznes egalari uchun landing: jarayonlarni avtomatlashtirish, og‘riqlarni davolash, shaffoflik.
Dizayn va kod asosi CV saytdan (`site/index.html`) olingan. CV sayt ishonch uchun tayanch bo‘lib qoladi:
CV sayt footer’idagi "Biznes uchun xizmatlar" tugmasi shu yerga olib keladi; bu sahifaning o‘zida esa tashqariga (CV, telefon, messenjer) olib chiqadigan havola yo‘q — har bir blok diagnostika so‘rovnomasiga olib boradi.

## Tuzilma

```
tools/business/content.py      barcha matnlar (UZ + RU), kontaktlar, sozlamalar — FAQAT SHU YERDA tahrirlang
tools/business/template.html   sahifa shabloni (CSS + JS ichida, CV sayt uslubida)
tools/business/build_site.py   generator → site/business/index.html (uz), site/business/ru/index.html (ru), sitemap.xml
tools/business/build_og.py     ijtimoiy tarmoq rasmlari → site/business/assets/og-{uz,ru}.jpg (Pillow kerak)
tools/business/serve.js        lokal ko‘rish: butun site/ papkasi
tools/business/mock-telegram.js  lead.php ni lokal sinash uchun soxta Telegram API
site/business/api/lead.php     forma → Telegram bot (serverda ishlaydi)
site/business/api/lead-quiz.php  quiz javoblari kodi → yozuvi (generatsiya qilinadi, lead.php o‘qiydi)
site/business/.htaccess        lead-config va lead-quiz fayllarini yopadi
```

`site/business/index.html`, `site/business/ru/index.html` va `site/business/api/lead-quiz.php` generatsiya qilinadi — qo‘lda tahrirlanmaydi.
Logo, favicon, portret va OG-rasmlar shu saytning o‘zida: `site/business/assets/` — CV saytdagi o‘zgarishlar bu saytni buzmaydi.

## Ishlatish

```bash
python3 tools/business/build_site.py   # matn o‘zgargach qayta yig‘ish (faqat standart kutubxona)
python3 tools/business/build_og.py     # faqat og_lines / og_sub yoki portret o‘zgarsa
node tools/business/serve.js           # http://localhost:8772/ (CV) va http://localhost:8772/business/
```

Qayta yig‘ilgan sahifalarni `content.py` bilan birga commit qiling; `development` ga push — deploy.
Generator oxirida `TASDIQLANG` deb belgilangan, hali tasdiqlanmagan va’da/faktlar ro‘yxatini chiqaradi.

## Nega har til — alohida URL

CV saytda til JS bilan almashadi, shuning uchun Google faqat o‘zbekcha versiyani ko‘radi.
Bu yerda `/business/` (uz) va `/business/ru/` — alohida statik sahifalar, `hreflang` bilan: ruscha qidiruvda ham chiqadi.
Yangi til qo‘shish: `content.py` da `LANGS` va `L["en"]` ni to‘ldirish kifoya.

## Forma (lidlar)

Sahifada Telegram, WhatsApp va telefon **ataylab yo‘q** (header, hero, aloqa bo‘limi, footer, mobil pastki panel, JSON-LD):
har bir lid quiz orqali kelishi kerak — maqsadli auditoriyani saralash uchun. Barcha tugmalar (header’dagisi ham) quizni ochadi.
Telegram faqat bitta joyda qoladi — forma yuborilmay qolgandagi zaxira yo‘lda (pastda, 2-band).

"Diagnostikaga yozilish" tugmasi quiz ochadi: har qadamda bitta savol, oxirgi qadam — ism va telefon.
Savollar ixtiyoriy; har qadamda "Savollarsiz raqam qoldirish" yo‘li bor. Bitta javobli savolda variant bosilishi bilan
keyingi savol ochiladi (klaviaturada — "Davom etish" tugmasi). Oyna yopilsa, javoblar saqlanib qoladi.

Savollar `content.py` da: `quiz` ro‘yxati (UZ va RU da `key` va variant kodlari bir xil bo‘lishi shart — generator tekshiradi).
Birinchi savol variantlari — `pains` sarlavhalarining o‘zi (`PAIN_CODES` shu tartibda). Savol qo‘shish yoki o‘zgartirish uchun
faqat `content.py` ni tahrirlab, qayta yig‘ing: sahifalar ham, `api/lead-quiz.php` ham yangilanadi.

1. Sayt `api/lead.php` ga javob kodlari va kontaktni yuboradi → u Telegram bot orqali sizga xabar jo‘natadi → mijoz "qabul qilindi"ni ko‘radi.
   Server faqat `lead-quiz.php` dagi kodlarni qabul qiladi, xabarga ularning o‘zbekcha yozuvi tushadi.
2. Endpoint sozlanmagan yoki xato bersa — mijozga "Telegram’da yuborish" tugmasi chiqadi (matn javoblar bilan tayyor). Lid yo‘qolmaydi.

Sozlash (bir marta, serverda): cPanel File Manager’da `business/api/lead-config.sample.php` ni `lead-config.php` deb
nusxalab, bot tokeni va chat id ni yozing (yo‘riqnoma fayl ichida). **`lead-config.php` git’ga qo‘shilmaydi**
(`.gitignore` da) — repozitoriy ochiq, token esa sir. FTP deploy serverdagi bu faylga tegmaydi.
Sozlagach saytdan bitta test ariza yuboring.

### Formani lokal sinash

Bu Mac’da PHP yo‘q, lekin Docker bor. Haqiqiy bot kerak emas — `lead.php` soxta Telegram’ga yuboradi:

```bash
node tools/business/mock-telegram.js   # soxta Telegram API: kelgan xabarlarni terminalga chiqaradi (…8774 fail — xato qaytaradi)
docker run --rm -p 127.0.0.1:8773:8080 -v "$PWD/site":/app php:8.3-cli php -S 0.0.0.0:8080 -t /app   # http://localhost:8773/business/
```

Lokal `site/business/api/lead-config.php` (git’ga tushmaydi) ichida:
`return ['bot_token' => 'TEST', 'chat_id' => '1', 'api_base' => 'http://host.docker.internal:8774'];`
Bir manzildan 10 daqiqada 5 tadan ortiq ariza — `429`; hisoblagich konteyner qayta ishga tushganda nolga qaytadi.

## Analitika

`content.py` → `SETTINGS["metrika_id"]` ga Yandex Metrika hisoblagich raqamini yozing. Maqsadlar (goals) tayyor:
`lead_open`, `quiz_step_2` … `quiz_step_6` (qaysi qadamgacha yetib kelgani), `quiz_skip`, `lead_sent`, `lead_fallback`, `lead_fallback_sent`.

## Hali qilinmagan

- [ ] `TASDIQLANG` bandlari (yuridik shakl, segment, muddatlar, narx siyosati, qaysi tizimlar bilan ishlaysiz)
- [ ] Uchta keysdagi faktlarni tekshirish; birinchi SMB keyslari paydo bo‘lgach — almashtirish
- [ ] Haqiqiy mijoz fikrlari (hozircha bo‘lim yo‘q — o‘ylab topilmaydi)
- [ ] Bot tokeni (`lead-config.php`) + Metrika ID
- [ ] "10+ yil" — CV PDF’da "8 yildan ortiq" deb yozilgan; bitta raqamga keltirish
