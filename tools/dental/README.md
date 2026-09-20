# Stomatologiya sahifasi — ravshancha.uz/dental/

Stomatologiya klinikalari egalari va stomatologlar uchun landing: Dental Navigator platformasi nima beradi,
uni kim qurgan va klinika qanday ulanadi. Asosiy tugma — `dentalnavigator.uz/apply` (klinika arizasi).
Sahifa `/business/` nusxasi emas: tuzilma, matn va palitra (Dental Navigator ko‘k rangi, yorug‘ rejim birinchi)
stomatologiya uchun noldan yozilgan; shrift, tugmalar va komponentlar ravshancha.uz bilan bir xil — brend bitta.

## Tuzilma

```
tools/dental/content.py      barcha matnlar (UZ + RU), kontaktlar, sozlamalar — FAQAT SHU YERDA tahrirlang
tools/dental/template.html   sahifa shabloni (CSS + JS ichida)
tools/dental/build_site.py   generator → site/dental/index.html (uz), site/dental/ru/index.html (ru), sitemap.xml
tools/dental/build_og.py     ijtimoiy tarmoq rasmlari → site/dental/assets/og-{uz,ru}.jpg (Pillow kerak)
site/dental/assets/          logo, favicon, portret, Dental Navigator logotipi (product-logo.png), OG-rasmlar
```

`site/dental/index.html` va `site/dental/ru/index.html` generatsiya qilinadi — qo‘lda tahrirlanmaydi.

## Ishlatish

```bash
python3 tools/dental/build_site.py   # matn o‘zgargach qayta yig‘ish (faqat standart kutubxona)
python3 tools/dental/build_og.py     # faqat og_lines / og_sub, portret yoki logotip o‘zgarsa
node tools/business/serve.js         # lokal ko‘rish: http://localhost:8772/dental/ (butun site/ papkasi)
```

Qayta yig‘ilgan sahifalarni `content.py` bilan birga commit qiling; `development` ga push — deploy.

## Urg‘u: “stomatologiya” so‘zlari

Sahifa tor nishaga qaratilgan, shuning uchun nisha so‘zlari ataylab ko‘rinadigan qilingan:

- `content.py` da `[[stomatologiya]]` deb o‘ralgan so‘z sahifada `<strong class="kw">` bo‘ladi: sarlavhada — urg‘u rangi,
  matnda — marker bilan belgilangan qalin so‘z. `title`, `description`, JSON-LD va `alt` larga belgisiz, oddiy matn tushadi.
- Hero sarlavhasidagi asosiy so‘z — `<span class="accent-word">`.
- Generator har yig‘ishda so‘z o‘zagi (`KEYWORD_STEM`: uz `stomatolog`, ru `стоматолог`) matnda necha marta uchrashini
  va nechta joyda urg‘u berilganini chiqaradi. Me’yor — o‘qilishi tabiiy bo‘lsin; so‘zni sun’iy tiqishtirmang.

## Faktlar qayerdan

Mahsulot haqidagi hamma gap Dental Navigator repozitoriysidan olingan, o‘ylab topilmagan:
tariflar va qoidalar — `technical-document/docs/02-purpose-and-goals/business-model.md`, ulanish tartibi — saytdagi
`/apply` formasi matnlari, kabinet bo‘limlari — klinika kabineti menyusi, onlayn yozilish — saytdagi bron oynasi.
Bular hujjat va kod; amaldagi holatga mosligini faqat Ravshanjon tasdiqlaydi — shuning uchun `TASDIQLANG` belgilari.
Generator oxirida tasdiqlanmagan bandlar ro‘yxatini chiqaradi.

Tariflar bo‘limini butunlay yashirish: `content.py` → `SETTINGS["show_tariffs"] = False` (menyu bandi ham yo‘qoladi).
Bunda “Bu pullikmi?” savolidagi narxni ham olib tashlang.

## Forma (qo‘ng‘iroq so‘rovi)

“Qo‘ng‘iroq buyurtma qilish” formasi `/business/api/lead.php` ga yuboradi (`SETTINGS["lead_endpoint"]`) — alohida endpoint
va ikkinchi bot tokeni kerak emas. Telegram xabarida `Sahifa: /dental/` qatori lid qayerdan kelganini ko‘rsatadi.
Endpoint sozlanmagan yoki xato bersa — mehmonga “Telegram’da yuborish” tugmasi chiqadi (matn tayyor), lid yo‘qolmaydi.
`/business/` boshqa domenga ko‘chsa, `lead_endpoint` ni yangilang.

## Analitika

`SETTINGS["metrika_id"]` ga Yandex Metrika raqamini yozing. Maqsadlar tayyor: `click_apply`, `click_product`,
`lead_open`, `lead_sent`, `lead_fallback`, `lead_fallback_sent`, `click_tel`, `click_telegram`, `click_whatsapp`, `click_cv`.

## Hali qilinmagan

- [ ] `TASDIQLANG` bandlari: ochiq yoziladigan lavozim, tariflar va narx, “komissiya yo‘q / o‘rin sotilmaydi / bepul ko‘rik”
      qoidalari, prod’da ochiq kabinet bo‘limlari, “13 kishilik jamoa”
- [ ] Haqiqiy klinika keyslari va fikrlari (hozircha bo‘lim yo‘q — o‘ylab topilmaydi); klinikalar soni ham yozilmagan
- [ ] Kabinetning haqiqiy skrinshotlari (hozir sahifada mahsulot rasmi yo‘q)
- [ ] dentalnavigator.uz saytidan shu sahifaga (“platforma ortida kim”) qaytma havola
- [ ] Bot tokeni (`/business/api/lead-config.php`) + Metrika ID
