# -*- coding: utf-8 -*-
# Selling-site copy in Uzbek and Russian. Edit here, then run build_site.py to regenerate site/.
#
# TASDIQLANG — a promise or a fact that Ravshanjon has to confirm before the site goes live.
# Nothing here may be invented: no made-up clients, numbers or testimonials.

SETTINGS = dict(
    base_url="https://ravshancha.uz/business/",  # public address of this site, with a trailing slash
    assets="../assets/",  # logo marks, favicons, portrait and OG image are shared with the CV site: path from this site's root
    cv_url="https://ravshancha.uz/",
    cv_label="ravshancha.uz",
    person="Ravshanjon Ismoilov",
    phone_display="+998 99 942 07 70",
    phone_e164="+998999420770",
    telegram="ravshanjon_ismoilov",
    whatsapp="998999420770",
    linkedin="https://www.linkedin.com/in/ravshancha",
    metrika_id="",  # Yandex Metrika counter id; empty = no analytics script is emitted
)

# Order matters: the first language is served at the site root.
LANGS = dict(
    uz=dict(code="UZ", name="O‘zbek", flag="flag-uz", path="", og_locale="uz_UZ"),
    ru=dict(code="RU", name="Русский", flag="flag-ru", path="ru/", og_locale="ru_RU"),
)

# Employer documentation for the Open API case, per language.
OPENAPI_DOCS = dict(
    uz="https://www.ipotekabank.uz/upload/openapi/openapi_uz.html",
    ru="https://www.ipotekabank.uz/upload/openapi/openapi_ru.html",
)

L = {}

L["uz"] = dict(
    # Search snippets: the title is cut at about 60 characters, the description at about 160.
    page_title="Biznes jarayonlarini avtomatlashtirish, Toshkent — Ravshanjon Ismoilov",
    description="Excel va qo‘l mehnati o‘rniga — avtomatlashtirilgan jarayonlar, integratsiyalar va rahbar uchun dashboard. Toshkent. Bepul 30 daqiqalik diagnostika.",
    og_description="Jarayon auditi, avtomatlashtirish, integratsiya va rahbar uchun dashboard. Bepul 30 daqiqalik diagnostika.",
    ld_name="Ravshanjon Ismoilov — biznes jarayonlarini avtomatlashtirish",
    og_image_alt="Biznesingiz qo‘lda emas, tizimda ishlasin — Ravshanjon Ismoilov",
    og_lines=[("Biznesingiz", False), ("qo‘lda emas, tizimda", True), ("ishlasin.", False)],  # social preview headline: (text, accent)
    og_sub=["Jarayon auditi · Avtomatlashtirish", "Integratsiya · Dashboard", "Toshkent, O‘zbekiston"],
    footer_location="Toshkent, O‘zbekiston",

    skip_link="Kontentga o‘tish",
    nav_label="Asosiy navigatsiya",
    menu_label="Menyuni ochish",
    nav_pains="Muammolar",
    nav_services="Xizmatlar",
    nav_process="Jarayon",
    nav_proof="Tajriba",
    nav_faq="Savollar",
    phone_label="+998 99 942 07 70 raqamiga qo‘ng‘iroq qilish",
    theme_label="Rang rejimini almashtirish",
    theme_dark="Qorong‘i",
    theme_light="Yorug‘",
    language_label="Til",
    back_to_top="Yuqoriga",
    footer_links_label="Aloqa havolalari",
    footer_cv="Rezyume",

    hero_eyebrow="Biznes jarayonlarini avtomatlashtirish",
    hero_title_html='Biznesingiz<br><span class="accent-word">qo‘lda emas, tizimda</span><br>ishlasin.',
    hero_lead="Qo‘lda bajariladigan ishlar, Excel va yo‘qolgan buyurtmalar o‘rniga — avtomatlashtirilgan jarayonlar va rahbar uchun shaffof hisobot. Har bir buyurtma va har bir so‘m ko‘rinib turadi.",
    cta_primary="Bepul diagnostika",
    cta_telegram="Telegram’da yozish",
    hero_trust=[
        "30 daqiqa, majburiyatsiz",
        "10+ yil bank va fintech tizimlari",
        "NDA va shartnoma asosida",  # TASDIQLANG: yuridik shakl (YaTT/MChJ)
    ],
    portrait_alt="Ravshanjon Ismoilov portreti",
    hero_cards_label="Xizmat yo‘nalishlari",
    hero_cards=[
        ("search", "Audit", "Jarayon xaritasi · Reja"),
        ("bolt", "Avtomatlashtirish", "Ichki tizim · Bot"),
        ("link", "Integratsiya", "1C · CRM · Bank · To‘lov"),  # TASDIQLANG: qaysi tizimlar bilan ishlaysiz
        ("chart", "Shaffoflik", "Dashboard · Hisobot"),
    ],

    summary_kicker="● Kim uchun",
    summary_title_html='<span class="accent-word">O‘sayotgan</span> savdo, ishlab chiqarish va xizmat ko‘rsatish kompaniyalari uchun.',  # TASDIQLANG: segment
    summary_text="Jamoa kattalashgan, buyurtmalar ko‘paygan, lekin jarayonlari hali Excel, Telegram va daftarda yurgan bizneslar bilan ishlayman.",
    stats=[
        ("clock", "10+ yil", "Bank va fintech tajribasi"),
        ("chat", "30 daq", "Bepul diagnostika"),
        ("search", "1–2 hafta", "Jarayon auditi"),  # TASDIQLANG: audit muddati
    ],
    cv_title="Rezyume",
    cv_action="ravshancha.uz",
    cv_label="To‘liq rezyumeni ravshancha.uz saytida ochish",

    pains_kicker="Tanish holatlar",
    pains_title="Bu muammolardan qaysi biri sizda bor?",
    pains_lead="Biznes o‘sgani sari qo‘lda boshqarish qimmatga tusha boshlaydi. Eng ko‘p uchraydigan oltita belgi:",
    pains=[
        ("calendar", "Hisobot oy oxirida yig‘iladi", "Raqamlar Excel fayllarda sochilgan. Qaror qabul qilish kerak bo‘lganda ma’lumot hali tayyor emas — yoki allaqachon eskirgan."),
        ("box", "Ombor va dastur mos kelmaydi", "Qog‘ozda bir qoldiq, dasturda boshqa. Kamomad qayerda paydo bo‘lganini hech kim ko‘rsatib bera olmaydi."),
        ("chat", "Buyurtmalar yo‘qoladi", "Arizalar Telegram, telefon va daftarda. Kimdir javob berishni unutsa — mijoz raqobatchiga ketadi, siz esa bilmay qolasiz."),
        ("user", "Hammasi bitta xodimga bog‘liq", "Menejer yoki hisobchi ketsa, mijozlar bazasi va jarayon haqidagi bilim ham u bilan birga ketadi."),
        ("grid", "Tizimlar bir-biri bilan gaplashmaydi", "1C, CRM, bank-klient va Telegram alohida yashaydi. Xodimlar ma’lumotni qo‘lda ko‘chiradi — vaqt shu yerda yo‘qoladi, xato shu yerda paydo bo‘ladi."),
        ("wallet", "Pul qayerga ketayotgani ko‘rinmaydi", "Aylanma bor, foyda esa noaniq. Qaysi mahsulot, filial yoki menejer pul olib kelayotganini bir qarashda ko‘rib bo‘lmaydi."),
    ],
    pains_cta_text="O‘zingizni tanidingizmi? 30 daqiqada qayerdan boshlashni aniqlaymiz.",
    cta_long="Diagnostikaga yozilish",

    services_kicker="Xizmatlar",
    services_title="Muammoga qarab — to‘rt yo‘nalish.",
    services_lead="Hammasini birdan emas: eng ko‘p pul va vaqt yo‘qolayotgan joydan boshlaymiz.",
    result_label="Natija",
    services=[
        ("search", "Jarayon auditi", "Jarayonlaringizni boshidan oxirigacha o‘rganib, qayerda vaqt, pul va ma’lumot yo‘qolayotganini topaman.",
         "Muammolar xaritasi va ustuvorlik bo‘yicha reja.", ["Jarayon xaritasi", "Yo‘qotishlar ro‘yxati", "Yo‘l xaritasi"]),
        ("bolt", "Avtomatlashtirish", "Qo‘lda takrorlanadigan ishlarni tizimga o‘tkazaman: buyurtmalar, ombor, hujjat aylanishi, xodimlar vazifalari.",
         "Xodimlar vaqtini rutinaga emas, mijozga sarflaydi.", ["Ichki tizim", "Telegram-bot", "Hujjat aylanishi"]),
        ("link", "Integratsiya", "Alohida yashayotgan tizimlarni bog‘layman: hisob dasturi, CRM, bank, to‘lov tizimlari va sayt bitta ma’lumot bilan ishlaydi.",
         "Ma’lumot bir marta kiritiladi — hamma joyda to‘g‘ri.", ["API", "To‘lov tizimlari", "CRM · 1C"]),
        ("chart", "Shaffoflik: dashboard va hisobotlar", "Rahbar uchun real vaqtdagi panel: savdo, qoldiq, qarzdorlik, xodimlar natijasi — telefon yoki kompyuterdan.",
         "Hisobotni kutmaysiz — ochib ko‘rasiz.", ["Dashboard", "Avto-hisobot", "Telegram xabarnoma"]),
    ],
    services_note="Har bir ish hajm, muddat va narx yozma kelishilgandan keyin boshlanadi. Avval kichik, o‘lchanadigan bosqich — natijani ko‘rib, davom etish-etmaslikni o‘zingiz hal qilasiz.",

    process_kicker="Ish jarayoni",
    process_title="Birinchi suhbatdan ishlaydigan tizimgacha.",
    process_lead="Har bir bosqichda nima olishingiz oldindan ma’lum.",
    process=[  # TASDIQLANG: bosqichlar va muddatlar sizning real ish uslubingizga mos bo‘lsin
        ("Bepul suhbat — 30 daqiqa", "Muammoni tinglayman, savollar beraman. Yordam bera olmasam — ochiq aytaman."),
        ("Audit va reja", "Jarayonni joyida yoki onlayn o‘rganaman. Natija — muammolar xaritasi, ustuvor yechimlar, muddat va narx."),
        ("Bosqichma-bosqich joriy qilish", "Ishni kichik bosqichlarga bo‘laman. Har ikki haftada ishlaydigan natijani ko‘rasiz va fikr bildirasiz."),
        ("Xodimlarni o‘rgatish", "Tizim faqat undan foydalanilsagina ishlaydi. Yo‘riqnoma va jonli o‘rgatish — ishning bir qismi."),
        ("Qo‘llab-quvvatlash", "Ishga tushgandan keyin ham yoningizdaman: monitoring, tuzatishlar va rivojlantirish."),
    ],

    proof_kicker="Nega men",
    proof_title="Bank tizimlarini qurgan tajriba — endi sizning biznesingiz uchun.",
    proof_p1="10 yildan ortiq vaqt davomida xato qimmatga tushadigan tizimlarni qurganman: mobil va internet-banking, to‘lov tizimlari, davlat xizmatlari bilan integratsiyalar. Ipotekabank OTP Group va REALSOFT’da dasturchilar guruhiga rahbarlik qilganman.",
    proof_p2="Shu intizomni — xavfsizlik, ishonchlilik, aniq muddat — kichik va o‘rta biznes jarayonlariga olib kelaman. Chiroyli taqdimot emas, har kuni ishlaydigan tizim.",
    facts=[
        ("link", "Integratsiyalar", "Uzcard · Humo · Paynet · Wolt · davlat xizmatlari"),
        ("team", "Jamoa boshqaruvi", "6 kishigacha bo‘lgan dasturchilar guruhlari"),
        ("doc", "Avtomatlashtirish", "Hisob modullari va bank hujjat aylanish tizimi"),
        ("check", "Sertifikat", "IBM Business Automation Workflow (2021)"),
    ],
    proof_cv_link="To‘liq ish tajribasi va rezyume — ravshancha.uz",

    cases_kicker="Tajribadan misollar",
    cases_title="Men qurgan tizimlardan uchtasi.",
    cases_lead="Bular — men ishlagan kompaniyalardagi loyihalar va ulardagi rolim.",
    case_task="Vazifa",
    case_solution="Yechim",
    case_result="Natija",
    case_docs="Hujjatlar",
    cases=[  # TASDIQLANG: har bir keysdagi fakt va natijani tekshiring; SMB keyslari paydo bo‘lgach shularni almashtiring
        dict(type="Fintech · To‘lov platformasi", name="RealPay", role="REALSOFT · Dasturchilar guruhi rahbari",
             task="Davlat loyihalari uchun yagona ichki to‘lov tizimi kerak edi.",
             solution="6 kishilik jamoa bilan RealPay tizimini ishga tushirdik, Uzcard va Humo’ni integratsiya qildik.",
             result="10 dan ortiq davlat loyihasi bitta to‘lov platformasiga ulandi."),
        dict(type="Bank · Korporativ mijozlar uchun Open API", name="Ipoteka Bank Open API", role="Ipotekabank OTP Group · Dasturchilar guruhi rahbari", docs=True,
             task="Korxonalar bank operatsiyalarini bank-klientga kirmasdan, o‘z hisob tizimidan bajarishni xohlaydi.",
             solution="Bank servislarini ochadigan xavfsiz REST API: hisobvaraq ko‘chirmasi, to‘lovlar va ularning holati, ish haqi loyihalari, valyuta kurslari.",
             result="Korxona tizimi bank bilan to‘g‘ridan-to‘g‘ri ishlaydi — ma’lumotni qo‘lda ko‘chirish shart emas."),
        dict(type="Bank · Hujjat aylanishi", name="Hujjat aylanish tizimi", role="MIRONSOFT · Java dasturchi",
             task="Bank ichidagi hujjat aylanishi va hisob ishlarini tizimga o‘tkazish.",
             solution="UzAgroExpertBank uchun hujjat aylanish tizimini, Ijod Fondi uchun hisob va avtomatlashtirish modullarini ishlab chiqdim va qo‘llab-quvvatladim.",
             result="Qog‘oz va qo‘lda yuritish o‘rniga — har bir hujjatning yo‘li ko‘rinadigan tizim."),
    ],

    faq_kicker="Savollar",
    faq_title="Ko‘p beriladigan savollar.",
    faq=[
        ("Narxi qancha?", "Narx ish hajmiga bog‘liq, shuning uchun avval bepul suhbat va audit. Auditdan keyin hajm, muddat va narxni yozma ko‘rinishda olasiz — kutilmagan qo‘shimcha to‘lovlarsiz."),  # TASDIQLANG: narx siyosati
        ("Qancha vaqt oladi?", "Audit — 1–2 hafta. Birinchi ishlaydigan natija odatda 2–6 hafta ichida chiqadi; katta tizimlar bosqichlarga bo‘linadi."),  # TASDIQLANG: muddatlar
        ("Bizda allaqachon 1C yoki CRM bor. Hammasini almashtirish kerakmi?", "Yo‘q. Ko‘pincha mavjud tizimlarni almashtirish emas, ularni o‘zaro bog‘lash va ustiga hisobot qurish kifoya."),
        ("Ma’lumotlarimiz xavfsizligi-chi?", "Bank tizimlaridan keyin xavfsizlik men uchun odat: NDA imzolaymiz, kirish huquqlari minimal bo‘ladi, ma’lumotlar o‘z serveringizda yoki siz tanlagan bulutda qoladi."),
        ("Xodimlar yangi tizimga qarshilik qilsa-chi?", "Bu eng ko‘p uchraydigan xavf. Shuning uchun tizimni xodimlar bilan birga loyihalayman, ularning ishini og‘irlashtirmaydigan qilib quraman va o‘rgataman."),
        ("Shartnoma bilan ishlaysizmi?", "Ha, shartnoma asosida — bosqichlar va to‘lov jadvali bilan."),  # TASDIQLANG: yuridik shakl, hisob-faktura
    ],

    contact_kicker="Aloqa",
    contact_title_html="Muammoni 30 daqiqada<br>muhokama qilamiz — bepul.",
    contact_text="Yordam bera olmasam, ochiq aytaman va kimga murojaat qilishni maslahat beraman.",

    order_title="Bepul diagnostikaga yozilish",
    order_intro="Raqamingizni qoldiring — imkon qadar tez bog‘lanib, qulay vaqtni kelishamiz.",
    order_name="Ismingiz",
    order_name_example="Masalan: Alisher Karimov",
    order_name_error="Ismingizni kiriting.",
    order_phone="Telefon raqamingiz",
    order_phone_example="Masalan: 99 942 07 70",
    order_phone_error="Faqat raqam, 9 ta belgi: 999420770.",
    order_info="Qaysi muammo bezovta qilyapti? (ixtiyoriy)",
    order_info_example="Masalan: ulgurji savdo, 25 xodim. Ombor qoldig‘i dastur bilan mos kelmaydi, hisobot Excel’da yig‘iladi.",
    order_submit="Yuborish",
    order_sending="Yuborilmoqda…",
    order_cancel="Bekor qilish",
    order_consent="Yuborish orqali ma’lumotlaringizdan siz bilan bog‘lanish uchun foydalanishimga rozilik bildirasiz.",
    order_success_title="Arizangiz qabul qilindi",
    order_success_text="Rahmat! Imkon qadar tez bog‘lanaman.",
    order_close="Yopish",
    order_fallback_text="Arizani avtomatik yuborib bo‘lmadi. Uni Telegram orqali yuboring — matn tayyor:",
    order_fallback_button="Telegram’da yuborish",
    order_fallback_note="Matn nusxalandi. Telegram’da xabar bo‘sh chiqsa — uni qo‘yib, yuboring.",
    order_message_title="Diagnostikaga ariza",
    order_message_info="Muammo",

    sticky_label="Tezkor aloqa",
    sticky_call="Qo‘ng‘iroq",
)

L["ru"] = dict(
    page_title="Автоматизация бизнес-процессов в Ташкенте — Равшанжон Исмоилов",
    description="Вместо Excel и ручной работы — автоматизированные процессы, интеграции и дашборд для руководителя. Ташкент. Бесплатная диагностика за 30 минут.",
    og_description="Аудит процессов, автоматизация, интеграции и дашборд для руководителя. Бесплатная 30-минутная диагностика.",
    ld_name="Равшанжон Исмоилов — автоматизация бизнес-процессов",
    og_image_alt="Пусть бизнес работает в системе, а не вручную — Равшанжон Исмоилов",
    og_lines=[("Пусть бизнес работает", False), ("в системе,", True), ("а не вручную.", True)],
    og_sub=["Аудит процессов · Автоматизация", "Интеграции · Дашборд", "Ташкент, Узбекистан"],
    footer_location="Ташкент, Узбекистан",

    skip_link="Перейти к содержимому",
    nav_label="Основная навигация",
    menu_label="Открыть меню",
    nav_pains="Проблемы",
    nav_services="Услуги",
    nav_process="Процесс",
    nav_proof="Опыт",
    nav_faq="Вопросы",
    phone_label="Позвонить по номеру +998 99 942 07 70",
    theme_label="Переключить цветовую тему",
    theme_dark="Тёмная",
    theme_light="Светлая",
    language_label="Язык",
    back_to_top="Наверх",
    footer_links_label="Контакты",
    footer_cv="Резюме",

    hero_eyebrow="Автоматизация бизнес-процессов",
    hero_title_html='Пусть бизнес работает<br><span class="accent-word">в системе, а не вручную</span>.',
    hero_lead="Вместо ручной работы, Excel и потерянных заказов — автоматизированные процессы и прозрачная отчётность для руководителя. Виден каждый заказ и каждый сум.",
    cta_primary="Бесплатная диагностика",
    cta_telegram="Написать в Telegram",
    hero_trust=[
        "30 минут, без обязательств",
        "10+ лет в банковских и финтех-системах",
        "Работаю по NDA и договору",
    ],
    portrait_alt="Портрет Равшанжона Исмоилова",
    hero_cards_label="Направления работы",
    hero_cards=[
        ("search", "Аудит", "Карта процессов · План"),
        ("bolt", "Автоматизация", "Внутренняя система · Бот"),
        ("link", "Интеграции", "1С · CRM · Банк · Платежи"),
        ("chart", "Прозрачность", "Дашборд · Отчёты"),
    ],

    summary_kicker="● Для кого",
    summary_title_html='Для <span class="accent-word">растущих</span> компаний в торговле, производстве и услугах.',
    summary_text="Работаю с бизнесами, где команда и поток заказов выросли, а процессы всё ещё живут в Excel, Telegram и блокноте.",
    stats=[
        ("clock", "10+ лет", "Банки и финтех"),
        ("chat", "30 мин", "Бесплатная диагностика"),
        ("search", "1–2 недели", "Аудит процессов"),
    ],
    cv_title="Резюме",
    cv_action="ravshancha.uz",
    cv_label="Открыть полное резюме на сайте ravshancha.uz",

    pains_kicker="Знакомые ситуации",
    pains_title="Какая из этих проблем есть у вас?",
    pains_lead="Чем больше бизнес, тем дороже обходится ручное управление. Шесть самых частых признаков:",
    pains=[
        ("calendar", "Отчёт собирается в конце месяца", "Цифры разбросаны по Excel-файлам. Когда нужно принять решение, данные ещё не готовы — или уже устарели."),
        ("box", "Склад не сходится с программой", "На бумаге один остаток, в программе другой. Где появилась недостача — никто показать не может."),
        ("chat", "Заявки теряются", "Заказы приходят в Telegram, по телефону и в блокнот. Кто-то забыл ответить — клиент ушёл к конкуренту, а вы об этом не узнали."),
        ("user", "Всё держится на одном сотруднике", "Уйдёт менеджер или бухгалтер — вместе с ним уйдут клиентская база и знание процесса."),
        ("grid", "Системы не общаются между собой", "1С, CRM, банк-клиент и Telegram живут отдельно. Сотрудники переносят данные вручную — здесь теряется время и появляются ошибки."),
        ("wallet", "Не видно, куда уходят деньги", "Оборот есть, а прибыль непонятна. Какой товар, филиал или менеджер приносит деньги — одним взглядом не увидеть."),
    ],
    pains_cta_text="Узнали себя? За 30 минут определим, с чего начать.",
    cta_long="Записаться на диагностику",

    services_kicker="Услуги",
    services_title="Четыре направления — под вашу задачу.",
    services_lead="Не всё сразу: начинаем там, где теряется больше всего денег и времени.",
    result_label="Результат",
    services=[
        ("search", "Аудит процессов", "Прохожу ваши процессы от начала до конца и нахожу, где теряются время, деньги и данные.",
         "Карта проблем и план по приоритетам.", ["Карта процессов", "Список потерь", "Дорожная карта"]),
        ("bolt", "Автоматизация", "Перевожу повторяющуюся ручную работу в систему: заказы, склад, документооборот, задачи сотрудников.",
         "Сотрудники тратят время на клиента, а не на рутину.", ["Внутренняя система", "Telegram-бот", "Документооборот"]),
        ("link", "Интеграции", "Связываю системы, которые живут отдельно: учётная программа, CRM, банк, платёжные системы и сайт работают с одними данными.",
         "Данные вводятся один раз — и верны везде.", ["API", "Платёжные системы", "CRM · 1С"]),
        ("chart", "Прозрачность: дашборд и отчёты", "Панель руководителя в реальном времени: продажи, остатки, дебиторка, результаты сотрудников — с телефона или компьютера.",
         "Отчёт не ждут — его открывают.", ["Дашборд", "Автоотчёты", "Уведомления в Telegram"]),
    ],
    services_note="Любая работа начинается после письменного согласования объёма, сроков и стоимости. Сначала небольшой измеримый этап — вы видите результат и сами решаете, идти ли дальше.",

    process_kicker="Как я работаю",
    process_title="От первого разговора до работающей системы.",
    process_lead="На каждом этапе заранее известно, что вы получите.",
    process=[
        ("Бесплатный разговор — 30 минут", "Слушаю задачу и задаю вопросы. Если помочь не смогу — скажу прямо."),
        ("Аудит и план", "Изучаю процесс на месте или онлайн. На выходе — карта проблем, приоритетные решения, сроки и стоимость."),
        ("Внедрение по этапам", "Делю работу на небольшие этапы. Каждые две недели вы видите работающий результат и даёте обратную связь."),
        ("Обучение сотрудников", "Система работает, только если ею пользуются. Инструкции и живое обучение — часть работы."),
        ("Поддержка", "После запуска остаюсь рядом: мониторинг, исправления и развитие."),
    ],

    proof_kicker="Почему я",
    proof_title="Опыт банковских систем — теперь для вашего бизнеса.",
    proof_p1="Больше 10 лет я строю системы, где ошибка стоит дорого: мобильный и интернет-банкинг, платёжные системы, интеграции с государственными сервисами. Руководил группами разработки в Ipotekabank OTP Group и REALSOFT.",
    proof_p2="Эту дисциплину — безопасность, надёжность, понятные сроки — я приношу в процессы малого и среднего бизнеса. Не красивая презентация, а система, которая работает каждый день.",
    facts=[
        ("link", "Интеграции", "Uzcard · Humo · Paynet · Wolt · госсервисы"),
        ("team", "Управление командой", "Группы разработки до 6 человек"),
        ("doc", "Автоматизация", "Учётные модули и банковский документооборот"),
        ("check", "Сертификат", "IBM Business Automation Workflow (2021)"),
    ],
    proof_cv_link="Полный опыт работы и резюме — ravshancha.uz",

    cases_kicker="Примеры из опыта",
    cases_title="Три системы, которые я строил.",
    cases_lead="Это проекты компаний, в которых я работал, и моя роль в них.",
    case_task="Задача",
    case_solution="Решение",
    case_result="Результат",
    case_docs="Документация",
    cases=[
        dict(type="Финтех · Платёжная платформа", name="RealPay", role="REALSOFT · руководитель группы разработки",
             task="Государственным проектам нужна была единая внутренняя платёжная система.",
             solution="С командой из 6 человек запустили RealPay и интегрировали Uzcard и Humo.",
             result="Более 10 государственных проектов подключены к одной платёжной платформе."),
        dict(type="Банк · Open API для корпоративных клиентов", name="Ipoteka Bank Open API", role="Ipotekabank OTP Group · руководитель группы разработки", docs=True,
             task="Компании хотят проводить банковские операции из своей учётной системы, не заходя в банк-клиент.",
             solution="Безопасный REST API к сервисам банка: выписки по счетам, платежи и их статусы, зарплатные проекты, курсы валют.",
             result="Система компании работает с банком напрямую — без ручного переноса данных."),
        dict(type="Банк · Документооборот", name="Система документооборота", role="MIRONSOFT · Java-разработчик",
             task="Перевести внутренний документооборот и учётные операции в систему.",
             solution="Разрабатывал и поддерживал систему документооборота для UzAgroExpertBank и модули учёта и автоматизации для Ijod Fondi.",
             result="Вместо бумаги и ручного ведения — система, где виден путь каждого документа."),
    ],

    faq_kicker="Вопросы",
    faq_title="Частые вопросы.",
    faq=[
        ("Сколько это стоит?", "Стоимость зависит от объёма, поэтому сначала бесплатный разговор и аудит. После аудита вы получаете объём, сроки и цену в письменном виде — без неожиданных доплат."),
        ("Сколько времени это займёт?", "Аудит — 1–2 недели. Первый работающий результат обычно появляется через 2–6 недель; большие системы делятся на этапы."),
        ("У нас уже есть 1С или CRM. Придётся всё менять?", "Нет. Чаще всего достаточно не менять существующие системы, а связать их между собой и построить отчётность поверх."),
        ("А безопасность наших данных?", "После банковских систем безопасность для меня — привычка: подписываем NDA, доступы минимальные, данные остаются на вашем сервере или в выбранном вами облаке."),
        ("Что если сотрудники будут сопротивляться новой системе?", "Это самый частый риск. Поэтому я проектирую систему вместе с сотрудниками, делаю так, чтобы она не усложняла им работу, и обучаю."),
        ("Вы работаете по договору?", "Да, по договору — с этапами и графиком оплаты."),
    ],

    contact_kicker="Контакты",
    contact_title_html="Обсудим вашу задачу<br>за 30 минут — бесплатно.",
    contact_text="Если помочь не смогу — скажу прямо и подскажу, к кому обратиться.",

    order_title="Запись на бесплатную диагностику",
    order_intro="Оставьте номер — свяжусь с вами в ближайшее время, и согласуем удобное время.",
    order_name="Ваше имя",
    order_name_example="Например: Алишер Каримов",
    order_name_error="Введите ваше имя.",
    order_phone="Номер телефона",
    order_phone_example="Например: 99 942 07 70",
    order_phone_error="Только цифры, 9 знаков: 999420770.",
    order_info="Какая проблема беспокоит? (необязательно)",
    order_info_example="Например: оптовая торговля, 25 сотрудников. Остатки на складе не сходятся с программой, отчёты собираем в Excel.",
    order_submit="Отправить",
    order_sending="Отправка…",
    order_cancel="Отмена",
    order_consent="Отправляя форму, вы соглашаетесь на использование ваших данных для связи с вами.",
    order_success_title="Заявка принята",
    order_success_text="Спасибо! Свяжусь с вами в ближайшее время.",
    order_close="Закрыть",
    order_fallback_text="Не удалось отправить заявку автоматически. Отправьте её через Telegram — текст уже готов:",
    order_fallback_button="Отправить в Telegram",
    order_fallback_note="Текст скопирован. Если сообщение в Telegram окажется пустым — вставьте его и отправьте.",
    order_message_title="Заявка на диагностику",
    order_message_info="Проблема",

    sticky_label="Быстрая связь",
    sticky_call="Позвонить",
)
