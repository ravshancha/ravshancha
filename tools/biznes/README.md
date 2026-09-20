# Sotuvchi sayt — ravshancha.uz/biznes/

Biznes egalari uchun landing: jarayonlarni avtomatlashtirish, og‘riqlarni davolash, shaffoflik.
Dizayn va kod asosi CV saytdan (`site/index.html`) olingan. CV sayt ishonch uchun tayanch bo‘lib qoladi:
bu sayt unga "Rezyume" havolalari orqali suyanadi, CV sayt footer’idagi "Biznes uchun xizmatlar" tugmasi esa shu yerga olib keladi.

## Tuzilma

```
tools/biznes/content.py      barcha matnlar (UZ + RU), kontaktlar, sozlamalar — FAQAT SHU YERDA tahrirlang
tools/biznes/template.html   sahifa shabloni (CSS + JS ichida, CV sayt uslubida)
tools/biznes/build_site.py   generator → site/biznes/index.html (uz), site/biznes/ru/index.html (ru), sitemap.xml
tools/biznes/serve.js        lokal ko‘rish: butun site/ papkasi
site/biznes/api/lead.php     forma → Telegram bot (serverda ishlaydi)
site/biznes/.htaccess        lead-config fayllarini yopadi
```

`site/biznes/index.html` va `site/biznes/ru/index.html` generatsiya qilinadi — qo‘lda tahrirlanmaydi.
Logo, favicon, portret va OG-rasm CV sayt bilan umumiy: `site/assets/` (`SETTINGS["assets"] = "../assets/"`).

## Ishlatish

```bash
python3 tools/biznes/build_site.py   # matn o‘zgargach qayta yig‘ish (faqat standart kutubxona)
node tools/biznes/serve.js           # http://localhost:8772/ (CV) va http://localhost:8772/biznes/
```

Qayta yig‘ilgan sahifalarni `content.py` bilan birga commit qiling; `development` ga push — deploy.
Generator oxirida `TASDIQLANG` deb belgilangan, hali tasdiqlanmagan va’da/faktlar ro‘yxatini chiqaradi.

## Nega har til — alohida URL

CV saytda til JS bilan almashadi, shuning uchun Google faqat o‘zbekcha versiyani ko‘radi.
Bu yerda `/biznes/` (uz) va `/biznes/ru/` — alohida statik sahifalar, `hreflang` bilan: ruscha qidiruvda ham chiqadi.
Yangi til qo‘shish: `content.py` da `LANGS` va `L["en"]` ni to‘ldirish kifoya.

## Forma (lidlar)

1. Sayt `api/lead.php` ga yuboradi → u Telegram bot orqali sizga xabar jo‘natadi → mijoz "qabul qilindi"ni ko‘radi.
2. Endpoint sozlanmagan yoki xato bersa — mijozga "Telegram’da yuborish" tugmasi chiqadi (matn tayyor). Lid yo‘qolmaydi.

Sozlash (bir marta, serverda): cPanel File Manager’da `biznes/api/lead-config.sample.php` ni `lead-config.php` deb
nusxalab, bot tokeni va chat id ni yozing (yo‘riqnoma fayl ichida). **`lead-config.php` git’ga qo‘shilmaydi**
(`.gitignore` da) — repozitoriy ochiq, token esa sir. FTP deploy serverdagi bu faylga tegmaydi.
`lead.php` lokal muhitda sinalmagan (bu Mac’da PHP yo‘q) — sozlagach bitta test ariza yuboring.

## Analitika

`content.py` → `SETTINGS["metrika_id"]` ga Yandex Metrika hisoblagich raqamini yozing. Maqsadlar (goals) tayyor:
`lead_open`, `lead_sent`, `lead_fallback`, `lead_fallback_sent`, `click_tel`, `click_telegram`, `click_whatsapp`, `click_cv`.

## Hali qilinmagan

- [ ] `TASDIQLANG` bandlari (yuridik shakl, segment, muddatlar, narx siyosati, qaysi tizimlar bilan ishlaysiz)
- [ ] Uchta keysdagi faktlarni tekshirish; birinchi SMB keyslari paydo bo‘lgach — almashtirish
- [ ] Haqiqiy mijoz fikrlari (hozircha bo‘lim yo‘q — o‘ylab topilmaydi)
- [ ] Sotuvchi sayt uchun alohida OG-rasm (hozir CV saytniki)
- [ ] Bot tokeni (`lead-config.php`) + Metrika ID
- [ ] "10+ yil" — CV PDF’da "8 yildan ortiq" deb yozilgan; bitta raqamga keltirish
