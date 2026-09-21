# -*- coding: utf-8 -*-
# Copy of the dentistry page (ravshancha.uz/dental/) in Uzbek and Russian. Edit here, then run build_site.py.
# L          — the main page. DIRECTIONS — one page per direction (ravshancha.uz/dental/[ru/]<slug>/): the main page's
#              copy with the direction's own keys laid over it, so only what differs is written there.
#
# [[word]]   — keyword emphasis: the page is aimed at dentistry, so "stomatologiya / stomatolog" (ru: "стоматология /
#              стоматолог") are wrapped in [[...]] and rendered as <strong class="kw">. Meta tags get the plain text.
# TASDIQLANG — a promise or a fact that Ravshanjon has to confirm before the page goes live.
#              Product facts come from the Dental Navigator repository (business model, apply form, clinic cabinet);
#              nothing here may be invented: no made-up clinics, numbers or testimonials.

SETTINGS = dict(
    base_url="https://ravshancha.uz/dental/",  # public address of this page, with a trailing slash
    assets="assets/",  # this page owns its images (site/dental/assets)
    cv_url="https://ravshancha.uz/",
    person="Ravshanjon Ismoilov",
    product="Dental Navigator",
    product_url="https://dentalnavigator.uz/",
    apply_url="https://dentalnavigator.uz/apply",  # the clinic application form — the main call to action
    catalog_url="https://dentalnavigator.uz/clinics",  # patient pages: the clinic catalog — their main call to action
    map_url="https://dentalnavigator.uz/map",
    lead_endpoint="/api/lead.php",  # callback form: one endpoint for all three sites, it writes into the shared spreadsheet
    phone_display="+998 99 942 07 70",
    phone_e164="+998999420770",
    telegram="ravshanjon_ismoilov",
    whatsapp="998999420770",
    linkedin="https://www.linkedin.com/in/ravshancha",
    metrika_id="",  # Yandex Metrika counter id; empty = no analytics script is emitted
    show_tariffs=False,  # narxlar sahifalarda ko‘rsatilmaydi; True = tariflar bo‘limi va menyu bandi qaytadi (narxlarni TASDIQLANG)
)

# Order matters: the first language is served at the page root.
LANGS = dict(
    uz=dict(code="UZ", name="O‘zbek", flag="flag-uz", path="", og_locale="uz_UZ"),
    ru=dict(code="RU", name="Русский", flag="flag-ru", path="ru/", og_locale="ru_RU"),
)

# The word stem that must stay prominent in each language; build_site.py reports how often it occurs.
KEYWORD_STEM = dict(uz="stomatolog", ru="стоматолог")

L = {}

L["uz"] = dict(
    # Search snippets: the title is cut at about 60 characters, the description at about 160.
    page_title="Stomatologiya klinikasi uchun platforma — Dental Navigator",
    description="Stomatologiya klinikalari va stomatologlar uchun Dental Navigator: katalogdagi sahifa, onlayn yozilish, grafik va kabinet. Klinikangizni bepul qo‘shing.",
    og_description="Stomatologiya klinikalari uchun: katalogdagi sahifa, onlayn yozilish, grafik va klinika kabineti — bitta platformada.",
    ld_name="Dental Navigator — stomatologiya klinikalari uchun platforma",
    ld_topic="Stomatologiya",
    ld_audience="Stomatologiya klinikalari egalari va stomatologlar",
    og_image_alt="Stomatologiya klinikangizga bemor onlayn yoziladi — Dental Navigator",
    og_lines=[("Stomatologiya", True), ("klinikangizga bemor", False), ("onlayn yoziladi.", False)],  # social preview headline: (text, accent)
    og_sub=["Katalog · Onlayn yozilish", "Grafik · Klinika kabineti"],
    footer_location="Toshkent, O‘zbekiston",

    skip_link="Kontentga o‘tish",
    nav_label="Asosiy navigatsiya",
    menu_label="Menyuni ochish",
    nav_platform="Platforma",
    nav_tariffs="Tariflar",
    nav_steps="Ulanish",
    nav_founder="Kim qurgan",
    nav_faq="Savollar",
    phone_label="+998 99 942 07 70 raqamiga qo‘ng‘iroq qilish",
    theme_label="Rang rejimini almashtirish",
    theme_dark="Qorong‘i",
    theme_light="Yorug‘",
    language_label="Til",
    back_to_top="Yuqoriga",
    footer_links_label="Aloqa havolalari",
    footer_cv="Rezyume",  # the footer's site buttons: these three and one per direction (its footer_label)
    footer_biz="Biznes uchun xizmatlar",
    footer_dental="Stomatologiya uchun",
    breadcrumb_label="Klinikalar uchun Dental Navigator",  # the first step of a direction page's breadcrumb
    directions_label="Yo‘nalishlar bo‘yicha sahifalar",

    hero_eyebrow="Stomatologiya klinikalari va stomatologlar uchun",
    hero_title_html='<span class="accent-word">Stomatologiya</span> klinikangizga bemor onlayn yoziladi.',
    hero_lead="Dental Navigator — faqat [[stomatologiya]] uchun qurilgan platforma. Klinikangiz katalogda ko‘rinadi, bemor narxlarni ko‘rib onlayn yoziladi, siz esa shifokorlar, grafik va yozuvlarni bitta kabinetda yuritasiz.",
    cta_primary="Klinikani qo‘shish",
    cta_telegram="Telegram’da yozish",
    cta_call="Qo‘ng‘iroq buyurtma qilish",
    hero_trust=[
        "Katalog va onlayn yozilish — bepul",  # TASDIQLANG: bepul tarif tarkibi (biznes-model: katalog sahifasi, yozuvlar, grafik)
        "Yozilgan bemor uchun komissiya yo‘q",  # TASDIQLANG: biznes-modeldagi qoida amaldami
        "Katalogdagi o‘rin sotilmaydi",  # TASDIQLANG: organik tartib, pullik o‘rin yo‘q
    ],
    portrait_alt="Ravshanjon Ismoilov — Dental Navigator rahbari",
    product_logo_alt="Dental Navigator logotipi",
    hero_badge_text="Stomatologiya platformasi",
    hero_chips_label="Platforma qismlari",
    hero_chips=[
        ("pin", "Katalog va xarita"),
        ("calendar", "Onlayn yozilish"),
        ("grid", "Klinika kabineti"),
    ],

    audience_kicker="Kim uchun",
    audience_title="Har qanday hajmdagi [[stomatologiya]] uchun.",
    audience_lead="Bir kresloli kabinetdan bir nechta filialli tarmoqqacha — platforma bir xil ishlaydi.",
    audience=[
        ("tooth", "Stomatologiya klinikasi", "1–3 kreslo",
         "Yangi bemorlar va to‘la grafik kerak. Katalogdagi sahifa va onlayn yozilish aynan shunga xizmat qiladi."),
        ("grid", "Stomatologiya tarmog‘i", "Bir nechta filial",
         "Har bir filialning shifokorlari, narxlari va yozuvlari o‘z kabinetida — hammasi bir xil tartibda."),
        ("user", "Xususiy stomatolog", "O‘z nomi bilan ishlaydi",
         "Bemor sizni ismingiz va yo‘nalishingiz bo‘yicha topadi: shifokor sahifasida ish joyingiz va sharhlar ko‘rinadi."),  # TASDIQLANG: xususiy shifokor qanday ulanadi
    ],

    pains_kicker="Tanish holatlar",
    pains_title="[[Stomatologiyada]] har kuni uchraydigan olti holat.",
    pains_lead="Bularning birortasi tanish bo‘lsa — sahifaning qolgan qismi siz uchun.",
    pains=[
        ("chat", "Bemor faqat tanish-bilish orqali keladi", "Yangi bemor sizni tanishidan yoki Instagram’dan topadi. Klinikangiz yaxshi bo‘lsa ham, stomatolog qidirayotgan odam sizni ko‘rmaydi."),
        ("doc", "Yozuvlar daftar va Telegram’da", "Administrator band bo‘lsa yoki javob berishni unutsa — bemor boshqa klinikaga yoziladi, siz esa bilmay qolasiz."),
        ("calendar", "Kreslo bo‘sh turadi", "Kim, qachon, qaysi shifokorga yozilgani bir joyda ko‘rinmaydi. Bo‘sh oynalar kech bilinadi va to‘lmay qoladi."),
        ("user", "Baza shifokor bilan ketadi", "Bemorlarning raqamlari shifokorning shaxsiy telefonida. Shifokor ketsa — bemorlar ham u bilan ketadi."),
        ("phone", "Bir xil savollar — kuniga o‘nlab marta", "“Narxi qancha?”, “Qachon bo‘sh?”, “Manzil qayerda?” Administrator vaqti qo‘ng‘iroqlarga ketadi, bemorga emas."),
        ("chart", "Raqamlar yo‘q", "Oyiga nechta yangi bemor keldi, qaysi shifokor band, qaysi xizmat ko‘p so‘raladi — hisobot yo‘q, qaror taxmin bilan qabul qilinadi."),
    ],
    pains_cta_text="Tanish holatmi? Klinikangizni qo‘shing yoki raqamingizni qoldiring — qo‘ng‘iroq qilib, platformani ko‘rsatib beramiz.",

    platform_kicker="Platforma",
    platform_title="Dental Navigator [[stomatologiya]] klinikasiga nima beradi.",
    platform_lead="Umumiy CRM emas: yo‘nalishlar, xizmatlar va narxlar — hammasi stomatologiya tilida.",
    result_label="Natija",
    features=[
        ("pin", "Katalogdagi sahifa", "Klinikangiz dentalnavigator.uz katalogida: manzil, ish vaqti, shifokorlar, xizmatlar va narxlar. Bemor sizni xaritadan, yo‘nalish yoki xizmat bo‘yicha topadi.",
         "Bemor qo‘ng‘iroq qilmasdan kerakli ma’lumotni ko‘radi.", ["Katalog", "Xarita", "Narxlar"]),
        ("calendar", "Onlayn yozilish va grafik", "Bemor xizmatni, kunni va bo‘sh vaqtni tanlab yoziladi — ro‘yxatdan o‘tmasdan, telefon raqami bilan. Yozuv darhol kabinetingizdagi kalendarga tushadi.",
         "Hamma yozuvlar bitta kalendarda.", ["Onlayn yozilish", "Kalendar", "Navbat"]),
        ("grid", "Klinika kabineti", "Shifokorlar, xodimlar, ish grafigi, xizmatlar va narxlarni o‘zingiz yuritasiz. Bemorlar bazasi klinikaniki: shifokor ketsa, uning kirish huquqi yopiladi, baza sizda qoladi.",  # TASDIQLANG: baza klinikada qolishi amalda shundaymi
         "Klinika bitta odamga bog‘liq bo‘lmaydi.", ["Shifokorlar", "Xodimlar", "Bemorlar"]),
        ("star", "Sharhlar va murojaatlar", "Bemor sharhlari va savollari kabinetga tushadi: javob berasiz, obro‘ingiz esa katalogda ko‘rinadi.",  # TASDIQLANG: sharhlar va murojaatlar prod’da ochiqmi
         "Obro‘ingiz tanish-bilishga emas, ochiq sharhlarga tayanadi.", ["Sharhlar", "Murojaatlar", "Hisobotlar"]),
    ],
    modules_label="Klinika kabineti bo‘limlari",
    modules=["Bronlar", "Kalendar", "Shifokorlar", "Xizmatlar va narxlar", "Bemorlar", "Navbat", "Sharhlar", "Murojaatlar", "Hisobotlar", "Xodimlar"],  # TASDIQLANG: qaysi bo‘limlar prod’da ochiq (nomlar kabinet menyusidan)

    tariffs_kicker="Tariflar",
    tariffs_title="[[Stomatologiya]] klinikasi uchun ikki tarif.",
    tariffs_lead="Chegara oddiy: bemorlarni jalb qilish — bepul, davolashni tizimda yuritish — pullik.",
    tariffs=[  # TASDIQLANG: narx va tarkib biznes-modeldan olingan — amaldagi holatga mosligini tekshiring
        dict(name="Bepul", price="0 so‘m", period="muddatsiz", text="Bemorlar sizni topishi va yozilishi uchun kerak bo‘lgan hammasi.",
             items=["Katalogdagi klinika sahifasi", "Onlayn yozuvlarni qabul qilish", "Shifokorlar grafigi"], featured=True),
        dict(name="Pullik", price="99 000 so‘m", period="filial uchun, oyiga", text="Davolashni ham tizimda yuritmoqchi bo‘lgan klinika uchun.",
             items=["Bepul tarifdagi hammasi", "Bemor kartalari va tish formulasi", "Davolash rejalari", "Kassa va hisobotlar"], featured=False),
    ],
    tariff_cta="Bepul boshlash",
    tariff_notes=[
        "Yozilgan bemor uchun komissiya olinmaydi.",  # TASDIQLANG
        "Katalogdagi tartib sotilmaydi: reklama alohida blokda va belgi bilan ko‘rsatiladi.",  # TASDIQLANG
        "Platformadagi har bir klinika bemorga oyiga bir marta bepul ko‘rik beradi — bu ishtirok sharti.",  # TASDIQLANG: shart hozir talab qilinadimi (saytdagi bron oynasida “Bepul ko‘rik” bor)
    ],

    steps_kicker="Ulanish",
    steps_title="[[Stomatologiya]] klinikangizni to‘rt qadamda ulaymiz.",
    steps_lead="Boshlash uchun kompyuter ham shart emas — ariza telefondan yuboriladi.",
    steps=[
        ("Ariza qoldirasiz", "dentalnavigator.uz/apply sahifasida ismingiz va klinika nomini yozasiz. Parol kerak emas — raqamingizga SMS-kod keladi."),
        ("Moderator tekshiradi", "Klinika haqiqatan sizniki ekanini tasdiqlaymiz. Litsenziya va klinika suratlarini birga yuborsangiz, tekshiruv tezroq o‘tadi; natijani SMS orqali bilasiz."),
        ("Kabinet ochiladi", "Shifokorlar, ish grafigi, xizmatlar va narxlarni kiritasiz."),
        ("Sahifangiz katalogda", "Bemorlar klinikangizni ko‘radi va onlayn yozila boshlaydi."),
    ],

    founder_kicker="Platforma ortida kim",
    founder_title="Bank tizimlarini qurgan muhandis — endi [[stomatologiya]] uchun.",
    founder_p1="Men Ravshanjon Ismoilov — Dental Navigator rahbariman. 10 yildan ortiq vaqt davomida xato qimmatga tushadigan tizimlarni qurganman: mobil va internet-banking, to‘lov tizimlari, davlat xizmatlari bilan integratsiyalar.",  # TASDIQLANG: ochiq yoziladigan lavozim — rahbar (CEO) / asoschi / hammuassis
    founder_p2="Bemorlar ma’lumoti ham pul kabi ehtiyotkorlik talab qiladi. Shu intizomni — xavfsizlik, ishonchlilik, aniq muddat — [[stomatologlar]] uchun platformaga olib keldim. Dental Navigator’ni 13 kishilik jamoa rivojlantiradi.",  # TASDIQLANG: “13 kishilik jamoa” deb yozsa bo‘ladimi
    facts=[
        ("clock", "Tajriba", "10+ yil bank va fintech tizimlari"),
        ("team", "Jamoa", "13 kishi: ishlab chiqish, mobil ilovalar, marketing"),  # TASDIQLANG
        ("link", "Integratsiyalar", "Uzcard · Humo · Paynet · davlat xizmatlari"),
        ("tooth", "Ixtisos", "Faqat stomatologiya — umumiy CRM emas"),
    ],
    founder_cv_link="To‘liq ish tajribasi va rezyume — ravshancha.uz",

    faq_kicker="Savollar",
    faq_title="[[Stomatologlar]] ko‘p beradigan savollar.",
    faq=[
        ("Bu pullikmi?", "Katalogdagi sahifa, onlayn yozuvlar va grafik — bepul. Davolashni tizimda yuritish (bemor kartalari, tish formulasi, davolash rejalari, kassa, hisobotlar) — pullik tarifda, shartlarini qo‘ng‘iroqda aytamiz. Yozilgan bemor uchun komissiya olinmaydi."),  # TASDIQLANG
        ("Bizda allaqachon CRM bor. Almashtirishimiz kerakmi?", "Yo‘q. Katalog va onlayn yozilish mavjud dasturingiz bilan yonma-yon ishlaydi: yangi yozuvlar kabinetga tushadi, qolgan ishni o‘rgangan dasturingizda davom ettirasiz."),
        ("Bemorlarim bazasi kimda qoladi?", "Klinikangizda. Boshqa klinikalar bemorlaringizni ko‘rmaydi. Shifokor ishdan ketsa, uning kirish huquqi yopiladi — baza klinikada qoladi."),  # TASDIQLANG
        ("Katalogda birinchi o‘rin sotiladimi?", "Yo‘q. Katalogdagi tartib sotilmaydi. Reklama alohida blokda va belgi bilan ko‘rsatiladi — qidiruv natijalariga ta’sir qilmaydi."),  # TASDIQLANG
        ("“Bepul ko‘rik” nima?", "Platformadagi har bir klinika bemorga oyiga bir marta bepul ko‘rik beradi. Bu — ishtirok sharti: bemor uchun kelishga sabab, klinika uchun esa yangi bemor bilan tanishish imkoni."),  # TASDIQLANG
        ("Ulanish qancha vaqt oladi?", "Ariza bir necha daqiqa oladi. Moderator tekshiruvidan keyin kabinet ochiladi; litsenziya va klinika suratlarini birga yuborsangiz, tekshiruv tezroq o‘tadi."),
        ("Toshkentdan tashqaridamiz — ulansak bo‘ladimi?", "Ha. Ariza ham, kabinet ham onlayn — O‘zbekistonning istalgan shahridagi stomatologiya ulanadi."),
    ],

    contact_kicker="Aloqa",
    contact_title_html="[[Stomatologiya]] klinikangizni bugun katalogga qo‘shamiz.",
    contact_text="Savolingiz bo‘lsa — to‘g‘ridan-to‘g‘ri yozing yoki qo‘ng‘iroq qiling. Javobni platforma rahbaridan olasiz.",

    order_title="Qo‘ng‘iroq buyurtma qilish",
    order_intro="Raqamingizni qoldiring — qo‘ng‘iroq qilib, platformani ko‘rsatib beramiz va savollaringizga javob beramiz.",
    order_name="Ismingiz",
    order_name_example="Masalan: Alisher Karimov",
    order_name_error="Ismingizni kiriting.",
    order_phone="Telefon raqamingiz",
    order_phone_example="Masalan: 99 942 07 70",
    order_phone_error="Faqat raqam, 9 ta belgi: 999420770.",
    order_info="Klinikangiz nomi va manzili (ixtiyoriy)",
    order_info_example="Masalan: “Smile Dent” stomatologiyasi, Yunusobod, 3 kreslo.",
    order_submit="Yuborish",
    order_sending="Yuborilmoqda…",
    order_cancel="Bekor qilish",
    order_consent="Yuborish orqali ma’lumotlaringizdan siz bilan bog‘lanish uchun foydalanishimizga rozilik bildirasiz.",
    order_success_title="So‘rovingiz qabul qilindi",
    order_success_text="Rahmat! Imkon qadar tez qo‘ng‘iroq qilamiz.",
    order_close="Yopish",
    order_fallback_text="So‘rovni avtomatik yuborib bo‘lmadi. Uni Telegram orqali yuboring — matn tayyor:",
    order_fallback_button="Telegram’da yuborish",
    order_fallback_note="Matn nusxalandi. Telegram’da xabar bo‘sh chiqsa — uni qo‘yib, yuboring.",
    order_message_title="Stomatologiya sahifasi — qo‘ng‘iroq so‘rovi",
    order_message_info="Klinika",

    sticky_label="Tezkor aloqa",
    sticky_call="Qo‘ng‘iroq",
)

L["ru"] = dict(
    page_title="Платформа для стоматологических клиник — Dental Navigator",
    description="Dental Navigator для стоматологий и стоматологов: страница в каталоге, онлайн-запись, расписание и кабинет клиники. Добавьте свою стоматологию бесплатно.",
    og_description="Для стоматологических клиник: страница в каталоге, онлайн-запись, расписание и кабинет клиники — на одной платформе.",
    ld_name="Dental Navigator — платформа для стоматологических клиник",
    ld_topic="Стоматология",
    ld_audience="Владельцы стоматологических клиник и стоматологи",
    og_image_alt="Пациенты записываются в вашу стоматологию онлайн — Dental Navigator",
    og_lines=[("Пациенты", False), ("записываются в вашу", False), ("стоматологию онлайн.", True)],
    og_sub=["Каталог · Онлайн-запись", "Расписание · Кабинет клиники"],
    footer_location="Ташкент, Узбекистан",

    skip_link="Перейти к содержанию",
    nav_label="Основная навигация",
    menu_label="Открыть меню",
    nav_platform="Платформа",
    nav_tariffs="Тарифы",
    nav_steps="Подключение",
    nav_founder="Кто создал",
    nav_faq="Вопросы",
    phone_label="Позвонить по номеру +998 99 942 07 70",
    theme_label="Переключить цветовую тему",
    theme_dark="Тёмная",
    theme_light="Светлая",
    language_label="Язык",
    back_to_top="Наверх",
    footer_links_label="Контактные ссылки",
    footer_cv="Резюме",
    footer_biz="Услуги для бизнеса",
    footer_dental="Для стоматологии",
    breadcrumb_label="Dental Navigator для клиник",
    directions_label="Страницы по направлениям",

    hero_eyebrow="Для стоматологических клиник и стоматологов",
    hero_title_html='Пациенты записываются в вашу <span class="accent-word">стоматологию</span> онлайн.',
    hero_lead="Dental Navigator — платформа, созданная только для [[стоматологии]]. Клиника видна в каталоге, пациент смотрит цены и записывается онлайн, а вы ведёте врачей, расписание и записи в одном кабинете.",
    cta_primary="Добавить клинику",
    cta_telegram="Написать в Telegram",
    cta_call="Заказать звонок",
    hero_trust=[
        "Каталог и онлайн-запись — бесплатно",  # TASDIQLANG
        "Без комиссии за записавшегося пациента",  # TASDIQLANG
        "Место в каталоге не продаётся",  # TASDIQLANG
    ],
    portrait_alt="Равшанжон Исмоилов — руководитель Dental Navigator",
    product_logo_alt="Логотип Dental Navigator",
    hero_badge_text="Платформа для стоматологии",
    hero_chips_label="Части платформы",
    hero_chips=[
        ("pin", "Каталог и карта"),
        ("calendar", "Онлайн-запись"),
        ("grid", "Кабинет клиники"),
    ],

    audience_kicker="Для кого",
    audience_title="Для [[стоматологии]] любого размера.",
    audience_lead="От кабинета на одно кресло до сети с несколькими филиалами — платформа работает одинаково.",
    audience=[
        ("tooth", "Стоматологическая клиника", "1–3 кресла",
         "Нужны новые пациенты и заполненное расписание. Страница в каталоге и онлайн-запись работают именно на это."),
        ("grid", "Сеть стоматологий", "Несколько филиалов",
         "Врачи, цены и записи каждого филиала — в своём кабинете, и всё устроено одинаково."),
        ("user", "Частный стоматолог", "Работает под своим именем",
         "Пациент находит вас по имени и направлению: на странице врача видны место работы и отзывы."),  # TASDIQLANG
    ],

    pains_kicker="Знакомые ситуации",
    pains_title="Шесть ситуаций, которые в [[стоматологии]] случаются каждый день.",
    pains_lead="Если знакома хотя бы одна — остальная часть страницы для вас.",
    pains=[
        ("chat", "Пациенты приходят только по знакомству", "Новый пациент узнаёт о вас от знакомых или из Instagram. Даже хорошую клинику не видит человек, который прямо сейчас ищет стоматолога."),
        ("doc", "Записи — в тетради и в Telegram", "Администратор занят или забыл ответить — пациент записывается в другую клинику, а вы об этом даже не узнаёте."),
        ("calendar", "Кресло простаивает", "Кто, когда и к какому врачу записан — в одном месте не видно. Свободные окна замечают поздно, и они остаются пустыми."),
        ("user", "База уходит вместе с врачом", "Номера пациентов — в личном телефоне врача. Уходит врач — уходят и пациенты."),
        ("phone", "Одни и те же вопросы — десятки раз в день", "«Сколько стоит?», «Когда свободно?», «Где вы находитесь?» Время администратора уходит на звонки, а не на пациента."),
        ("chart", "Нет цифр", "Сколько новых пациентов пришло за месяц, какой врач загружен, какую услугу спрашивают чаще — отчёта нет, решения принимаются наугад."),
    ],
    pains_cta_text="Знакомо? Добавьте клинику или оставьте номер — позвоним, покажем платформу и ответим на вопросы.",

    platform_kicker="Платформа",
    platform_title="Что Dental Navigator даёт [[стоматологической]] клинике.",
    platform_lead="Не универсальная CRM: направления, услуги и цены — всё на языке стоматологии.",
    result_label="Результат",
    features=[
        ("pin", "Страница в каталоге", "Ваша клиника в каталоге dentalnavigator.uz: адрес, режим работы, врачи, услуги и цены. Пациент находит вас на карте, по направлению или по услуге.",
         "Пациент видит нужное, не звоня в клинику.", ["Каталог", "Карта", "Цены"]),
        ("calendar", "Онлайн-запись и расписание", "Пациент выбирает услугу, день и свободное время и записывается — без регистрации, по номеру телефона. Запись сразу попадает в календарь вашего кабинета.",
         "Все записи — в одном календаре.", ["Онлайн-запись", "Календарь", "Лист ожидания"]),
        ("grid", "Кабинет клиники", "Врачей, сотрудников, расписание, услуги и цены вы ведёте сами. База пациентов принадлежит клинике: если врач уходит, его доступ закрывается, а база остаётся у вас.",  # TASDIQLANG
         "Клиника не зависит от одного человека.", ["Врачи", "Сотрудники", "Пациенты"]),
        ("star", "Отзывы и обращения", "Отзывы и вопросы пациентов приходят в кабинет: вы отвечаете, а репутация видна в каталоге.",  # TASDIQLANG
         "Репутация держится на открытых отзывах, а не на знакомствах.", ["Отзывы", "Обращения", "Отчёты"]),
    ],
    modules_label="Разделы кабинета клиники",
    modules=["Записи", "Календарь", "Врачи", "Услуги и цены", "Пациенты", "Лист ожидания", "Отзывы", "Обращения", "Отчёты", "Сотрудники"],  # TASDIQLANG

    tariffs_kicker="Тарифы",
    tariffs_title="Два тарифа для [[стоматологической]] клиники.",
    tariffs_lead="Граница простая: привлечение пациентов — бесплатно, ведение лечения в системе — платно.",
    tariffs=[  # TASDIQLANG
        dict(name="Бесплатный", price="0 сум", period="без срока", text="Всё, что нужно, чтобы пациенты находили вас и записывались.",
             items=["Страница клиники в каталоге", "Приём онлайн-записей", "Расписание врачей"], featured=True),
        dict(name="Платный", price="99 000 сум", period="за филиал в месяц", text="Для клиники, которая хочет вести в системе и лечение.",
             items=["Всё из бесплатного тарифа", "Карточки пациентов и зубная карта", "Планы лечения", "Касса и отчёты"], featured=False),
    ],
    tariff_cta="Начать бесплатно",
    tariff_notes=[
        "Комиссия за записавшегося пациента не берётся.",  # TASDIQLANG
        "Порядок в каталоге не продаётся: реклама показывается отдельным блоком с пометкой.",  # TASDIQLANG
        "Каждая клиника платформы раз в месяц даёт пациенту бесплатный осмотр — это условие участия.",  # TASDIQLANG
    ],

    steps_kicker="Подключение",
    steps_title="Подключаем вашу [[стоматологию]] за четыре шага.",
    steps_lead="Для начала не нужен даже компьютер — заявка отправляется с телефона.",
    steps=[
        ("Оставляете заявку", "На странице dentalnavigator.uz/apply указываете своё имя и название клиники. Пароль не нужен — на номер придёт SMS-код."),
        ("Модератор проверяет", "Подтверждаем, что клиника действительно ваша. Лицензия и фото клиники ускоряют проверку; результат придёт по SMS."),
        ("Открывается кабинет", "Вносите врачей, расписание, услуги и цены."),
        ("Страница в каталоге", "Пациенты видят клинику и начинают записываться онлайн."),
    ],

    founder_kicker="Кто стоит за платформой",
    founder_title="Инженер, строивший банковские системы, — теперь для [[стоматологии]].",
    founder_p1="Я Равшанжон Исмоилов — руководитель Dental Navigator. Больше 10 лет строил системы, где ошибка стоит дорого: мобильный и интернет-банкинг, платёжные системы, интеграции с государственными сервисами.",  # TASDIQLANG: должность
    founder_p2="Данные пациентов требуют той же аккуратности, что и деньги. Эту дисциплину — безопасность, надёжность, точные сроки — я принёс в платформу для [[стоматологов]]. Dental Navigator развивает команда из 13 человек.",  # TASDIQLANG: команда
    facts=[
        ("clock", "Опыт", "10+ лет банковских и финтех-систем"),
        ("team", "Команда", "13 человек: разработка, мобильные приложения, маркетинг"),  # TASDIQLANG
        ("link", "Интеграции", "Uzcard · Humo · Paynet · госсервисы"),
        ("tooth", "Специализация", "Только стоматология — не универсальная CRM"),
    ],
    founder_cv_link="Полный опыт работы и резюме — ravshancha.uz",

    faq_kicker="Вопросы",
    faq_title="Частые вопросы [[стоматологов]].",
    faq=[
        ("Это платно?", "Страница в каталоге, онлайн-записи и расписание — бесплатно. Ведение лечения в системе (карточки пациентов, зубная карта, планы лечения, касса, отчёты) — на платном тарифе, условия расскажем на звонке. Комиссия за записавшегося пациента не берётся."),  # TASDIQLANG
        ("У нас уже есть CRM. Её нужно менять?", "Нет. Каталог и онлайн-запись работают рядом с вашей программой: новые записи приходят в кабинет, а остальную работу вы продолжаете в привычной программе."),
        ("У кого остаётся база пациентов?", "У вашей клиники. Другие клиники ваших пациентов не видят. Если врач увольняется, его доступ закрывается — база остаётся в клинике."),  # TASDIQLANG
        ("Первое место в каталоге продаётся?", "Нет. Порядок в каталоге не продаётся. Реклама показывается отдельным блоком с пометкой и на результаты поиска не влияет."),  # TASDIQLANG
        ("Что такое «бесплатный осмотр»?", "Каждая клиника платформы раз в месяц даёт пациенту бесплатный осмотр. Это условие участия: пациенту — повод прийти, клинике — возможность познакомиться с новым пациентом."),  # TASDIQLANG
        ("Сколько времени занимает подключение?", "Заявка занимает несколько минут. После проверки модератором открывается кабинет; если сразу приложить лицензию и фото клиники, проверка пройдёт быстрее."),
        ("Мы не в Ташкенте — можно подключиться?", "Да. И заявка, и кабинет работают онлайн — подключается стоматология из любого города Узбекистана."),
    ],

    contact_kicker="Контакты",
    contact_title_html="Добавим вашу [[стоматологию]] в каталог уже сегодня.",
    contact_text="Есть вопрос — напишите или позвоните напрямую. Отвечает руководитель платформы.",

    order_title="Заказать звонок",
    order_intro="Оставьте номер — позвоним, покажем платформу и ответим на вопросы.",
    order_name="Ваше имя",
    order_name_example="Например: Алишер Каримов",
    order_name_error="Укажите имя.",
    order_phone="Номер телефона",
    order_phone_example="Например: 99 942 07 70",
    order_phone_error="Только цифры, 9 знаков: 999420770.",
    order_info="Название и адрес клиники (необязательно)",
    order_info_example="Например: стоматология «Smile Dent», Юнусабад, 3 кресла.",
    order_submit="Отправить",
    order_sending="Отправка…",
    order_cancel="Отмена",
    order_consent="Отправляя форму, вы соглашаетесь на использование данных для связи с вами.",
    order_success_title="Запрос принят",
    order_success_text="Спасибо! Позвоним как можно скорее.",
    order_close="Закрыть",
    order_fallback_text="Автоматически отправить запрос не получилось. Отправьте его через Telegram — текст уже готов:",
    order_fallback_button="Отправить в Telegram",
    order_fallback_note="Текст скопирован. Если сообщение в Telegram окажется пустым — вставьте его и отправьте.",
    order_message_title="Страница для стоматологий — запрос звонка",
    order_message_info="Клиника",

    sticky_label="Быстрая связь",
    sticky_call="Позвонить",
)


# Direction pages. The key is the address; every direction has two pages in every language:
#   patients — ravshancha.uz/dental/[ru/]<slug>/             for patients: what it is, who it suits, how to choose a clinic;
#                                                            the call to action is the Dental Navigator catalog. No prices.
#   clinics  — ravshancha.uz/dental/[ru/]<slug>/klinikalar/  for clinics, like the main page: show this direction to the
#                                                            patients who look for it. Only the keys that differ from the
#                                                            main page, plus direction_name (link text on the main page and
#                                                            the breadcrumb), breadcrumb_nav_label and patients_link_label.
# keyword_stem is the word build_site.py counts on both pages; footer_label names the patients' page among the
# footer's site buttons (the same label stands in the footers of ravshancha.uz and /business/ — keep them alike).
DIRECTIONS = {}

DIRECTIONS["sedatsiya"] = dict(
    keyword_stem=dict(uz="sedatsiya", ru="седац"),
    footer_label=dict(uz="Sedatsiya", ru="Седация"),
    patients=dict(
        uz=dict(
            direction_name="Tishlarni sedatsiya (narkoz) bilan davolash",
            page_title="Toshkentda tishlarni sedatsiya (narkoz) bilan davolash",
            description="Toshkentda tishlarni sedatsiya va narkoz bilan davolash: farqi nimada, kimga mos, davolash qanday o‘tadi va klinikani qanday tanlash kerak.",
            og_description="Sedatsiya narkozdan nimasi bilan farq qiladi, uyquda davolash kimga mos, qanday o‘tadi va klinikadan nimani so‘rash kerak.",
            ld_topic="Tishlarni sedatsiya (narkoz) bilan davolash",
            ld_audience="Patient",
            og_image_alt="Toshkentda tishlarni sedatsiya (narkoz) bilan davolash",
            og_lines=[("Tishlarni", False), ("sedatsiya (narkoz)", True), ("bilan davolash.", False)],
            og_sub=["Nima u, kimga mos, qanday o‘tadi", "va klinikani qanday tanlash kerak"],

            nav_what="Nima u",
            nav_who="Kimga mos",
            nav_process="Qanday o‘tadi",
            nav_safety="Klinika tanlash",
            cta_find="Klinika topish",
            cta_how="Davolash qanday o‘tadi",
            find_map="Xaritadagi klinikalar",
            footer_clinics="Klinikalar uchun",
            sticky_label="Tezkor havolalar",

            hero_image="sedatsiya-child-dentist.webp",
            hero_image_alt="Bolani mehr bilan ko‘rikdan o‘tkazayotgan stomatolog va xursand bola",
            consultation_image_alt="Stomatolog onaga davolash haqida tushuntirmoqda",
            family_image_alt="Klinikada xursand bola va uning onasi",
            preparation_image_alt="Shifokor stomatologiya xonasini davolashga tayyorlamoqda",
            monitoring_image_alt="Anesteziolog kuzatuv monitorini tekshirmoqda",
            hero_eyebrow="Bemorlar uchun · Toshkent",
            hero_title_html='Toshkentda tishlarni <span class="accent-word">sedatsiya (narkoz)</span> bilan davolash.',
            hero_lead="Qo‘rquv, kuchli qusish refleksi yoki davolash hajmining kattaligi — stomatologga borishni kechiktirishning ko‘p uchraydigan sabablari. [[Sedatsiya]] yoki [[narkoz]] bilan tishlar siz xotirjam yoki uxlab yotganingizda davolanadi. Farqi nimada, kimga mos va klinikani qanday tanlashni tushuntiramiz.",
            hero_trust=[
                "Sedatsiya va narkozni anesteziolog o‘tkazadi",
                "Davolash davomida holatingiz nazorat qilinadi",
                "Bir tashrifda bir nechta tishni davolash mumkin",
            ],
            hero_badge_text="Stomatologiyalar katalogi",
            hero_chips_label="Asosiy farqlar",
            hero_chips=[
                ("moon", "Sedatsiya — yengil uyqu"),
                ("shield", "Anesteziolog nazorati"),
                ("clock", "Bir tashrifda bir nechta tish"),
            ],

            what_kicker="Nima u",
            what_title="[[Sedatsiya]], narkoz va mahalliy og‘riqsizlantirish — farqi nimada.",
            what_lead="Og‘riqsizlantirish har qanday davolashda kerak. Farq — davolash paytida qanday holatda bo‘lishingizda.",
            what_cards=[
                ("moon", "Sedatsiya", "Yengil dori uyqusi",
                 "Siz bo‘shashgan va mudroq holatdasiz, o‘zingiz nafas olasiz va shifokorga javob bera olasiz. Qo‘rquv va zo‘riqish bo‘lmaydi, davolashning o‘zi esa keyin ko‘pincha deyarli esda qolmaydi."),
                ("shield", "Umumiy narkoz", "To‘liq uyqu",
                 "Siz to‘liq uxlaysiz va hech narsani sezmaysiz. Narkozni anesteziolog o‘tkazadi va butun davolash davomida nafas, puls va bosimni kuzatib turadi."),
                ("tooth", "Mahalliy og‘riqsizlantirish", "Siz hushingizdasiz",
                 "Faqat davolanadigan joy og‘riqsizlantiriladi. U oddiy davolashda ham, sedatsiya bilan birga ham qilinadi."),
            ],

            who_kicker="Kimga mos",
            who_title="Qachon shifokordan [[sedatsiya]] haqida so‘rash kerak.",
            who_lead="Yakuniy qarorni ko‘rikdan keyin stomatolog va anesteziolog qabul qiladi: sedatsiya va narkozning qarshi ko‘rsatmalari bor.",
            fits=[
                ("chat", "Stomatologdan kuchli qo‘rquv", "Qo‘rquv tufayli davolashni yillab kechiktirayotgan bo‘lsangiz, sedatsiya uni xotirjam o‘tkazishga yordam beradi."),
                ("user", "Davolanishdan qo‘rqadigan bolalar", "Bola davolatishga ko‘nmasa, narkoz bilan davolash hammasini bir martada va stresssiz qilish imkonini beradi."),
                ("clock", "Bir tashrifda ko‘p ish", "Bir nechta tish, murakkab olib tashlash yoki implantatsiya — bir necha tashrif o‘rniga bittada."),
                ("tooth", "Aql tishlari va murakkab olib tashlash", "Uzoq va noxush muolajalar uxlab yoki mudrab yotganingizda yengilroq o‘tadi."),
                ("doc", "Kuchli qusish refleksi", "Refleks hatto ko‘rikka xalaqit bersa, sedatsiya davolashni mumkin qiladi."),
                ("team", "Alohida ehtiyojlar", "Kresloda uzoq qimirlamay o‘tira olmaydigan bemorlar uchun uyquda davolash eng qulay yo‘l bo‘lishi mumkin."),
            ],

            process_kicker="Qanday o‘tadi",
            process_title="[[Sedatsiya]] bilan davolash — bosqichma-bosqich.",
            process_lead="Aniq tayyorgarlikni klinikangiz belgilaydi; quyida — umumiy tartib.",
            process=[
                ("Konsultatsiya va ko‘rik", "Stomatolog davolash rejasini tuzadi, anesteziolog salomatligingiz va ichayotgan dorilaringiz haqida so‘raydi, kerak bo‘lsa tahlillar buyuradi."),
                ("Tayyorgarlik", "Odatda sedatsiya yoki narkozdan oldin bir necha soat yeyish va ichish mumkin emas — aniq vaqtni klinika aytadi. O‘zingiz bilan kuzatuvchi olib keling."),
                ("Davolash", "Anesteziolog dori yuboradi va nafas, puls hamda bosimni doimiy kuzatib turadi, stomatolog esa xotirjam ishlaydi."),
                ("Tiklanish", "Dori ta’siri o‘tguncha klinikada dam olasiz va uyga kuzatuvchi bilan ketasiz. Shu kuni rulga o‘tirish mumkin emas."),
            ],

            safety_kicker="Klinika tanlash",
            safety_title="[[Sedatsiya]] bilan davolashdan oldin klinikadan nimani so‘rash kerak.",
            safety_lead="Yaxshi klinika bu savollarning barchasiga yozilishdan oldinoq xotirjam javob beradi.",
            checks=[
                "Sedatsiya yoki narkozni kim o‘tkazadi — anesteziologmi?",
                "Klinikada bu turdagi yordam uchun litsenziya bormi?",
                "Davolash paytida holat qanday kuzatiladi: monitor, kislorod bormi?",
                "Oldindan qanday tahlil va tekshiruvlar kerak?",
                "Qanday tayyorlanish kerak va tiklanish qancha davom etadi?",
                "Kim davolaydi va shifokor haqida sharhlarda nima yozilgan?",
            ],

            faq_title="[[Sedatsiya]] haqida ko‘p beriladigan savollar.",
            medical_note="Sahifadagi ma’lumotlar tanishish uchun berilgan va shifokor maslahatining o‘rnini bosmaydi.",
            faq=[
                ("Bu xavfsizmi?", "Stomatologiyada sedatsiya va narkoz — ko‘rikdan keyin anesteziolog o‘tkazsa va bemor holati nazorat qilinsa, odatiy amaliyot. Shuning uchun klinikadan kim va qanday o‘tkazishini oldindan so‘rash muhim."),
                ("Og‘riydimi?", "Yo‘q. Davolanadigan joy baribir og‘riqsizlantiriladi, sedatsiya yoki narkozda esa qo‘rquv va zo‘riqishni ham his qilmaysiz."),
                ("Sedatsiya narkozdan nimasi bilan farq qiladi?", "Sedatsiyada siz mudraysiz, o‘zingiz nafas olasiz va shifokorga javob bera olasiz. Umumiy narkozda to‘liq uxlaysiz. Qaysi biri mosligini shifokor va anesteziolog hal qiladi."),
                ("Bolalarni narkoz bilan davolasa bo‘ladimi?", "Ha, bolalar stomatologiyasida narkoz bilan davolash keng tarqalgan, ayniqsa ko‘p tishni davolash kerak bo‘lsa. Qaror bolani ko‘rikdan o‘tkazgandan keyin qabul qilinadi."),
                ("Davolash qancha davom etadi?", "Hajmga bog‘liq: bir tashrifda bir soatdan bir necha soatgacha. Bunga klinikada tiklanish vaqti qo‘shiladi."),
                ("Darhol ishga qaytsa bo‘ladimi?", "Uyga kuzatuvchi bilan borgan ma’qul, shu kuni rulga o‘tirish esa mumkin emas. Boshqa cheklovlar haqida klinika aytadi."),
            ],

            find_kicker="Klinika topish",
            find_title_html="Klinikani Dental Navigator katalogidan tanlang.",
            find_text="Katalogda — Toshkent stomatologiyalari: manzil, shifokorlar, xizmatlar va sharhlar; onlayn yozilish ham mumkin. Yozilishdan oldin klinikadan [[sedatsiya]] yoki narkoz bilan davolashini aniqlang.",
        ),
        ru=dict(
            direction_name="Лечение зубов с седацией (наркозом)",
            page_title="Лечение зубов с седацией (наркозом) в Ташкенте",
            description="Лечение зубов с седацией и под наркозом в Ташкенте: чем они отличаются, кому подходят, как проходит лечение и как выбрать клинику.",
            og_description="Чем седация отличается от наркоза, кому подходит лечение во сне, как оно проходит и что спросить у клиники.",
            ld_topic="Лечение зубов с седацией (наркозом)",
            ld_audience="Patient",
            og_image_alt="Лечение зубов с седацией (наркозом) в Ташкенте",
            og_lines=[("Лечение зубов", False), ("с седацией (наркозом)", True), ("в Ташкенте.", False)],
            og_sub=["Что это, кому подходит, как проходит", "и как выбрать клинику"],

            nav_what="Что это",
            nav_who="Кому подходит",
            nav_process="Как проходит",
            nav_safety="Выбор клиники",
            cta_find="Найти клинику",
            cta_how="Как проходит лечение",
            find_map="Клиники на карте",
            footer_clinics="Для клиник",
            sticky_label="Быстрые ссылки",

            hero_image="sedatsiya-child-dentist.webp",
            hero_image_alt="Стоматолог заботливо осматривает зубы довольного ребёнка",
            consultation_image_alt="Стоматолог объясняет матери план лечения",
            family_image_alt="Довольный ребёнок с мамой в клинике",
            preparation_image_alt="Врач готовит стоматологический кабинет к лечению",
            monitoring_image_alt="Анестезиолог проверяет монитор наблюдения",
            hero_eyebrow="Для пациентов · Ташкент",
            hero_title_html='Лечение зубов с <span class="accent-word">седацией (наркозом)</span> в Ташкенте.',
            hero_lead="Страх, сильный рвотный рефлекс или большой объём лечения — частые причины откладывать визит к стоматологу. С [[седацией]] или под [[наркозом]] зубы лечат, пока вы спокойны или спите. Рассказываем, чем они отличаются, кому подходят и как выбрать клинику.",
            hero_trust=[
                "Седацию и наркоз проводит анестезиолог",
                "Состояние контролируют всё время лечения",
                "Можно вылечить несколько зубов за визит",
            ],
            hero_badge_text="Каталог стоматологий",
            hero_chips_label="Главное",
            hero_chips=[
                ("moon", "Седация — лёгкий сон"),
                ("shield", "Контроль анестезиолога"),
                ("clock", "Несколько зубов за визит"),
            ],

            what_kicker="Что это",
            what_title="[[Седация]], наркоз и местная анестезия — в чём разница.",
            what_lead="Обезболивание нужно при любом лечении. Отличается то, в каком состоянии вы будете во время него.",
            what_cards=[
                ("moon", "Седация", "Лёгкий медикаментозный сон",
                 "Вы расслаблены и дремлете, дышите сами и можете отвечать врачу. Страха и напряжения нет, а само лечение потом часто почти не вспоминается."),
                ("shield", "Общий наркоз", "Полный сон",
                 "Вы полностью спите и ничего не чувствуете. Наркоз проводит анестезиолог — он же всё лечение следит за дыханием, пульсом и давлением."),
                ("tooth", "Местная анестезия", "Вы в сознании",
                 "Обезболивается только зона лечения. Её делают и при обычном лечении, и вместе с седацией."),
            ],

            who_kicker="Кому подходит",
            who_title="Когда стоит спросить врача о [[седации]].",
            who_lead="Окончательно решают стоматолог и анестезиолог после осмотра: у седации и наркоза есть противопоказания.",
            fits=[
                ("chat", "Сильный страх стоматолога", "Если из-за страха вы годами откладываете лечение, седация помогает пройти его спокойно."),
                ("user", "Дети, которые боятся лечения", "Когда ребёнок не даётся лечить, лечение под наркозом позволяет сделать всё за один раз и без стресса."),
                ("clock", "Много работы за один визит", "Несколько зубов, сложное удаление или имплантация — за один визит вместо нескольких."),
                ("tooth", "Зубы мудрости и сложное удаление", "Долгие и неприятные вмешательства переносятся легче, когда вы спите или дремлете."),
                ("doc", "Сильный рвотный рефлекс", "Если рефлекс мешает даже осмотру, седация делает лечение возможным."),
                ("team", "Особые потребности", "Тем, кому трудно долго сидеть в кресле неподвижно, лечение во сне может быть самым удобным вариантом."),
            ],

            process_kicker="Как проходит",
            process_title="Лечение с [[седацией]] — по шагам.",
            process_lead="Точную подготовку назначает ваша клиника; ниже — общий порядок.",
            process=[
                ("Консультация и осмотр", "Стоматолог составляет план лечения, анестезиолог расспрашивает о здоровье и лекарствах и при необходимости назначает анализы."),
                ("Подготовка", "Обычно перед седацией или наркозом нельзя есть и пить несколько часов — точное время скажет клиника. Возьмите с собой сопровождающего."),
                ("Лечение", "Анестезиолог вводит препарат и всё время следит за дыханием, пульсом и давлением, а стоматолог спокойно работает."),
                ("Восстановление", "Вы отдыхаете в клинике, пока действие препарата не пройдёт, и уходите домой с сопровождающим. В этот день нельзя садиться за руль."),
            ],

            safety_kicker="Выбор клиники",
            safety_title="Что спросить у клиники перед лечением с [[седацией]].",
            safety_lead="Хорошая клиника спокойно ответит на все эти вопросы ещё до записи.",
            checks=[
                "Кто проводит седацию или наркоз — анестезиолог?",
                "Есть ли у клиники лицензия на этот вид помощи?",
                "Как следят за состоянием во время лечения: есть ли монитор и кислород?",
                "Какие анализы и обследования нужны заранее?",
                "Как подготовиться и сколько длится восстановление?",
                "Кто будет лечить и что пишут о враче в отзывах?",
            ],

            faq_title="Частые вопросы о [[седации]].",
            medical_note="Информация на странице носит справочный характер и не заменяет консультацию врача.",
            faq=[
                ("Это безопасно?", "Седация и наркоз в стоматологии — обычная практика, когда их проводит анестезиолог после осмотра и с контролем состояния пациента. Поэтому так важно заранее спросить клинику, кто и как их проводит."),
                ("Будет больно?", "Нет. Зону лечения всё равно обезболивают, а с седацией или под наркозом вы ещё и не испытываете страха и напряжения."),
                ("Чем седация отличается от наркоза?", "При седации вы дремлете, дышите сами и можете отвечать врачу. При общем наркозе вы полностью спите. Какой вариант подходит, решают врач и анестезиолог."),
                ("Можно ли лечить детей под наркозом?", "Да, в детской стоматологии лечение под наркозом распространено, особенно если лечить нужно много зубов. Решение принимают после осмотра ребёнка."),
                ("Сколько длится лечение?", "Зависит от объёма: от часа до нескольких часов за визит. Плюс время на восстановление в клинике."),
                ("Можно ли сразу вернуться к делам?", "Домой лучше ехать с сопровождающим, а за руль в этот день садиться нельзя. Об остальных ограничениях расскажет клиника."),
            ],

            find_kicker="Найти клинику",
            find_title_html="Выберите клинику в каталоге Dental Navigator.",
            find_text="В каталоге — стоматологии Ташкента: адреса, врачи, услуги и отзывы; записаться можно онлайн. Перед записью уточните у клиники, проводит ли она лечение с [[седацией]] или под наркозом.",
        ),
    ),
    clinics=dict(uz=dict(
        direction_name="Tishlarni sedatsiya (narkoz) bilan davolash",
        breadcrumb_nav_label="Sahifa yo‘li",
        patients_link_label="Bemorlaringiz uchun sahifa",
        page_title="Sedatsiya (narkoz) bilan tish davolash — Toshkent klinikalari uchun",
        description="Toshkentda tishlarni sedatsiya yoki narkoz bilan davolaysizmi? Xizmat va shifokorlarni Dental Navigator katalogida ko‘rsating — bemorlar onlayn yoziladi.",
        og_description="Tishlarni sedatsiya va narkoz bilan davolaydigan klinikalar uchun: katalogdagi xizmat, shifokorlar va onlayn yozilish.",
        ld_topic="Tishlarni sedatsiya (narkoz) bilan davolash",
        ld_audience="Tishlarni sedatsiya va narkoz bilan davolaydigan stomatologiya klinikalari",
        og_image_alt="Toshkentda tishlarni sedatsiya (narkoz) bilan davolash — klinikalar uchun Dental Navigator",
        og_lines=[("Tishlarni", False), ("sedatsiya (narkoz)", True), ("bilan davolash.", False)],
        og_sub=["Klinikalar uchun: xizmat katalogda", "Shifokorlar · Onlayn yozilish"],

        hero_eyebrow="Sedatsiya va narkoz bilan davolaydigan stomatologiyalar uchun",
        hero_title_html='Toshkentda tishlarni <span class="accent-word">sedatsiya (narkoz)</span> bilan davolash — bemorlarga ko‘rsating.',
        hero_lead="Stomatologdan qo‘rqadigan odam shunchaki klinika emas, [[sedatsiya]] yoki [[narkoz]] bilan davolaydigan joyni qidiradi. Dental Navigator bu xizmatni klinikangiz sahifasida shifokorlar va sharhlar bilan ko‘rsatadi — bemor esa darhol onlayn yoziladi.",
        hero_chips=[
            ("tooth", "Katalogda sedatsiya xizmati"),
            ("user", "Klinika shifokorlari"),
            ("calendar", "Onlayn yozilish"),
        ],

        audience_title="[[Sedatsiya]] va [[narkoz]] bilan davolaydigan klinikalar uchun.",
        audience_lead="Anesteziologingiz shtatda bo‘ladimi yoki grafik bo‘yicha keladimi — xizmatni bemorlarga ko‘rsatish bir xil.",
        audience=[
            ("tooth", "Anesteziologi bor klinika", "Sedatsiya va umumiy narkoz",
             "Bir tashrifda bir nechta tishni davolaysiz, aql tishlarini olasiz, implantni uyqu holatida qo‘yasiz — bemor buni qabulxonada emas, oldindan bilishi kerak."),
            ("user", "Bolalar stomatologiyasi", "Qo‘rqadigan bolalar",
             "Ota-onalar bolani xotirjam va bir martada davolaydigan joyni qidiradi. Ularga shifokor, sharhlar va uzoq qo‘ng‘iroqlarsiz yozilish imkoni kerak."),
            ("grid", "Klinikalar tarmog‘i", "Hamma filialda emas",
             "Bemor sedatsiya bilan aynan qaysi filialda davolashini ko‘radi va eng yaqiniga emas, o‘sha filialga yoziladi."),
        ],

        pains_title="[[Sedatsiya]] kerak bo‘lgan bemor nega klinikangizga yetib kelmaydi.",
        pains_lead="Xizmat bor, talab bor — lekin yozuvlar bo‘lishi mumkin bo‘lganidan kam.",
        pains=[
            ("chat", "Sedatsiya haqida faqat qabulxona biladi", "Xizmat bor, lekin Instagram’da aksiyalar orasida yo‘qolib ketadi. Narkoz bilan davolatmoqchi bo‘lgan bemor siz haqingizda shunchaki bilmaydi."),
            ("phone", "Telefonda bir xil savollar", "“Bu narkozmi yoki sedatsiyami?”, “Qancha davom etadi?”, “Bolaga mumkinmi?” Administrator bularga kuniga o‘nlab marta javob beradi, bemor esa baribir ikkilanadi."),
            ("doc", "Xizmat tushunarsiz yozilgan", "Bemor sizda sedatsiyami yoki narkozmi, uni kim o‘tkazadi va davolash qancha davom etishini tushunmaydi — va qo‘ng‘iroqni orqaga suradi."),
            ("clock", "Qo‘rquv davolashni kechiktiradi", "Qo‘rqadigan bemor o‘tkir og‘riq boshlanguncha kutadi, keyin esa sedatsiya bilan davolashini birinchi bo‘lib aytgan klinikaga boradi."),
            ("calendar", "Kelmagan bemor — yarim kun bo‘sh kreslo", "Sedatsiya bilan davolash kreslo, shifokor va anesteziologni bir necha soatga band qiladi. Yozuv yo‘qolsa yoki bemor kelmasa, bitta oyna emas, yarim kun bo‘sh qoladi."),
            ("user", "Bemor kim davolashini bilmaydi", "Qo‘rqadigan odam uchun shifokorni oldindan ko‘rish muhim. Shifokor sahifasi va sharhlar bo‘lmasa, qaror orqaga suriladi."),
        ],
        pains_cta_text="Tanish holatmi? Klinikangizni qo‘shing va xizmatlarda sedatsiya bilan davolashni ko‘rsating — yoki raqamingizni qoldiring, qo‘ng‘iroq qilib, qanday ko‘rinishini ko‘rsatamiz.",

        platform_title="Dental Navigator [[sedatsiya]] bilan davolashni qanday ko‘rsatadi.",
        platform_lead="Bemor xizmat, shifokorlar va sharhlarni qo‘ng‘iroqdan oldin ko‘radi — va o‘zi yoziladi.",
        features=[
            ("pin", "Klinika sahifasidagi xizmat", "Sedatsiya yoki narkoz bilan davolash klinika xizmatlariga qo‘shiladi. Bemor uni dentalnavigator.uz katalogidagi klinika sahifasida, manzil va ish vaqti yonida ko‘radi.",  # TASDIQLANG: sedatsiyani klinika xizmati sifatida qo‘shsa bo‘ladimi (katalogdagi 12 yo‘nalish orasida sedatsiya yo‘q)
             "Bemor to‘g‘ri joyga kelganini tushunadi.", ["Xizmatlar", "Katalog", "Xarita"]),
            ("user", "Klinika shifokorlari", "Klinika sahifasida shifokorlar va ularning yo‘nalishlari. Qo‘rqadigan odam kim davolashini oldindan bilsa, xotirjamroq bo‘ladi.",
             "Ishonch birinchi tashrifdan oldin paydo bo‘ladi.", ["Shifokorlar", "Yo‘nalishlar", "Tajriba"]),
            ("calendar", "Konsultatsiyaga onlayn yozilish", "Sedatsiya bilan davolash odatda konsultatsiyadan boshlanadi. Bemor kun va vaqtni tanlab, telefon raqami bilan yoziladi — yozuv darhol kabinet kalendarida.",
             "Birorta ariza yozishmalarda yo‘qolmaydi.", ["Onlayn yozilish", "Kalendar", "Navbat"]),
            ("star", "Bemorlar sharhlari", "Boshqa bemorlarning sharhlari katalogda ko‘rinadi. Davolanishdan qo‘rqadigan odam uchun ular har qanday reklamadan kuchliroq.",  # TASDIQLANG: sharhlar prod’da ochiqmi
             "Obro‘ingiz yangi bemorlar uchun ishlaydi.", ["Sharhlar", "Murojaatlar", "Hisobotlar"]),
        ],
        modules_label="Bemor klinika sahifasida nimani ko‘radi",
        modules=["Manzil va xarita", "Ish vaqti", "Shifokorlar", "Xizmatlar", "Sharhlar", "Onlayn yozilish"],

        steps_title="[[Sedatsiya]] bilan davolashni bemorlarga to‘rt qadamda ko‘rsatamiz.",
        steps=[
            L["uz"]["steps"][0],
            L["uz"]["steps"][1],
            ("Kabinet ochiladi", "Shifokorlar, ish grafigi va xizmatlarni kiritasiz — sedatsiya bilan davolashni ham."),
            L["uz"]["steps"][3],
        ],

        faq_title="Klinikalarning [[sedatsiya]] bilan davolash haqidagi savollari.",
        faq=[
            ("Sedatsiya bilan davolashni katalogda ko‘rsatish pullikmi?", "Katalogdagi klinika sahifasi, xizmatlar va onlayn yozuvlar — bepul, yozilgan bemor uchun komissiya olinmaydi. Pullik tarif faqat davolashni ham tizimda yuritmoqchi bo‘lganlarga kerak — shartlarini qo‘ng‘iroqda aytamiz."),  # TASDIQLANG
            ("Katalogda alohida “sedatsiya” yo‘nalishi bormi?", "Sedatsiya va narkoz bilan davolash klinika xizmatlarida ko‘rsatiladi — bemor uni klinika sahifasida ko‘radi. Katalogda qanday xizmat va yo‘nalishlar borligini qo‘ng‘iroqda ko‘rsatamiz."),  # TASDIQLANG: xizmat sifatida qo‘shish
            ("Sedatsiya va narkoz — bir narsami?", "Yo‘q. Sedatsiyada bemor bo‘shashgan va mudroq holatda bo‘ladi, umumiy narkozda esa to‘liq uxlaydi. Xizmatda aynan nimani qilishingizni yozing: bemor birinchi bo‘lib shuni so‘raydi."),
            ("Bolalarni narkoz bilan davolashni ko‘rsatsa bo‘ladimi?", "Ha — alohida xizmat sifatida. Ota-onalar aynan shuni qidiradi va ularga shifokor hamda sharhlarni qo‘ng‘iroqdan oldin ko‘rish muhim."),
            L["uz"]["faq"][1],
            L["uz"]["faq"][5],
        ],

        contact_title_html="[[Sedatsiya]] bilan davolashni uni qidirayotganlarga ko‘rsating.",
        order_intro="Raqamingizni qoldiring — qo‘ng‘iroq qilib, sedatsiya bilan davolash klinikangiz sahifasida qanday ko‘rinishini ko‘rsatamiz.",
        order_info_example="Masalan: “Smile Dent” stomatologiyasi, Yunusobod, sedatsiya bilan davolaymiz, o‘z anesteziologimiz bor.",
        order_message_title="“Sedatsiya bilan davolash” sahifasi — qo‘ng‘iroq so‘rovi",
    ),
    ru=dict(
        direction_name="Лечение зубов с седацией (наркозом)",
        breadcrumb_nav_label="Навигационная цепочка",
        patients_link_label="Страница для ваших пациентов",
        page_title="Лечение зубов с седацией (наркозом) в Ташкенте — для клиник",
        description="Лечите зубы с седацией или под наркозом в Ташкенте? Покажите услугу и врачей в каталоге Dental Navigator — пациенты запишутся онлайн.",
        og_description="Для клиник, где лечат зубы с седацией и под наркозом: услуга в каталоге, врачи и онлайн-запись.",
        ld_topic="Лечение зубов с седацией (наркозом)",
        ld_audience="Стоматологические клиники, где лечат зубы с седацией и под наркозом",
        og_image_alt="Лечение зубов с седацией (наркозом) в Ташкенте — Dental Navigator для клиник",
        og_lines=[("Лечение зубов", False), ("с седацией (наркозом)", True), ("в Ташкенте.", False)],
        og_sub=["Для клиник: услуга в каталоге", "Врачи · Онлайн-запись"],

        hero_eyebrow="Для стоматологий, где лечат с седацией и под наркозом",
        hero_title_html='Лечение зубов с <span class="accent-word">седацией (наркозом)</span> в Ташкенте — покажите его пациентам.',
        hero_lead="Кто боится стоматолога, ищет не просто клинику, а место, где лечат с [[седацией]] или под [[наркозом]]. Dental Navigator показывает эту услугу на странице вашей клиники — с врачами и отзывами, — а пациент сразу записывается онлайн.",
        hero_chips=[
            ("tooth", "Услуга с седацией в каталоге"),
            ("user", "Врачи клиники"),
            ("calendar", "Онлайн-запись"),
        ],

        audience_title="Для клиник, где лечат с [[седацией]] и под [[наркозом]].",
        audience_lead="Анестезиолог у вас в штате или приходит по графику — показать услугу пациентам можно одинаково.",
        audience=[
            ("tooth", "Клиника с анестезиологом", "Седация и общий наркоз",
             "Лечите несколько зубов за визит, удаляете зубы мудрости, ставите импланты во сне — пациенту важно узнать об этом заранее, а не на ресепшене."),
            ("user", "Детская стоматология", "Дети, которые боятся",
             "Родители ищут, где ребёнка вылечат спокойно и за один раз. Им нужны врач, отзывы и возможность записаться без долгих звонков."),
            ("grid", "Сеть клиник", "Не во всех филиалах",
             "Пациент видит, в каком именно филиале лечат с седацией, и записывается туда, а не в ближайший."),
        ],

        pains_title="Почему пациент, которому нужна [[седация]], не доходит до вашей клиники.",
        pains_lead="Услуга есть, спрос есть — а записей меньше, чем могло бы быть.",
        pains=[
            ("chat", "О седации знает только ресепшен", "Услуга есть, но в Instagram она теряется среди акций. Пациент, который ищет лечение под наркозом, о вас просто не узнаёт."),
            ("phone", "Одни и те же вопросы по телефону", "«Это наркоз или седация?», «Сколько это длится?», «Можно ли ребёнку?» Администратор отвечает на них десятки раз в день, а пациент всё равно сомневается."),
            ("doc", "Услуга описана непонятно", "Пациент не понимает, седация у вас или наркоз, кто её проводит и сколько длится лечение, — и откладывает звонок."),
            ("clock", "Страх откладывает лечение", "Боящийся пациент тянет до острой боли, а потом идёт в клинику, которая первой сказала, что лечит с седацией."),
            ("calendar", "Неявка — полдня пустого кресла", "Лечение с седацией занимает кресло, врача и анестезиолога на несколько часов. Если запись потерялась или пациент не пришёл, пустует не окно, а полдня."),
            ("user", "Пациент не знает, кто будет лечить", "Тому, кто боится, важно заранее увидеть врача. Без страницы врача и отзывов решение откладывается."),
        ],
        pains_cta_text="Знакомо? Добавьте клинику и укажите лечение с седацией в услугах — или оставьте номер: позвоним и покажем, как это будет выглядеть.",

        platform_title="Как Dental Navigator показывает лечение с [[седацией]].",
        platform_lead="Пациент видит услугу, врачей и отзывы до звонка — и записывается сам.",
        features=[
            ("pin", "Услуга на странице клиники", "Лечение с седацией или под наркозом добавляется в услуги клиники. Пациент видит его на странице клиники в каталоге dentalnavigator.uz — рядом с адресом и режимом работы.",  # TASDIQLANG
             "Пациент понимает, что пришёл по адресу.", ["Услуги", "Каталог", "Карта"]),
            ("user", "Врачи клиники", "На странице клиники — врачи и их направления. Тому, кто боится, спокойнее, когда он заранее знает, кто будет лечить.",
             "Доверие появляется до первого визита.", ["Врачи", "Направления", "Опыт"]),
            ("calendar", "Онлайн-запись на консультацию", "Лечение с седацией обычно начинается с консультации. Пациент выбирает день и время и записывается по номеру телефона — запись сразу в календаре кабинета.",
             "Ни одна заявка не теряется в переписке.", ["Онлайн-запись", "Календарь", "Лист ожидания"]),
            ("star", "Отзывы пациентов", "Отзывы других пациентов видны в каталоге. Для того, кто боится лечения, они весомее любой рекламы.",  # TASDIQLANG
             "Репутация работает на новых пациентов.", ["Отзывы", "Обращения", "Отчёты"]),
        ],
        modules_label="Что пациент видит на странице клиники",
        modules=["Адрес и карта", "Режим работы", "Врачи", "Услуги", "Отзывы", "Онлайн-запись"],

        steps_title="Показываем лечение с [[седацией]] пациентам за четыре шага.",
        steps=[
            L["ru"]["steps"][0],
            L["ru"]["steps"][1],
            ("Открывается кабинет", "Вносите врачей, расписание и услуги — в том числе лечение с седацией."),
            L["ru"]["steps"][3],
        ],

        faq_title="Вопросы клиник о лечении с [[седацией]].",
        faq=[
            ("Показать лечение с седацией в каталоге — платно?", "Страница клиники в каталоге, услуги и онлайн-записи — бесплатно, комиссия за записавшегося пациента не берётся. Платный тариф нужен только тем, кто хочет вести в системе и само лечение, — условия расскажем на звонке."),  # TASDIQLANG
            ("Есть ли в каталоге отдельное направление «седация»?", "Лечение с седацией и под наркозом указывается в услугах клиники — так пациент видит его на странице клиники. Какие услуги и направления есть в каталоге, покажем на звонке."),  # TASDIQLANG
            ("Седация и наркоз — это одно и то же?", "Нет. При седации пациент расслаблен и дремлет, при общем наркозе — полностью спит. Укажите в услуге, что именно вы проводите: это первый вопрос пациента."),
            ("Можно показать лечение детей под наркозом?", "Да — отдельной услугой. Родители ищут именно это, и им важно видеть врача и отзывы до звонка."),
            L["ru"]["faq"][1],
            L["ru"]["faq"][5],
        ],

        contact_title_html="Покажите лечение с [[седацией]] тем, кто его ищет.",
        order_intro="Оставьте номер — позвоним и покажем, как лечение с седацией будет выглядеть на странице вашей клиники.",
        order_info_example="Например: стоматология «Smile Dent», Юнусабад, лечим с седацией, свой анестезиолог.",
        order_message_title="Страница «Лечение с седацией» — запрос звонка",
    )),
)
