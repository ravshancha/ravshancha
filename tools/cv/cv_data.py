# -*- coding: utf-8 -*-
# CV content in three languages. Edit here, then run build_cv.py to regenerate site/cv/*.pdf.
NAME = "Ravshanjon Ismoilov"
CONTACT = {
    "phone": "+998 99 942 07 70", "email": "ismoilov.ravshanjon@gmail.com", "site": "ravshancha.uz",
    "tg": "t.me/ravshanjon_ismoilov", "li": "linkedin.com/in/ravshancha", "gh": "github.com/ravshancha",
}
CERTS = [
    ("2022", "LinkedIn Learning", "Spring: Spring Cloud · Microservices: Design Patterns · Microservices Foundations · Java Memory Management · Spring 5.0 and Spring Boot 2.0 New Features · Creating Your First Spring Boot Microservice · Spring Microservices"),
    ("2021", "QDTS", "IBM Business Automation Workflow V19.0.0.1"),
    ("2021", "SoloLearn", "Java, Kotlin, SQL, Python, HTML/CSS, JavaScript, jQuery, React + Redux, PHP"),
    ("2019", "PDP IT Academy", "Full Stack Web Development (Spring Boot)"),
    ("2015", "BePro IT Academy", "Java, Oracle, Windows Server, ITIL v3"),
]
T_IPOTEKA = "Java 21, Spring Boot 3.x, Spring Security, Spring Data JPA, RabbitMQ, PostgreSQL, Docker, Swagger 3.0 / OpenAPI, GitLab CI/CD"
T_REALSOFT = "Java 17, Spring Boot 2.7+, Spring Security, Spring Data JPA, REST API, PostgreSQL, Redis, RabbitMQ, GitLab CI/CD, Swagger"
T_EPAM = "Java 17, Spring Boot 2.x, REST API, RabbitMQ, GitLab CI, Docker, Kubernetes"
T_APELSIN = "Java 11, Spring Boot 2.x, Spring Security, Spring Data JPA, PostgreSQL, Redis, Swagger 2.0, Git"
T_MARKET = "Java 11, Spring Boot 2.x, Spring Cloud (Config, Discovery, Gateway, OpenFeign), PostgreSQL, Redis, Elasticsearch"
T_K24 = "Java 8, Spring Boot, Spring Security, Spring Data, Oracle, ActiveMQ, Swagger 2.0"
T_ORIENT = "Java 11, Spring Boot 2.x, Spring Cloud Gateway, PostgreSQL, MongoDB, Swagger 2.0"
T_DAVR = "Java 11, Spring Boot 2.x, Spring Security, Spring Data JPA, REST API, Oracle Database, Swagger 2.0, Git"
T_MIRON = "Java 8, Spring MVC, Spring Core, PostgreSQL, Git"

L = {}
L["uz"] = dict(
    title="Java Software Developer", updated="Sentyabr 2026", location="Toshkent, O‘zbekiston",
    labels=dict(summary="Qisqacha", exp="Ish tajribasi", edu="Ta’lim", certs="Kurslar va sertifikatlar", skills="Ko‘nikmalar", langs="Tillar", format="Ish formati", qualities="Shaxsiy fazilatlar", tech="Texnologiyalar", project="Loyiha"),
    summary="Bank va fintech sohasida 8 yildan ortiq tajribaga ega Java dasturchi: mobil va internet-banking, to‘lov tizimlari va integratsiyalar (Uzcard, Humo, Paynet, Wolt, davlat idoralari). 6 kishigacha bo‘lgan jamoalarga rahbarlik qilgan, arxitektura va xavfsiz REST API’larni loyihalagan, relizlar va kod-revyu uchun javob bergan. Asosiy stek: Java 21, Spring Boot 3, Spring Cloud, PostgreSQL, Oracle, RabbitMQ, Docker.",
    qualities="Muloqotga ochiq, tez o‘rganaman va yangi vazifalarga moslashaman; natijaga yo‘naltirilgan va mas’uliyatli; tashabbuskor, jamoada samarali ishlayman; doimiy professional o‘sishga intilaman.",
    workformat="To‘liq bandlik · ofis, masofaviy yoki gibrid · Toshkent",
    langs=["O‘zbek — ona tili", "Rus — C2", "Ingliz — B2", "Turk — B2"],
    edu=[("Toshkent axborot texnologiyalari universiteti", "Bakalavr — Kompyuter injiniringi (kompyuter tizimlari)", "2017")],
    skills=[("Backend", "Java 21, Spring Boot 3.x, Spring Security, OAuth2, Spring Data / JPA / JDBC, Hibernate"),
            ("Mikroservislar", "Spring Cloud (Config, Discovery, Gateway, OpenFeign, Routing), RabbitMQ, ActiveMQ"),
            ("API", "REST, SOAP, JSON, XML, Swagger / OpenAPI"),
            ("Ma’lumotlar bazalari", "Oracle, PostgreSQL, MySQL; NoSQL: Redis, MongoDB, Elasticsearch"),
            ("Serverlar va vositalar", "Apache Tomcat, NGINX, Docker, Kubernetes, Git / GitHub / GitLab CI/CD, Maven / Gradle"),
            ("Frontend (boshlang‘ich)", "React.js / Vue.js, HTML5, CSS3, JavaScript")],
    jobs=[
        dict(co="Ipotekabank OTP Group", role="Dasturchilar guruhi rahbari", period="2024-yil yanvar — 2025-yil dekabr", loc="Toshkent · Bank", blocks=[
            dict(head="Omnichannel bo‘limi", bullets=[
                "OpenAPI / DiBank — yuridik mijozlar integratsiyasi: yuridik shaxslar va korporativ mijozlar uchun REST API; kodni optimallashtirish, yangilangan xavfsizlik va tokenizatsiya arxitekturasini joriy etish; CRM va ichki bank servislari o‘rtasida integratsiya.",
                "Wolt integratsiyasi — xalqaro ovqat yetkazib berish servisi bilan: bank tizimi orqali to‘lovlarni qabul qilish va qayta ishlash; ichki tizimlar va hamkor API’si o‘rtasidagi aloqa; moliyaviy operatsiyalarni real vaqtda monitoring va loglash."]),
            dict(head="Integratsiya bo‘limi", bullets=[
                "MinStroy — Qurilish vazirligi bilan eskrou-hisoblar bo‘yicha integratsiya: turar va noturar joy bitimlarini avtomatlashtiruvchi servislar; bank va davlat idoralari o‘rtasida eskrou-hisoblarni ochish va yuritish; REST API orqali bildirishnoma va tasdiqlashlar.",
                "KATM — kredit assotsiatsiyasi bilan ikki tomonlama integratsiya: kredit arizalarini avtomatik yuborish, qayta ishlash va holatini kuzatish; ma’lumotlar xavfsizligi va validatsiyasi; asinxron qayta ishlash uchun RabbitMQ navbatlari."], tech=T_IPOTEKA)]),
        dict(co="REALSOFT", role="Dasturchilar guruhi rahbari", period="2022-yil sentyabr — 2023-yil dekabr", loc="Toshkent · realsoft.co", blocks=[
            dict(bullets=[
                "Kompaniyaning ichki to‘lov tizimi RealPay ishlab chiqilishiga rahbarlik qildim; tizim mening texnik rahbarligimda ishga tushirildi. 6 kishilik jamoa (3 backend, 3 frontend).",
                "To‘lovlar va kartadan kartaga o‘tkazmalar uchun Uzcard va Humo integratsiyasi.",
                "Davlat muassasalari foydalanadigan 10 dan ortiq ichki loyihani, jumladan bog‘cha va onlayn ta’lim to‘lovlarini RealPay’ga uladim.",
                "Arxitektura va servislararo xavfsiz REST API’larni loyihalash; relizlar, kod-revyu va mikroservislar integratsiyasini nazorat qilish."], tech=T_REALSOFT)]),
        dict(co="EPAM Uzbekistan", role="Software Engineer (Java Developer)", period="2022-yil yanvar — 2023-yil dekabr", loc="Toshkent", blocks=[
            dict(head="Loyiha: EPAM Certification System — EPAM muhandislarini sertifikatlashni avtomatlashtiruvchi ichki platforma", bullets=[
                "Java 17 / Spring Boot 2.x asosidagi server qismi; imtihonlar, foydalanuvchilar va natijalar modullari uchun REST API’larni loyihalash va yaratish.",
                "Tashqi servislar (LMS, email-shlyuz, Notification Service) bilan integratsiya; RabbitMQ navbatlari bilan ishlash.",
                "Unumdorlikni oshirish, refaktoring, texnik hujjatlar va kod-revyu; arxitektura va CI/CD (GitLab CI, Docker, Kubernetes) loyihalashda ishtirok."], tech=T_EPAM)]),
        dict(co="Tune Consulting", role="Java dasturchi", period="2020-yil yanvar — 2021-yil noyabr", loc="Toshkent", blocks=[
            dict(bullets=[
                "Apelsin (Kapital Bank) — mobil bank ekotizimi: CRM va dashboard modulining server mantig‘i; tranzaksiyalar, o‘tkazmalar, to‘lovlar va bonuslarni hisobga olish servislari; Android/iOS mijozlar va tashqi tizimlar uchun REST API; P2P o‘tkazmalar; COVID-19 karantini davrida kartalarni onlayn buyurtma qilish va uyga yetkazib berishni qisqa muddatda ishga tushirish; bankning Auth, Account, Transaction mikroservislari bilan integratsiya. <i>" + T_APELSIN + "</i>",
                "Apelsin Marketplace — bank servislari bilan integratsiyalashgan savdo platformasi: katalog, savat va to‘lovning server mantig‘i; mikroservislar (katalog, buyurtmalar, to‘lov) va bank to‘lov tizimi bilan integratsiya. <i>" + T_MARKET + "</i>",
                "Kapital24 — jismoniy va yuridik shaxslar uchun internet-banking: shaxsiy kabinet va biznes-akkauntlar API’si, to‘lov shlyuzlari bilan integratsiya, SQL so‘rovlarini optimallashtirish va operatsiyalar xavfsizligi. <i>" + T_K24 + "</i>",
                "E-commerce (Orient Finance Bank) — onlayn to‘lovlar integratsiya platformasi: to‘lov shlyuzi modullari va tranzaksiyalarni qayta ishlash mantig‘i. <i>" + T_ORIENT + "</i>"])]),
        dict(co="Davr Bank (XATB «Davr Bank»)", role="Java dasturchi (Strong Junior Backend Developer)", period="2019-yil may — 2020-yil yanvar", loc="Toshkent · Bank", blocks=[
            dict(head="Loyiha: DavrBank Mobile App — jismoniy shaxslar uchun mobil bank (to‘lovlar, o‘tkazmalar, hisoblarni boshqarish)", bullets=[
                "Java / Spring Boot asosidagi server qismi; Android va iOS jamoalari uchun REST API va hujjatlar.",
                "UzCard va Humo (to‘lovlar, P2P o‘tkazmalar) hamda Paynet integratsiyasi; NCI core-tizimi bilan ishlash.",
                "Test muhitlarini sozlash va SQL so‘rovlarini optimallashtirish."], tech=T_DAVR)]),
        dict(co="MIRONSOFT", role="Java dasturchi (Junior Software Developer)", period="2017-yil sentyabr — 2019-yil mart", loc="Toshkent", blocks=[
            dict(bullets=[
                "Ijod Fondi — ijod fondiga kiruvchi tashkilotlar hisobini avtomatlashtirish tizimi: to‘lovlar va buxgalteriya modullari; soliq imtiyozlarini avtomatik hisoblash; SQL unumdorligini oshirish.",
                "UzAgroExpertBank — hujjat aylanishini avtomatlashtirish: ichki hujjat aylanishi modullari, hujjatlarni yo‘naltirish va kelishuv holatlari; qo‘llab-quvvatlash va refaktoring."], tech=T_MIRON)]),
    ],
    certs_extra=[("2016", "TATU", "Chet tillarini o‘rganish bo‘yicha dasturiy ta’minot tanlovi")],
)
L["ru"] = dict(
    title="Java Software Developer", updated="Сентябрь 2026", location="Ташкент, Узбекистан",
    labels=dict(summary="О себе", exp="Опыт работы", edu="Образование", certs="Курсы и сертификаты", skills="Навыки", langs="Языки", format="Формат работы", qualities="Личные качества", tech="Технологии", project="Проект"),
    summary="Java-разработчик с опытом более 8 лет в банковском и финтех-секторе: мобильный и интернет-банкинг, платёжные системы и интеграции (Uzcard, Humo, Paynet, Wolt, госструктуры). Руководил командами до 6 человек, проектировал архитектуру и безопасные REST API, отвечал за релизы и код-ревью. Основной стек: Java 21, Spring Boot 3, Spring Cloud, PostgreSQL, Oracle, RabbitMQ, Docker.",
    qualities="Коммуникабельный, быстро обучаюсь и адаптируюсь к новым задачам; целеустремлённый и ответственный, ориентирован на результат; проявляю инициативу, эффективно работаю в команде; постоянно развиваюсь профессионально.",
    workformat="Полная занятость · офис, удалённо или гибрид · Ташкент",
    langs=["Узбекский — родной", "Русский — C2", "Английский — B2", "Турецкий — B2"],
    edu=[("Ташкентский университет информационных технологий", "Бакалавр — Компьютерный инжиниринг (компьютерные системы)", "2017")],
    skills=[("Backend", "Java 21, Spring Boot 3.x, Spring Security, OAuth2, Spring Data / JPA / JDBC, Hibernate"),
            ("Микросервисы", "Spring Cloud (Config, Discovery, Gateway, OpenFeign, Routing), RabbitMQ, ActiveMQ"),
            ("API", "REST, SOAP, JSON, XML, Swagger / OpenAPI"),
            ("Базы данных", "Oracle, PostgreSQL, MySQL; NoSQL: Redis, MongoDB, Elasticsearch"),
            ("Серверы и инструменты", "Apache Tomcat, NGINX, Docker, Kubernetes, Git / GitHub / GitLab CI/CD, Maven / Gradle"),
            ("Frontend (базовый)", "React.js / Vue.js, HTML5, CSS3, JavaScript")],
    jobs=[
        dict(co="Ipotekabank OTP Group", role="Руководитель группы разработки", period="Январь 2024 — Декабрь 2025", loc="Ташкент · Банк", blocks=[
            dict(head="Omnichannel Department", bullets=[
                "OpenAPI / DiBank — интеграция юридических клиентов: REST API для юридических лиц и корпоративных клиентов; оптимизация кода, внедрение обновлённой архитектуры безопасности и токенизации; взаимодействие между CRM и внутренними банковскими сервисами.",
                "Wolt Integration — интеграция с международным сервисом доставки еды: приём и обработка платежей через систему банка; взаимодействие внутренних систем с API партнёра; мониторинг и логирование финансовых операций в реальном времени."]),
            dict(head="Integration Department", bullets=[
                "MinStroy — интеграция с Министерством строительства по эскроу-счетам: сервисы автоматизации сделок с жилыми и нежилыми помещениями; создание и ведение эскроу-счетов между банком и госструктурами; уведомления и подтверждения через REST API.",
                "KATM — двусторонняя интеграция с кредитной ассоциацией: автоматическая подача, обработка и статусы кредитных заявок; безопасность и валидация данных; очереди RabbitMQ для асинхронной обработки."], tech=T_IPOTEKA)]),
        dict(co="REALSOFT", role="Руководитель группы разработки", period="Сентябрь 2022 — Декабрь 2023", loc="Ташкент · realsoft.co", blocks=[
            dict(bullets=[
                "Руководил разработкой внутренней платёжной системы RealPay, запущенной под моим техническим руководством; команда из 6 человек (3 backend, 3 frontend).",
                "Интеграция с Uzcard и Humo для обработки платежей и межкартовых переводов.",
                "Подключил более 10 внутренних проектов государственных учреждений к RealPay, включая оплаты для детских садов и онлайн-обучения.",
                "Проектирование архитектуры и безопасных REST API для межсервисного взаимодействия; контроль релизов, код-ревью и интеграции микросервисов."], tech=T_REALSOFT)]),
        dict(co="EPAM Uzbekistan", role="Software Engineer (Java Developer)", period="Январь 2022 — Декабрь 2023", loc="Ташкент", blocks=[
            dict(head="Проект: EPAM Certification System — внутренняя платформа автоматизации сертификации инженеров EPAM", bullets=[
                "Серверная часть на Java 17 / Spring Boot 2.x; проектирование и реализация REST API для модулей экзаменов, пользователей и результатов.",
                "Интеграция с внешними сервисами (LMS, email-шлюз, Notification Service); работа с очередями RabbitMQ.",
                "Оптимизация производительности, рефакторинг, техническая документация и код-ревью; участие в проектировании архитектуры и CI/CD (GitLab CI, Docker, Kubernetes)."], tech=T_EPAM)]),
        dict(co="Tune Consulting", role="Java-разработчик", period="Январь 2020 — Ноябрь 2021", loc="Ташкент", blocks=[
            dict(bullets=[
                "Apelsin (Kapital Bank) — экосистема мобильного банка: CRM и серверная логика dashboard-модуля; сервисы учёта транзакций, переводов, платежей и бонусов; REST API для Android/iOS-клиентов и внешних систем; P2P-переводы; быстрый запуск онлайн-заказа карт с доставкой на дом в период COVID-19; взаимодействие с микросервисами банка (Auth, Account, Transaction). <i>" + T_APELSIN + "</i>",
                "Apelsin Marketplace — торговая платформа, интегрированная с банковскими сервисами: серверная логика каталога, корзины и оплаты; микросервисы (каталог, заказы, оплата) и интеграция с платёжной системой банка. <i>" + T_MARKET + "</i>",
                "Kapital24 — интернет-банкинг для физических и юридических лиц: API личного кабинета и бизнес-аккаунтов, интеграция с платёжными шлюзами, оптимизация SQL-запросов и безопасность операций. <i>" + T_K24 + "</i>",
                "E-commerce (Orient Finance Bank) — платформа онлайн-платежей: модули платёжного шлюза и бизнес-логика обработки транзакций. <i>" + T_ORIENT + "</i>"])]),
        dict(co="ЧАКБ «Давр Банк»", role="Java-разработчик (Strong Junior Backend Developer)", period="Май 2019 — Январь 2020", loc="Ташкент · Банк", blocks=[
            dict(head="Проект: DavrBank Mobile App — мобильный банк для физических лиц (платежи, переводы, управление счетами)", bullets=[
                "Серверная часть на Java / Spring Boot; REST API и документация для Android- и iOS-команд.",
                "Интеграция с UzCard и Humo (платежи, P2P-переводы), сервисы для Paynet; взаимодействие с core-системой NCI.",
                "Настройка тестовых сред и оптимизация SQL-запросов."], tech=T_DAVR)]),
        dict(co="MIRONSOFT", role="Java-разработчик (Junior Software Developer)", period="Сентябрь 2017 — Март 2019", loc="Ташкент", blocks=[
            dict(bullets=[
                "Ijod Fondi — система учёта организаций творческого фонда: модули учёта платежей и бухгалтерских операций; автоматизация расчёта налоговых льгот; оптимизация SQL-запросов.",
                "UzAgroExpertBank — автоматизация документооборота: модули внутреннего документооборота, маршрутизация документов и статусы согласования; поддержка и рефакторинг."], tech=T_MIRON)]),
    ],
    certs_extra=[("2016", "ТУИТ", "Software contest for learning and enhancing foreign languages")],
)
L["en"] = dict(
    title="Java Software Developer", updated="September 2026", location="Tashkent, Uzbekistan",
    labels=dict(summary="Summary", exp="Experience", edu="Education", certs="Courses & certificates", skills="Skills", langs="Languages", format="Work format", qualities="Personal qualities", tech="Tech", project="Project"),
    summary="Java developer with 8+ years in banking and fintech: mobile and internet banking, payment systems and integrations (Uzcard, Humo, Paynet, Wolt, government services). Led teams of up to 6 engineers, designed architecture and secure REST APIs, owned releases and code reviews. Core stack: Java 21, Spring Boot 3, Spring Cloud, PostgreSQL, Oracle, RabbitMQ, Docker.",
    qualities="Communicative, fast learner, adapts quickly to new tasks; goal-driven, responsible and result-oriented; proactive and effective in a team; committed to continuous professional growth.",
    workformat="Full-time · on-site, remote or hybrid · Tashkent",
    langs=["Uzbek — native", "Russian — C2", "English — B2", "Turkish — B2"],
    edu=[("Tashkent University of Information Technologies", "Bachelor’s degree — Computer Engineering (Computer Systems)", "2017")],
    skills=[("Backend", "Java 21, Spring Boot 3.x, Spring Security, OAuth2, Spring Data / JPA / JDBC, Hibernate"),
            ("Microservices", "Spring Cloud (Config, Discovery, Gateway, OpenFeign, Routing), RabbitMQ, ActiveMQ"),
            ("API", "REST, SOAP, JSON, XML, Swagger / OpenAPI"),
            ("Databases", "Oracle, PostgreSQL, MySQL; NoSQL: Redis, MongoDB, Elasticsearch"),
            ("Servers & tools", "Apache Tomcat, NGINX, Docker, Kubernetes, Git / GitHub / GitLab CI/CD, Maven / Gradle"),
            ("Frontend (basic)", "React.js / Vue.js, HTML5, CSS3, JavaScript")],
    jobs=[
        dict(co="Ipotekabank OTP Group", role="Head of Development Team", period="January 2024 — December 2025", loc="Tashkent · Banking", blocks=[
            dict(head="Omnichannel Department", bullets=[
                "OpenAPI / DiBank, corporate client integration: REST APIs for legal entities and corporate clients; code optimisation, updated security and tokenisation architecture; integration between CRM and internal banking services.",
                "Wolt integration with the international food-delivery service: payment acceptance and processing through the bank’s system; connectivity between internal systems and the partner API; real-time monitoring and logging of financial operations."]),
            dict(head="Integration Department", bullets=[
                "MinStroy, escrow-account integration with the Ministry of Construction: services automating residential and commercial property deals; creation and maintenance of escrow accounts between the bank and state bodies; REST notifications and confirmations.",
                "KATM, two-way integration with the credit association: automatic submission, processing and status tracking of credit applications; data security and validation; RabbitMQ queues for asynchronous processing."], tech=T_IPOTEKA)]),
        dict(co="REALSOFT", role="Head of Development Team", period="September 2022 — December 2023", loc="Tashkent · realsoft.co", blocks=[
            dict(bullets=[
                "Led the development of RealPay, the company’s internal payment system, launched under my technical leadership; team of 6 (3 backend, 3 frontend).",
                "Uzcard and Humo integration for payments and card-to-card transfers.",
                "Connected 10+ internal projects used by government institutions to RealPay, including kindergarten and online-learning payments.",
                "Architecture design and secure REST APIs for service-to-service communication; release control, code review and microservice integration."], tech=T_REALSOFT)]),
        dict(co="EPAM Uzbekistan", role="Software Engineer (Java Developer)", period="January 2022 — December 2023", loc="Tashkent", blocks=[
            dict(head="Project: EPAM Certification System, an internal platform automating engineer certification", bullets=[
                "Backend in Java 17 / Spring Boot 2.x; design and implementation of REST APIs for the exam, user and results modules.",
                "Integration with external services (LMS, email gateway, notification service); RabbitMQ messaging.",
                "Performance optimisation, refactoring, technical documentation and code review; participation in architecture and CI/CD design (GitLab CI, Docker, Kubernetes)."], tech=T_EPAM)]),
        dict(co="Tune Consulting", role="Java Developer", period="January 2020 — November 2021", loc="Tashkent", blocks=[
            dict(bullets=[
                "Apelsin (Kapital Bank), mobile banking ecosystem: CRM and backend logic of the dashboard module; transaction, transfer, payment and bonus services; REST APIs for Android/iOS clients and external systems; P2P transfers; rapid launch of online card ordering with home delivery during COVID-19; integration with the bank’s Auth, Account and Transaction microservices. <i>" + T_APELSIN + "</i>",
                "Apelsin Marketplace, a trading platform integrated with banking services: backend logic for catalogue, cart and checkout; microservices (catalogue, orders, payment) integrated with the bank’s payment system. <i>" + T_MARKET + "</i>",
                "Kapital24, internet banking for individuals and businesses: personal and business account APIs, payment gateway integration, SQL optimisation and operation security. <i>" + T_K24 + "</i>",
                "E-commerce (Orient Finance Bank), online payment integration platform: payment gateway modules and transaction processing logic. <i>" + T_ORIENT + "</i>"])]),
        dict(co="Davr Bank", role="Java Developer (Strong Junior Backend Developer)", period="May 2019 — January 2020", loc="Tashkent · Banking", blocks=[
            dict(head="Project: DavrBank Mobile App, retail mobile banking (payments, transfers, account management)", bullets=[
                "Backend in Java / Spring Boot; REST APIs and documentation for the Android and iOS teams.",
                "UzCard and Humo integration (payments, P2P transfers) and Paynet services; integration with the NCI core banking system.",
                "Test environment setup and SQL query optimisation."], tech=T_DAVR)]),
        dict(co="MIRONSOFT", role="Java Developer (Junior Software Developer)", period="September 2017 — March 2019", loc="Tashkent", blocks=[
            dict(bullets=[
                "Ijod Fondi, accounting and automation system for the creative fund’s organisations: payment and accounting modules; automated tax-benefit calculation; SQL performance.",
                "UzAgroExpertBank, document workflow automation: internal workflow modules, document routing and approval statuses; maintenance and refactoring."], tech=T_MIRON)]),
    ],
    certs_extra=[("2016", "TUIT", "Software contest for learning and enhancing foreign languages")],
)
