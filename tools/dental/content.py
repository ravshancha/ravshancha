# -*- coding: utf-8 -*-
# Copy of the dentistry page (ravshancha.uz/dental/) in Uzbek and Russian. Edit here, then run build_site.py.
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
    lead_endpoint="/api/lead.php",  # callback form: one endpoint for all three sites, it writes into the shared spreadsheet
    phone_display="+998 99 942 07 70",
    phone_e164="+998999420770",
    telegram="ravshanjon_ismoilov",
    whatsapp="998999420770",
    linkedin="https://www.linkedin.com/in/ravshancha",
    metrika_id="",  # Yandex Metrika counter id; empty = no analytics script is emitted
    show_tariffs=True,  # TASDIQLANG: tariflar amalda shundaymi va ochiq yozsa bo‘ladimi; False = bo‘lim va menyu bandi chiqmaydi
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
    footer_cv="Rezyume",
    footer_biz="Biznes uchun xizmatlar",

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
        ("Bu pullikmi?", "Katalogdagi sahifa, onlayn yozuvlar va grafik — bepul. Davolashni tizimda yuritish (bemor kartalari, tish formulasi, davolash rejalari, kassa, hisobotlar) — pullik tarifda: filial uchun oyiga 99 000 so‘m. Yozilgan bemor uchun komissiya olinmaydi."),  # TASDIQLANG: narx
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
        ("Это платно?", "Страница в каталоге, онлайн-записи и расписание — бесплатно. Ведение лечения в системе (карточки пациентов, зубная карта, планы лечения, касса, отчёты) — на платном тарифе: 99 000 сум за филиал в месяц. Комиссия за записавшегося пациента не берётся."),  # TASDIQLANG
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
