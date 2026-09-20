#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Builds the selling site from template.html + content.py: one static page per language
# (site/business/index.html for the first language, site/business/<lang>/index.html for the others), sitemap.xml
# and api/lead-quiz.php (the quiz answers the lead endpoint accepts).
# Standard library only.
# Usage: python3 tools/business/build_site.py [output-dir]
import datetime, html, json, os, re, sys
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import L, LANGS, OPENAPI_DOCS, PAIN_CODES, SETTINGS

REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "site", "business")
TOKEN = re.compile(r"\{\{([a-z0-9_]+)\}\}")
CODE = re.compile(r"^[a-z][a-z0-9-]{0,23}$")  # quiz keys and option codes: they travel to api/lead.php

# 24-unit stroke icons, wrapped the same way as the icon sprite of ravshancha.uz.
ICON_WRAP = ('    <symbol id="icon-{name}" viewBox="0 0 64 64"><g transform="translate(12 12) scale(1.666667)" fill="none" '
             'stroke="currentColor" stroke-width="1.80" stroke-linecap="round" stroke-linejoin="round">{body}</g></symbol>')
ICONS = {
    "sun": '<circle cx="12" cy="12" r="4.5"/><path d="M12 1.8V5M12 19v3.2M22.2 12H19M5 12H1.8M19.2 4.8l-2.3 2.3M7.1 16.9l-2.3 2.3M19.2 19.2l-2.3-2.3M7.1 7.1L4.8 4.8"/>',
    "moon": '<path d="M20.6 14.3A9.3 9.3 0 1 1 9.7 3.4 7.3 7.3 0 0 0 20.6 14.3z"/>',
    "chevron-down": '<path d="M2.4 8.4L12 18l9.6-9.6"/>',
    "arrow-right": '<path d="M2.4 12h19.2M13.4 3.8L21.6 12l-8.2 8.2"/>',
    "arrow-left": '<path d="M21.6 12H2.4M10.6 3.8L2.4 12l8.2 8.2"/>',
    "arrow-up": '<path d="M12 21.6V2.4M3.8 10.6L12 2.4l8.2 8.2"/>',
    "arrow-up-right": '<path d="M5.4 18.6L18.6 5.4"/><path d="M8.4 5.4h10.2v10.2"/>',
    "link": '<path d="M10.2 13.2a4.8 4.8 0 0 0 7.2.5l2.4-2.4a4.8 4.8 0 0 0-6.8-6.8l-1.4 1.4"/><path d="M13.8 10.8a4.8 4.8 0 0 0-7.2-.5l-2.4 2.4a4.8 4.8 0 0 0 6.8 6.8l1.4-1.4"/>',
    "clock": '<circle cx="12" cy="12" r="9.8"/><path d="M12 6.2V12l3.9 2.4"/>',
    "team": '<path d="M15.4 20.6v-2a4 4 0 0 0-4-4H5.9a4 4 0 0 0-4 4v2"/><circle cx="8.7" cy="6.8" r="3.6"/><path d="M22.1 20.6v-2a4 4 0 0 0-3-3.9M15.9 3.5a3.6 3.6 0 0 1 0 6.9"/>',
    "search": '<circle cx="10.6" cy="10.6" r="7"/><path d="M15.8 15.8l5.8 5.8"/>',
    "bolt": '<path d="M13.2 2.4L4.2 13.6h6.9l-1.3 8 9-11.2h-6.9z"/>',
    "chart": '<path d="M2.4 21.6h19.2"/><path d="M6 21.6v-7.2M12 21.6V4.8M18 21.6V10.2"/>',
    "chat": '<path d="M21.6 11.6a8.6 8.6 0 0 1-12.6 7.6L2.4 21.6l2.4-6.2a8.6 8.6 0 1 1 16.8-3.8z"/>',
    "calendar": '<rect x="2.8" y="4.6" width="18.4" height="16.6" rx="2.4"/><path d="M2.8 9.8h18.4M7.8 2.4v4.2M16.2 2.4v4.2"/>',
    "box": '<path d="M21 7.6l-9-5-9 5v8.8l9 5 9-5z"/><path d="M3.3 7.8L12 12.6l8.7-4.8M12 21.4v-8.8"/>',
    "user": '<circle cx="12" cy="7.4" r="4.2"/><path d="M3.8 21.6v-1.4a5.4 5.4 0 0 1 5.4-5.4h5.6a5.4 5.4 0 0 1 5.4 5.4v1.4"/>',
    "grid": '<rect x="2.8" y="2.8" width="7.4" height="7.4" rx="1.6"/><rect x="13.8" y="2.8" width="7.4" height="7.4" rx="1.6"/><rect x="2.8" y="13.8" width="7.4" height="7.4" rx="1.6"/><rect x="13.8" y="13.8" width="7.4" height="7.4" rx="1.6"/>',
    "wallet": '<path d="M2.8 7.2a2.4 2.4 0 0 1 2.4-2.4h13.2v4"/><path d="M2.8 7.2v11.2a2.4 2.4 0 0 0 2.4 2.4h16V9.6h-16a2.4 2.4 0 0 1-2.4-2.4z"/><path d="M16.6 15.2h.1"/>',
    "doc": '<path d="M13.8 2.4H6.4a1.8 1.8 0 0 0-1.8 1.8v15.6a1.8 1.8 0 0 0 1.8 1.8h11.2a1.8 1.8 0 0 0 1.8-1.8V8z"/><path d="M13.8 2.4V8h5.6M8.4 13h7.2M8.4 17h7.2"/>',
    "check": '<path d="M3.6 12.6l5.4 5.4L20.4 6.6"/>',
    "plus": '<path d="M12 4.2v15.6M4.2 12h15.6"/>',
    "close": '<path d="M4.8 4.8l14.4 14.4M19.2 4.8L4.8 19.2"/>',
}


def esc(text):
    return html.escape(str(text), quote=True)


def icon(name, extra=""):
    if name not in ICONS:
        raise SystemExit(f"content.py refers to an unknown icon: {name}")
    classes = ("site-icon " + extra).strip()
    return f'<svg class="{classes}" aria-hidden="true" focusable="false"><use href="#icon-{name}"/></svg>'


def lines(items, indent):
    return "\n".join(" " * indent + item for item in items)


def php_string(text):
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'") + "'"


def quiz_questions(t):
    # Every question with its full option list; the one marked from_pains offers the pain titles first.
    questions = []
    for question in t["quiz"]:
        options = list(question["options"])
        if question.get("from_pains"):
            options = [(code, title) for code, (_, title, _) in zip(PAIN_CODES, t["pains"])] + options
        questions.append(dict(question, options=options, multi=bool(question.get("multi"))))
    return questions


def render_fragments(t, lang):
    f = {}
    root = "../" * LANGS[lang]["path"].count("/")
    f["icon_symbols_html"] = "\n".join(ICON_WRAP.format(name=name, body=body) for name, body in ICONS.items())
    f["hero_trust_html"] = lines([f'<li>{icon("check", "icon-accent")}<span>{esc(text)}</span></li>' for text in t["hero_trust"]], 14)
    f["hero_cards_html"] = lines([
        f'<li class="service-card"><span class="service-icon">{icon(name, "icon-accent")}</span><div><strong>{esc(title)}</strong><small>{esc(meta)}</small></div></li>'
        for name, title, meta in t["hero_cards"]], 12)
    f["stats_html"] = lines([
        f'<div class="stat-card"><span class="stat-icon">{icon(name, "icon-accent")}</span><strong>{esc(value)}</strong><span>{esc(label)}</span></div>'
        for name, value, label in t["stats"]], 12)
    f["pains_html"] = lines([
        f'<article class="pain-card reveal"><div class="card-head"><h3>{esc(title)}</h3><span class="card-icon" aria-hidden="true">{icon(name)}</span></div><p>{esc(text)}</p></article>'
        for name, title, text in t["pains"]], 10)
    f["services_html"] = lines([
        f'<article class="expertise-card reveal"><div class="card-head"><h3>{esc(title)}</h3><span class="card-icon" aria-hidden="true">{icon(name)}</span></div>'
        f'<p>{esc(text)}</p><p class="service-result"><span>{esc(t["result_label"])}</span>{esc(result)}</p>'
        f'<div class="tag-list">{"".join(f"<span>{esc(tag)}</span>" for tag in tags)}</div></article>'
        for name, title, text, result, tags in t["services"]], 10)
    f["process_html"] = lines([
        f'<article class="reveal"><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></article>'
        for title, text in t["process"]], 10)
    f["facts_html"] = lines([
        f'<div><dt><span class="fact-icon">{icon(name, "icon-accent")}</span><span>{esc(label)}</span></dt><dd>{esc(value)}</dd></div>'
        for name, label, value in t["facts"]], 12)
    cases = []
    for case in t["cases"]:
        logo_src = root + "../assets/" + case["logo"]
        docs = ""
        if case.get("docs"):
            docs = (f'<a class="text-link" href="{esc(OPENAPI_DOCS[lang])}" target="_blank" rel="noopener noreferrer">'
                    f'<span>{esc(t["case_docs"])}</span>{icon("arrow-up-right")}</a>')
        cases.append(
            f'<article class="case-card reveal"><p class="case-type">{esc(case["type"])}</p><h3>{esc(case["name"])}</h3>'
            f'<p class="case-role"><img src="{esc(logo_src)}" alt="{esc(case["company"])}"><span>{esc(case["role"])}</span></p>'
            f'<dl class="case-rows"><div><dt>{esc(t["case_task"])}</dt><dd>{esc(case["task"])}</dd></div>'
            f'<div><dt>{esc(t["case_solution"])}</dt><dd>{esc(case["solution"])}</dd></div>'
            f'<div class="case-result"><dt>{esc(t["case_result"])}</dt><dd>{esc(case["result"])}</dd></div></dl>{docs}</article>')
    f["cases_html"] = lines(cases, 10)
    f["faq_html"] = lines([
        f'<details class="faq-item"><summary><span>{esc(question)}</span>{icon("plus")}</summary><p>{esc(answer)}</p></details>'
        for question, answer in t["faq"]], 10)
    steps = []
    for question in quiz_questions(t):
        key, kind = esc(question["key"]), "checkbox" if question["multi"] else "radio"
        choices = "".join(
            f'<label class="quiz-option"><input type="{kind}" name="{key}" value="{esc(code)}"><span class="quiz-mark">{icon("check")}</span><span>{esc(label)}</span></label>'
            for code, label in question["options"])
        steps.append(
            f'<div class="quiz-step" role="{"group" if question["multi"] else "radiogroup"}" aria-labelledby="quiz-title-{key}" data-quiz-step="{key}" '
            f'data-quiz-label="{esc(question["label"])}"{" data-quiz-multi" if question["multi"] else ""} hidden>'
            f'<h3 class="quiz-title" id="quiz-title-{key}" tabindex="-1">{esc(question["title"])}</h3>'
            f'<p class="quiz-hint">{esc(t["quiz_hint_multi" if question["multi"] else "quiz_hint_single"])}</p>'
            f'<div class="quiz-options">{choices}</div></div>')
    f["quiz_steps_html"] = lines(steps, 8)
    return f


def page_url(lang):
    return SETTINGS["base_url"] + LANGS[lang]["path"]


def render_page(template, lang):
    t, meta = L[lang], LANGS[lang]
    root = "../" * meta["path"].count("/")
    default_lang = next(iter(LANGS))
    assets = root + SETTINGS["assets"]
    assets_abs = urljoin(SETTINGS["base_url"], SETTINGS["assets"])
    og_image = assets_abs + f"og-{lang}.jpg"  # drawn by build_og.py

    options = []
    for code, other in LANGS.items():
        active = code == lang
        current = ' aria-current="page"' if active else ""
        options.append(
            f'<a class="language-option{" active" if active else ""}" href="{esc((root + other["path"]) or "./")}" hreflang="{code}" lang="{code}"{current}>'
            f'<svg class="language-flag" viewBox="0 0 24 16" aria-hidden="true" focusable="false"><use href="#{other["flag"]}"/></svg>'
            f'<span>{esc(other["name"])}</span></a>')

    alternates = [f'  <link rel="alternate" hreflang="{code}" href="{esc(page_url(code))}">' for code in LANGS]
    alternates.append(f'  <link rel="alternate" hreflang="x-default" href="{esc(page_url(default_lang))}">')
    og_alternates = [f'  <meta property="og:locale:alternate" content="{other["og_locale"]}">' for code, other in LANGS.items() if code != lang]

    json_ld = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": t["ld_name"],
        "description": t["og_description"],
        "url": page_url(lang),
        "image": og_image,
        "address": {"@type": "PostalAddress", "addressLocality": "Tashkent", "addressCountry": "UZ"},
        "areaServed": {"@type": "Country", "name": "Uzbekistan"},
        "knowsLanguage": list(LANGS),
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": t["services_kicker"],
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": title, "description": text}}
                for _, title, text, _, _ in t["services"]
            ],
        },
        "founder": {
            "@type": "Person",
            "name": SETTINGS["person"],
            "url": SETTINGS["cv_url"],
            "sameAs": [SETTINGS["linkedin"], "https://t.me/" + SETTINGS["telegram"]],
        },
    }

    metrika_id = SETTINGS["metrika_id"].strip()
    if metrika_id and not metrika_id.isdigit():
        raise SystemExit("SETTINGS['metrika_id'] must contain digits only")
    metrika = ""
    if metrika_id:
        metrika = (
            "  <script>\n"
            "    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};m[i].l=1*new Date();\n"
            "    for (var j = 0; j < document.scripts.length; j++) { if (document.scripts[j].src === r) { return; } }\n"
            "    k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})\n"
            '    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");\n'
            f'    ym({metrika_id}, "init", {{ clickmap: true, trackLinks: true, accurateTrackBounce: true, webvisor: true }});\n'
            "  </script>")

    site = {
        "root": root,
        "assets": assets,
        "lang": lang,
        "telegram": SETTINGS["telegram"],
        "metrikaId": int(metrika_id) if metrika_id else 0,
        "t": {
            "themeDark": t["theme_dark"], "themeLight": t["theme_light"],
            "submit": t["order_submit"], "sending": t["order_sending"],
            "messageTitle": t["order_message_title"], "name": t["order_name"], "phone": t["order_phone"],
            "info": t["order_message_info"],
        },
    }

    context = {key: value for key, value in t.items() if isinstance(value, str)}
    context.update(render_fragments(t, lang))
    context.update(
        lang=lang, root=root, assets=assets, og_image=og_image, canonical=page_url(lang), base_url=SETTINGS["base_url"], og_locale=meta["og_locale"],
        lang_code=meta["code"], lang_name=meta["name"], lang_flag=meta["flag"],
        person=SETTINGS["person"], linkedin=SETTINGS["linkedin"],
        telegram_url="https://t.me/" + SETTINGS["telegram"],  # the order form's fallback link; the page itself shows no contact channels
        quiz_intro=t["quiz_intro"].format(count=len(t["quiz"])), stat_cta_label=t["stat_cta_label"].format(count=len(t["quiz"])), quiz_total=str(len(t["quiz"]) + 1),  # the contact fields are the last step
        language_options_html=lines(options, 14), alternates_html="\n".join(alternates), og_alternates_html="\n".join(og_alternates),
        json_ld_html=json.dumps(json_ld, ensure_ascii=False, indent=2).replace("</", "<\\/"),
        site_json_html=json.dumps(site, ensure_ascii=False).replace("</", "<\\/"),
        metrika_html=metrika,
    )

    missing = sorted(set(TOKEN.findall(template)) - set(context))
    if missing:
        raise SystemExit(f"template.html uses tokens that content.py does not define ({lang}): {', '.join(missing)}")

    def fill(match):
        key = match.group(1)
        return context[key] if key.endswith("_html") else esc(context[key])

    return TOKEN.sub(fill, template)


def main():
    if set(L) != set(LANGS):
        raise SystemExit("content.py: L and LANGS must describe the same languages")
    reference = next(iter(L.values()))
    for lang, t in L.items():
        diff = set(t) ^ set(reference)
        if diff:
            raise SystemExit(f"content.py: language '{lang}' differs in keys: {', '.join(sorted(diff))}")
    if not SETTINGS["base_url"].endswith("/"):
        raise SystemExit("SETTINGS['base_url'] must end with a slash")

    # The quiz sends codes, not texts: every language has to describe the same questions and options.
    quiz_shape = None
    for lang, t in L.items():
        if len(t["pains"]) != len(PAIN_CODES):
            raise SystemExit(f"content.py: PAIN_CODES must name every pain, in order ({lang})")
        shape = [(question["key"], question["multi"], [code for code, _ in question["options"]]) for question in quiz_questions(t)]
        bad = sorted({code for key, _, codes in shape for code in [key] + codes if not CODE.match(code)})
        if bad:
            raise SystemExit(f"content.py: quiz keys and option codes are lowercase latin, digits and '-' ({lang}): {', '.join(bad)}")
        if len({key for key, _, _ in shape}) != len(shape) or any(len(set(codes)) != len(codes) for _, _, codes in shape):
            raise SystemExit(f"content.py: the quiz repeats a question key or an option code ({lang})")
        if quiz_shape is not None and shape != quiz_shape:
            raise SystemExit(f"content.py: the quiz in '{lang}' differs from the first language in keys, order or option codes")
        quiz_shape = quiz_shape or shape

    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as source:
        template = source.read()

    for lang, meta in LANGS.items():
        target = os.path.join(OUT, meta["path"], "index.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as out:
            out.write(render_page(template, lang))
        print(f"{lang}: {os.path.relpath(target, REPO)}  ({os.path.getsize(target) // 1024} KB)")

    # api/lead.php accepts only these answer codes and writes their labels (first language) into the message.
    quiz_rows = []
    for question in quiz_questions(reference):
        options = ", ".join(f"{php_string(code)} => {php_string(label)}" for code, label in question["options"])
        quiz_rows.append(f"    {php_string(question['key'])} => ['label' => {php_string(question['label'])}, "
                         f"'multi' => {'true' if question['multi'] else 'false'}, 'options' => [{options}]],\n")
    quiz_map = os.path.join(OUT, "api", "lead-quiz.php")
    os.makedirs(os.path.dirname(quiz_map), exist_ok=True)
    with open(quiz_map, "w", encoding="utf-8") as out:
        out.write("<?php\n// Generated by tools/business/build_site.py from content.py — do not edit by hand.\n"
                  "// The quiz answers lead.php accepts: question key => label, multi, option code => label.\n"
                  "return [\n" + "".join(quiz_rows) + "];\n")
    print(f"quiz: {os.path.relpath(quiz_map, REPO)}  ({len(quiz_rows)} questions)")

    today = datetime.date.today().isoformat()
    alternates = "".join(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{esc(page_url(code))}"/>\n' for code in LANGS)
    urls = "".join(
        f"  <url>\n    <loc>{esc(page_url(lang))}</loc>\n{alternates}    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n  </url>\n" for lang in LANGS)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as out:
        out.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')

    # Crawlers read robots.txt only at the host root; in a subfolder the parent site's robots.txt has to list this sitemap.
    sitemap_url = SETTINGS["base_url"] + "sitemap.xml"
    if urlparse(SETTINGS["base_url"]).path == "/":
        with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as out:
            out.write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {sitemap_url}\n")
    else:
        host_robots = os.path.join(REPO, "site", "robots.txt")
        listed = os.path.isfile(host_robots) and sitemap_url in open(host_robots, encoding="utf-8").read()
        if not listed:
            print(f"note: the site lives in a subfolder — add 'Sitemap: {sitemap_url}' to the host's root robots.txt")

    with open(os.path.join(HERE, "content.py"), encoding="utf-8") as source:
        pending = [line.split("TASDIQLANG", 1)[1].lstrip(": ").strip() for line in source if "TASDIQLANG" in line]
    pending = [item for item in pending if item and not item.startswith("—")]  # the header comment explains the marker itself
    if pending:
        print(f"\nTASDIQLANG — {len(pending)} band hali tasdiqlanmagan:")
        for item in pending:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
