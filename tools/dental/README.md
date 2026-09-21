# Stomatologiya sahifasi — ravshancha.uz/dental/

Stomatologiya klinikalari egalari va stomatologlar uchun landing: Dental Navigator platformasi nima beradi,
uni kim qurgan va klinika qanday ulanadi. Asosiy tugma — `dentalnavigator.uz/apply` (klinika arizasi).
Sahifa `/business/` nusxasi emas: tuzilma, matn va palitra (Dental Navigator ko‘k rangi, yorug‘ rejim birinchi)
stomatologiya uchun noldan yozilgan; shrift, tugmalar va komponentlar ravshancha.uz bilan bir xil — brend bitta.

## Tuzilma

```
tools/dental/content.py      barcha matnlar (UZ + RU), kontaktlar, sozlamalar — FAQAT SHU YERDA tahrirlang
tools/dental/template.html   sahifa shabloni (CSS + JS ichida)
tools/dental/build_site.py   generator → site/dental/index.html (uz), site/dental/ru/index.html (ru),
                             yo‘nalish sahifalari site/dental/[ru/]<slug>/index.html, sitemap.xml
tools/dental/build_og.py     ijtimoiy tarmoq rasmlari → site/dental/assets/og-{uz,ru}.jpg, og-<slug>-{uz,ru}.jpg (Pillow kerak)
site/dental/assets/          logo, favicon, portret, Dental Navigator logotipi (product-logo.png), OG-rasmlar
```

`site/dental/` dagi barcha `index.html` lar generatsiya qilinadi — qo‘lda tahrirlanmaydi.

## Ishlatish

```bash
python3 tools/dental/build_site.py   # matn o‘zgargach qayta yig‘ish (faqat standart kutubxona)
python3 tools/dental/build_og.py     # faqat og_lines / og_sub, portret yoki logotip o‘zgarsa
python3 tools/dental/build_og.py sedatsiya   # faqat bitta sahifaning rasmlari (main — asosiy sahifa)
node tools/business/serve.js         # lokal ko‘rish: http://localhost:8772/dental/ (butun site/ papkasi)
```

Qayta yig‘ilgan sahifalarni `content.py` bilan birga commit qiling; `development` ga push — deploy.

## Yo‘nalish sahifalari

Har bir yo‘nalishning ikki sahifasi bor (ikkala tilda):

| Sahifa | Kim uchun | UZ | RU |
|---|---|---|---|
| Bemorlar | yo‘nalish nima, kimga mos, qanday o‘tadi, klinikani qanday tanlash; tugma — dentalnavigator.uz katalogi | `/dental/sedatsiya/` | `/dental/ru/sedatsiya/` |
| Klinikalar | asosiy sahifa kabi: bu yo‘nalishni qidirayotgan bemorlarga ko‘rsating; tugma — `/apply` | `/dental/sedatsiya/klinikalar/` | `/dental/ru/sedatsiya/klinikalar/` |

Shablon bitta: `template.html` dagi `<!-- clinics:start -->` / `<!-- patients:start -->` bloklari sahifa turiga qarab
qoldiriladi yoki olib tashlanadi (menyu, kontent, footer tugmalari, qo‘ng‘iroq formasi). `content.py` → `DIRECTIONS["<slug>"]`:
`clinics` da faqat asosiy sahifadan farq qiladigan kalitlar (+ `direction_name`, `breadcrumb_nav_label`, `patients_link_label`),
`patients` da bemorlar sahifasining matni. Bemorlar sahifasida narx yo‘q, klinikalar formasi ham yo‘q.

Havolalar: asosiy sahifa → klinikalar sahifasi (“Platforma” bo‘limi); klinikalar sahifasi → bemorlar sahifasi va breadcrumb
orqali asosiy sahifaga; bemorlar sahifasining footeri → klinikalar sahifasi. Sitemap va hreflang avtomatik.
Yangi yo‘nalish: `DIRECTIONS` ga yangi blok → `build_site.py` → `build_og.py <slug>`.

Sayt tugmalari: har bir sahifa footerining pastki qatorida (© yonida) ravshancha.uz ning barcha sahifalari turadi —
Rezyume, Biznes, Stomatologiya va har bir yo‘nalishning ikki sahifasi: bemorlar (`DIRECTIONS["<slug>"]["footer_label"]`)
va klinikalar (`footer_label_clinics`). O‘qilayotgan sahifaning tugmasi havola emas, belgilangan holatda turadi
(`aria-current`). Xuddi shu besh tugma CV sayt (`site/index.html`) va `/business/` (`tools/business/`) footerida ham
bor — ular yo‘nalishlar ro‘yxatini bilmaydi, shuning uchun yangi yo‘nalish tugmalarini u yerga qo‘lda qo‘shing.

Eslatma: dentalnavigator.uz katalogidagi 12 yo‘nalish orasida sedatsiya yo‘q, shuning uchun klinikalar sahifasi uni klinika
*xizmati* sifatida ko‘rsatadi — bu `TASDIQLANG` bilan belgilangan. Bemorlar sahifasidagi tibbiy matn umumiy ma’lumot;
e’lon qilishdan oldin shifokor (anesteziolog) ko‘zdan kechirgani ma’qul.

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

Tariflar (narxlar) hozir yashirilgan: `SETTINGS["show_tariffs"] = False` — bo‘lim ham, menyu bandi ham chiqmaydi.
Qaytarish uchun `True` qiling va “Bu pullikmi?” savoliga narxni qaytaring.

## Forma (qo‘ng‘iroq so‘rovi)

“Qo‘ng‘iroq buyurtma qilish” formasi `/api/lead.php` ga yuboradi (`SETTINGS["lead_endpoint"]`) — uchala sayt uchun
bitta endpoint. Ariza umumiy "Lidlar" jadvaliga tushadi, `Manba` ustunida `dental` deb turadi.
Endpoint sozlanmagan yoki xato bersa — mehmonga “Telegram’da yuborish” tugmasi chiqadi (matn tayyor), lid yo‘qolmaydi.
Sahifa boshqa domenga ko‘chsa, `lead_endpoint` ni yangilang.

## Analitika

`SETTINGS["metrika_id"]` ga Yandex Metrika raqamini yozing. Maqsadlar tayyor: `click_apply`, `click_product`,
`lead_open`, `lead_sent`, `lead_fallback`, `lead_fallback_sent`, `click_tel`, `click_telegram`, `click_whatsapp`, `click_cv`.

## Hali qilinmagan

- [ ] `TASDIQLANG` bandlari: ochiq yoziladigan lavozim, tariflar va narx, “komissiya yo‘q / o‘rin sotilmaydi / bepul ko‘rik”
      qoidalari, prod’da ochiq kabinet bo‘limlari, “13 kishilik jamoa”
- [ ] Haqiqiy klinika keyslari va fikrlari (hozircha bo‘lim yo‘q — o‘ylab topilmaydi); klinikalar soni ham yozilmagan
- [ ] Kabinetning haqiqiy skrinshotlari (hozir sahifada mahsulot rasmi yo‘q)
- [ ] dentalnavigator.uz saytidan shu sahifaga (“platforma ortida kim”) qaytma havola
- [ ] Metrika ID
