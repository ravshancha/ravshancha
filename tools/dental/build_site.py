#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Builds the dentistry pages from template.html + content.py, in every language (the first one at the root, the others
# under <lang>/), and sitemap.xml:
#   main      site/dental/[<lang>/]index.html                       — clinics: Dental Navigator for dental clinics
#   patients  site/dental/[<lang>/]<slug>/index.html               — patients: what the direction is, how to choose a clinic
#   clinics   site/dental/[<lang>/]<slug>/klinikalar/index.html    — clinics: show this direction to the patients who look for it
# One template serves all three: <!-- clinics:start --> / <!-- patients:start --> blocks are kept or dropped per page.
# Standard library only.
# Usage: python3 tools/dental/build_site.py [output-dir]
import datetime, html, json, os, posixpath, re, sys
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import DIRECTIONS, KEYWORD_STEM, L, LANGS, SETTINGS

REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "site", "dental")
TOKEN = re.compile(r"\{\{([a-z0-9_]+)\}\}")
KEYWORD = re.compile(r"\[\[(.+?)\]\]")
# Keys a direction's clinic page has on top of the main page's copy.
DIRECTION_KEYS = {"direction_name", "breadcrumb_nav_label", "patients_link_label"}
CLINICS_DIR = "klinikalar"  # the clinic page of a direction lives under its patient page
BLOCK = re.compile(r"<!-- ([a-z]+):start -->\n(.*?)<!-- \1:end -->\n", re.S)

# 24-unit stroke icons, wrapped the same way as the icon sprite of ravshancha.uz.
ICON_WRAP = ('    <symbol id="icon-{name}" viewBox="0 0 64 64"><g transform="translate(12 12) scale(1.666667)" fill="none" '
             'stroke="currentColor" stroke-width="1.80" stroke-linecap="round" stroke-linejoin="round">{body}</g></symbol>')
TOOTH = ('<path d="M7.4 2.8c-2.5 0-4.2 1.9-4.2 4.5 0 1.7.5 2.9.9 4.4.5 1.9.6 4.2 1 6.3.3 1.7.8 3.2 2 3.2 1.3 0 1.5-1.7 1.8-3.4.3-1.7.8-3 3.1-3'
         's2.8 1.3 3.1 3c.3 1.7.5 3.4 1.8 3.4 1.2 0 1.7-1.5 2-3.2.4-2.1.5-4.4 1-6.3.4-1.5.9-2.7.9-4.4 0-2.6-1.7-4.5-4.2-4.5-1.8 0-2.9 1-4.6 1s-2.8-1-4.6-1z"/>')
ICONS = {
    "sun": '<circle cx="12" cy="12" r="4.5"/><path d="M12 1.8V5M12 19v3.2M22.2 12H19M5 12H1.8M19.2 4.8l-2.3 2.3M7.1 16.9l-2.3 2.3M19.2 19.2l-2.3-2.3M7.1 7.1L4.8 4.8"/>',
    "moon": '<path d="M20.6 14.3A9.3 9.3 0 1 1 9.7 3.4 7.3 7.3 0 0 0 20.6 14.3z"/>',
    "chevron-down": '<path d="M2.4 8.4L12 18l9.6-9.6"/>',
    "arrow-right": '<path d="M2.4 12h19.2M13.4 3.8L21.6 12l-8.2 8.2"/>',
    "arrow-up": '<path d="M12 21.6V2.4M3.8 10.6L12 2.4l8.2 8.2"/>',
    "arrow-up-right": '<path d="M5.4 18.6L18.6 5.4"/><path d="M8.4 5.4h10.2v10.2"/>',
    "telegram": '<path d="M3.5 4.4a1.2 1.2 0 0 0-1.7 1.5l2 5.4a1.2 1.2 0 0 1 0 .8l-2 5.4a1.2 1.2 0 0 0 1.7 1.5l17.6-7.2a1.2 1.2 0 0 0 0-2.2z"/><path d="M4.4 12h7.2"/>',
    "whatsapp": '<path d="M3.1 20.9l1.3-4.7A8.9 8.9 0 1 1 7.8 19.6l-4.7 1.3z"/><path d="M8.9 8.4c.3-.1.6 0 .8.3l.8 1.5c.1.3.1.6-.1.8l-.5.6c-.2.2-.2.4-.1.6.5.9 1.3 1.7 2.2 2.2.2.1.4.1.6-.1l.6-.5c.2-.2.5-.2.8-.1l1.5.8c.3.2.4.5.3.8-.2.8-1 1.3-1.8 1.3-2.8 0-6.1-3.3-6.1-6.1 0-.8.5-1.6 1.3-1.8z"/>',
    "phone": '<path d="M21.6 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 1.7 4.1 2 2 0 0 1 3.7 2h3a2 2 0 0 1 2 1.7 12.8 12.8 0 0 0 .7 2.8 2 2 0 0 1-.5 2.1L7.7 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4 12.8 12.8 0 0 0 2.8.7 2 2 0 0 1 1.7 2z"/>',
    "link": '<path d="M10.2 13.2a4.8 4.8 0 0 0 7.2.5l2.4-2.4a4.8 4.8 0 0 0-6.8-6.8l-1.4 1.4"/><path d="M13.8 10.8a4.8 4.8 0 0 0-7.2-.5l-2.4 2.4a4.8 4.8 0 0 0 6.8 6.8l1.4-1.4"/>',
    "clock": '<circle cx="12" cy="12" r="9.8"/><path d="M12 6.2V12l3.9 2.4"/>',
    "team": '<path d="M15.4 20.6v-2a4 4 0 0 0-4-4H5.9a4 4 0 0 0-4 4v2"/><circle cx="8.7" cy="6.8" r="3.6"/><path d="M22.1 20.6v-2a4 4 0 0 0-3-3.9M15.9 3.5a3.6 3.6 0 0 1 0 6.9"/>',
    "chart": '<path d="M2.4 21.6h19.2"/><path d="M6 21.6v-7.2M12 21.6V4.8M18 21.6V10.2"/>',
    "chat": '<path d="M21.6 11.6a8.6 8.6 0 0 1-12.6 7.6L2.4 21.6l2.4-6.2a8.6 8.6 0 1 1 16.8-3.8z"/>',
    "calendar": '<rect x="2.8" y="4.6" width="18.4" height="16.6" rx="2.4"/><path d="M2.8 9.8h18.4M7.8 2.4v4.2M16.2 2.4v4.2"/>',
    "user": '<circle cx="12" cy="7.4" r="4.2"/><path d="M3.8 21.6v-1.4a5.4 5.4 0 0 1 5.4-5.4h5.6a5.4 5.4 0 0 1 5.4 5.4v1.4"/>',
    "grid": '<rect x="2.8" y="2.8" width="7.4" height="7.4" rx="1.6"/><rect x="13.8" y="2.8" width="7.4" height="7.4" rx="1.6"/><rect x="2.8" y="13.8" width="7.4" height="7.4" rx="1.6"/><rect x="13.8" y="13.8" width="7.4" height="7.4" rx="1.6"/>',
    "doc": '<path d="M13.8 2.4H6.4a1.8 1.8 0 0 0-1.8 1.8v15.6a1.8 1.8 0 0 0 1.8 1.8h11.2a1.8 1.8 0 0 0 1.8-1.8V8z"/><path d="M13.8 2.4V8h5.6M8.4 13h7.2M8.4 17h7.2"/>',
    "check": '<path d="M3.6 12.6l5.4 5.4L20.4 6.6"/>',
    "plus": '<path d="M12 4.2v15.6M4.2 12h15.6"/>',
    "tooth": TOOTH,
    "pin": '<path d="M12 21.8s-7.2-6.2-7.2-11.9a7.2 7.2 0 0 1 14.4 0c0 5.7-7.2 11.9-7.2 11.9z"/><circle cx="12" cy="9.9" r="2.7"/>',
    "star": '<path d="M12 2.8l2.8 5.8 6.4.9-4.6 4.5 1.1 6.4L12 17.4l-5.7 3 1.1-6.4-4.6-4.5 6.4-.9z"/>',
    "shield": '<path d="M12 2.4l7.8 3v5.8c0 5-3.3 8.9-7.8 10.4-4.5-1.5-7.8-5.4-7.8-10.4V5.4z"/><path d="M8.4 12l2.6 2.6 4.8-5"/>',
}


def esc(text):
    return html.escape(str(text), quote=True)


def plain(text):
    """Text for meta tags, JSON-LD and attributes: the [[keyword]] markers are dropped."""
    return KEYWORD.sub(r"\1", text)


def rich(text, escape=True):
    """Visible text: [[keyword]] becomes <strong class="kw">."""
    return KEYWORD.sub(r'<strong class="kw">\1</strong>', esc(text) if escape else text)


def icon(name, extra=""):
    if name not in ICONS:
        raise SystemExit(f"content.py refers to an unknown icon: {name}")
    classes = ("site-icon " + extra).strip()
    return f'<svg class="{classes}" aria-hidden="true" focusable="false"><use href="#icon-{name}"/></svg>'


def lines(items, indent):
    return "\n".join(" " * indent + item for item in items)


def render_fragments(t):
    f = {}
    symbols = [ICON_WRAP.format(name=name, body=body) for name, body in ICONS.items()]
    symbols.append(f'    <symbol id="shape-tooth" viewBox="0 0 24 24">{TOOTH}</symbol>')  # the hero outline sets its own stroke
    f["icon_symbols_html"] = "\n".join(symbols)
    f["hero_trust_html"] = lines([f'<li>{icon("check", "icon-accent")}<span>{rich(text)}</span></li>' for text in t["hero_trust"]], 12)
    f["hero_chips_html"] = lines([f'<li>{icon(name, "icon-accent")}<span>{rich(text)}</span></li>' for name, text in t["hero_chips"]], 12)
    f["audience_html"] = lines([
        f'<article class="audience-card reveal"><span class="card-icon" aria-hidden="true">{icon(name)}</span><div><h3>{rich(title)}</h3><small>{rich(meta)}</small></div><p>{rich(text)}</p></article>'
        for name, title, meta, text in t["audience"]], 10)
    f["pains_html"] = lines([
        f'<article class="pain-card reveal"><div class="card-head"><span class="card-icon" aria-hidden="true">{icon(name)}</span></div><h3>{rich(title)}</h3><p>{rich(text)}</p></article>'
        for name, title, text in t["pains"]], 10)
    f["features_html"] = lines([
        f'<article class="feature-card reveal"><div class="card-head"><span class="card-icon" aria-hidden="true">{icon(name)}</span></div>'
        f'<h3>{rich(title)}</h3><p>{rich(text)}</p><p class="feature-result"><span>{esc(t["result_label"])}</span>{rich(result)}</p>'
        f'<div class="tag-list">{"".join(f"<span>{esc(tag)}</span>" for tag in tags)}</div></article>'
        for name, title, text, result, tags in t["features"]], 10)
    f["modules_html"] = lines([f"<li>{esc(name)}</li>" for name in t["modules"]], 12)

    tariffs = []
    for tariff in t["tariffs"]:
        items = "".join(f'<li>{icon("check", "icon-accent")}<span>{rich(item)}</span></li>' for item in tariff["items"])
        if tariff["featured"]:
            button = (f'<a class="button button-primary" href="{esc(SETTINGS["apply_url"])}" target="_blank" rel="noopener" data-goal="click_apply">'
                      f'<span>{esc(t["tariff_cta"])}</span>{icon("arrow-right", "button-icon")}</a>')
        else:
            button = f'<button class="button button-secondary" type="button" data-order-open>{icon("phone")}<span>{esc(t["cta_call"])}</span></button>'
        tariffs.append(
            f'<article class="tariff-card reveal{" featured" if tariff["featured"] else ""}"><p class="tariff-name">{esc(tariff["name"])}</p>'
            f'<p class="tariff-price"><strong>{esc(tariff["price"])}</strong><span>{esc(tariff["period"])}</span></p><p>{rich(tariff["text"])}</p>'
            f'<ul class="check-list">{items}</ul>{button}</article>')
    f["tariffs_html"] = lines(tariffs, 10)
    f["tariff_notes_html"] = lines([f'<li>{icon("check", "icon-accent")}<span>{rich(note)}</span></li>' for note in t["tariff_notes"]], 10)

    f["steps_html"] = lines([
        f'<li class="step-card reveal"><span class="step-number" aria-hidden="true">{i:02d}</span><h3>{rich(title)}</h3><p>{rich(text)}</p></li>'
        for i, (title, text) in enumerate(t["steps"], 1)], 10)
    f["facts_html"] = lines([
        f'<div><dt><span class="fact-icon">{icon(name, "icon-accent")}</span><span>{esc(label)}</span></dt><dd>{rich(value)}</dd></div>'
        for name, label, value in t["facts"]], 12)
    if "fits" in t:  # patient pages
        f["what_cards_html"] = lines([
            f'<article class="audience-card reveal"><span class="card-icon" aria-hidden="true">{icon(name)}</span><div><h3>{rich(title)}</h3><small>{rich(meta)}</small></div><p>{rich(text)}</p></article>'
            for name, title, meta, text in t["what_cards"]], 10)
        f["fits_html"] = lines([
            f'<article class="pain-card reveal"><div class="card-head"><span class="card-icon" aria-hidden="true">{icon(name)}</span></div><h3>{rich(title)}</h3><p>{rich(text)}</p></article>'
            for name, title, text in t["fits"]], 10)
        f["process_html"] = lines([
            f'<li class="step-card reveal"><span class="step-number" aria-hidden="true">{i:02d}</span><h3>{rich(title)}</h3><p>{rich(text)}</p></li>'
            for i, (title, text) in enumerate(t["process"], 1)], 10)
        f["checks_html"] = lines([f'<li>{icon("check", "icon-accent")}<span>{rich(item)}</span></li>' for item in t["checks"]], 10)
    f["faq_html"] = lines([
        f'<details class="faq-item"><summary><span>{rich(question)}</span>{icon("plus")}</summary><p>{rich(answer)}</p></details>'
        for question, answer in t["faq"]], 10)
    return f


def page_path(lang, slug=None, kind="main"):
    path = LANGS[lang]["path"]
    if kind == "patients":
        path += f"{slug}/"
    elif kind == "clinics":
        path += f"{slug}/{CLINICS_DIR}/"
    return path


def page_url(lang, slug=None, kind="main"):
    return SETTINGS["base_url"] + page_path(lang, slug, kind)


def og_name(lang, slug=None, kind="main"):
    """Social preview file of a page, drawn by build_og.py."""
    if kind == "main":
        return f"og-{lang}.jpg"
    return f"og-{slug}-{lang}.jpg" if kind == "patients" else f"og-{slug}-{CLINICS_DIR}-{lang}.jpg"


def page_copy(lang, slug=None, kind="main"):
    """The texts of one page: a direction page is the main page's copy with its own keys laid over it."""
    if kind == "main":
        return L[lang]
    return {**L[lang], **DIRECTIONS[slug][kind][lang]}


def pages():
    """(lang, slug, kind) of every page: the main page first, then each direction's patient and clinic pages."""
    return [(lang, None, "main") for lang in LANGS] + [
        (lang, slug, kind) for slug in DIRECTIONS for kind in ("patients", "clinics") for lang in LANGS]


def rel(target, current):
    """Relative link from the page at `current` to the page at `target` (both site/dental-relative paths)."""
    link = posixpath.relpath(target or ".", current or ".")
    return "./" if link == "." else link + "/"


def render_page(template, lang, slug=None, kind="main"):
    t, meta = page_copy(lang, slug, kind), LANGS[lang]
    path = page_path(lang, slug, kind)
    root = "../" * path.count("/")
    default_lang = next(iter(LANGS))
    assets = root + SETTINGS["assets"]
    og_image = urljoin(SETTINGS["base_url"], SETTINGS["assets"]) + og_name(lang, slug, kind)

    options = []
    for code, other in LANGS.items():
        active = code == lang
        current = ' aria-current="page"' if active else ""
        options.append(
            f'<a class="language-option{" active" if active else ""}" href="{esc(rel(page_path(code, slug, kind), path))}" hreflang="{code}" lang="{code}"{current}>'
            f'<svg class="language-flag" viewBox="0 0 24 16" aria-hidden="true" focusable="false"><use href="#{other["flag"]}"/></svg>'
            f'<span>{esc(other["name"])}</span></a>')

    alternates = [f'  <link rel="alternate" hreflang="{code}" href="{esc(page_url(code, slug, kind))}">' for code in LANGS]
    alternates.append(f'  <link rel="alternate" hreflang="x-default" href="{esc(page_url(default_lang, slug, kind))}">')
    og_alternates = [f'  <meta property="og:locale:alternate" content="{other["og_locale"]}">' for code, other in LANGS.items() if code != lang]

    person_id = SETTINGS["cv_url"] + "#person"
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": page_url(lang, slug, kind),
                "url": page_url(lang, slug, kind),
                "name": t["page_title"],
                "description": t["description"],
                "inLanguage": lang,
                "primaryImageOfPage": og_image,
                "about": {"@type": "Thing", "name": t["ld_topic"]},
                "audience": {"@type": "Audience", "audienceType": t["ld_audience"]},
                "author": {"@id": person_id},
                "mainEntity": {"@id": SETTINGS["product_url"] + "#app"},
            },
            {
                "@type": "WebApplication",
                "@id": SETTINGS["product_url"] + "#app",
                "name": SETTINGS["product"],
                "alternateName": t["ld_name"],
                "url": SETTINGS["product_url"],
                "description": t["og_description"],
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Web",
                "areaServed": {"@type": "Country", "name": "Uzbekistan"},
                "audience": {"@type": "Audience", "audienceType": t["ld_audience"]},
            },
            {
                "@type": "Person",
                "@id": person_id,
                "name": SETTINGS["person"],
                "url": SETTINGS["cv_url"],
                "telephone": SETTINGS["phone_e164"],
                "sameAs": [SETTINGS["linkedin"], "https://t.me/" + SETTINGS["telegram"]],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": plain(question), "acceptedAnswer": {"@type": "Answer", "text": plain(answer)}}
                    for question, answer in t["faq"]
                ],
            },
        ],
    }

    main_link = rel(meta["path"], path)  # the main page in the same language
    breadcrumb = directions = ""
    if kind == "patients":
        # A page for patients: a medical topic, not the clinic platform.
        page_ld = json_ld["@graph"][0]
        page_ld["@type"] = "MedicalWebPage"
        page_ld["about"] = {"@type": "MedicalProcedure", "name": t["ld_topic"]}
        page_ld["audience"] = {"@type": "MedicalAudience", "audienceType": t["ld_audience"]}
        del page_ld["mainEntity"]
        json_ld["@graph"].pop(1)  # the WebApplication describes the clinic product
    elif kind == "clinics":
        json_ld["@graph"][0]["breadcrumb"] = {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": plain(L[lang]["breadcrumb_label"]), "item": page_url(lang)},
                {"@type": "ListItem", "position": 2, "name": plain(t["direction_name"]), "item": page_url(lang, slug, kind)},
            ],
        }
        breadcrumb = (f'<nav class="breadcrumb" aria-label="{esc(t["breadcrumb_nav_label"])}"><a href="{esc(main_link)}">{esc(plain(L[lang]["breadcrumb_label"]))}</a>'
                      f'<span aria-hidden="true">/</span><span aria-current="page">{esc(plain(t["direction_name"]))}</span></nav>\n          ')
        # The clinic sees the page its patients will read.
        patients = DIRECTIONS[slug]["patients"][lang]
        directions = (f'<div class="directions reveal"><p class="modules-label">{esc(t["patients_link_label"])}</p><ul><li>'
                      f'<a href="{esc(rel(page_path(lang, slug, "patients"), path))}">{icon("user", "icon-accent")}<span>{esc(plain(patients["direction_name"]))}</span>'
                      f'{icon("arrow-right")}</a></li></ul></div>')
    elif DIRECTIONS:
        # The main page lists the directions' clinic pages, so each of them is one link away and gets found by crawlers.
        links = "".join(
            f'<li><a href="{esc(rel(page_path(lang, other, "clinics"), path))}">{icon("tooth", "icon-accent")}'
            f'<span>{esc(plain(DIRECTIONS[other]["clinics"][lang]["direction_name"]))}</span>{icon("arrow-right")}</a></li>' for other in DIRECTIONS)
        directions = f'<div class="directions reveal"><p class="modules-label">{esc(t["directions_label"])}</p><ul>{links}</ul></div>'

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
        "leadEndpoint": SETTINGS["lead_endpoint"],
        "metrikaId": int(metrika_id) if metrika_id else 0,
        "t": {
            "themeDark": t["theme_dark"], "themeLight": t["theme_light"],
            "submit": t["order_submit"], "sending": t["order_sending"],
            "messageTitle": t["order_message_title"], "name": t["order_name"], "phone": t["order_phone"],
            "info": t["order_message_info"],
        },
    }

    # Every string is available twice: {{key}} is plain text, {{key_html}} carries the keyword emphasis.
    context = {}
    for key, value in t.items():
        if not isinstance(value, str):
            continue
        if key.endswith("_html"):
            context[key] = rich(value, escape=False)
        else:
            context[key] = plain(value)
            context[key + "_html"] = rich(value)
    context.update(render_fragments(t))
    context.update(
        lang=lang, root=root, assets=assets, og_image=og_image, canonical=page_url(lang, slug, kind), og_locale=meta["og_locale"],
        lang_code=meta["code"], lang_name=meta["name"], lang_flag=meta["flag"],
        person=SETTINGS["person"], cv_url=SETTINGS["cv_url"], linkedin=SETTINGS["linkedin"],
        cv_link=root + "../", biz_link=root + "../business/" + meta["path"],  # every page leads to the other two
        brand_href=main_link if kind == "clinics" else "#top", breadcrumb_html=breadcrumb, directions_html=directions,
        clinics_link=rel(page_path(lang, slug, "clinics"), path) if slug else main_link,
        find_url=SETTINGS["catalog_url"], map_url=SETTINGS["map_url"],
        product=SETTINGS["product"], product_url=SETTINGS["product_url"], apply_url=SETTINGS["apply_url"],
        phone_display=SETTINGS["phone_display"], phone_e164=SETTINGS["phone_e164"],
        telegram_url="https://t.me/" + SETTINGS["telegram"], whatsapp_url="https://wa.me/" + SETTINGS["whatsapp"],
        language_options_html=lines(options, 14), alternates_html="\n".join(alternates), og_alternates_html="\n".join(og_alternates),
        json_ld_html=json.dumps(json_ld, ensure_ascii=False, indent=2).replace("</", "<\\/"),
        site_json_html=json.dumps(site, ensure_ascii=False).replace("</", "<\\/"),
        metrika_html=metrika,
    )

    # Blocks: clinic pages (main and a direction's clinic page) and patient pages differ in navigation, content,
    # footer buttons and the callback dialog; the tariffs section and its menu entry go when SETTINGS["show_tariffs"] is off.
    kept = {"patients"} if kind == "patients" else {"clinics"}
    if SETTINGS["show_tariffs"]:
        kept.add("tariffs")
    while BLOCK.search(template):
        template = BLOCK.sub(lambda block: block.group(2) if block.group(1) in kept else "", template)

    missing = sorted(set(TOKEN.findall(template)) - set(context))
    if missing:
        raise SystemExit(f"template.html uses tokens that content.py does not define ({path or lang}): {', '.join(missing)}")

    def fill(match):
        key = match.group(1)
        return context[key] if key.endswith("_html") else esc(context[key])

    page = TOKEN.sub(fill, template)
    if "[[" in page or "]]" in page.replace("]]>", ""):
        raise SystemExit(f"an unprocessed [[keyword]] marker is left in the page {path or lang}")
    return page


def visible_text(page):
    body = page.split("<main", 1)[1].split("</main>", 1)[0]
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body)))


def main():
    if set(L) != set(LANGS):
        raise SystemExit("content.py: L and LANGS must describe the same languages")
    reference = next(iter(L.values()))
    for lang, t in L.items():
        diff = set(t) ^ set(reference)
        if diff:
            raise SystemExit(f"content.py: language '{lang}' differs in keys: {', '.join(sorted(diff))}")
    for slug, direction in DIRECTIONS.items():
        if not re.fullmatch(r"[a-z0-9-]+", slug) or slug in {meta["path"].strip("/") for meta in LANGS.values()} | {"assets"}:
            raise SystemExit(f"content.py: '{slug}' cannot be a direction address")
        if set(direction) != {"keyword_stem", "patients", "clinics"} or any(set(direction[part]) != set(LANGS) for part in direction):
            raise SystemExit(f"content.py: direction '{slug}' needs keyword_stem, patients and clinics for every language")
        for lang in LANGS:
            unknown = set(direction["clinics"][lang]) - set(reference) - DIRECTION_KEYS
            missing = DIRECTION_KEYS - set(direction["clinics"][lang])
            if unknown or missing:
                raise SystemExit(f"content.py: direction '{slug}' clinics ({lang}): unknown keys {sorted(unknown)}, missing keys {sorted(missing)}")
        first = set(next(iter(direction["patients"].values())))
        for lang, copy in direction["patients"].items():
            if set(copy) != first:
                raise SystemExit(f"content.py: direction '{slug}' patients: language '{lang}' differs in keys: {', '.join(sorted(set(copy) ^ first))}")
    if not SETTINGS["base_url"].endswith("/"):
        raise SystemExit("SETTINGS['base_url'] must end with a slash")

    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as source:
        template = source.read()

    for lang, slug, kind in pages():
        target = os.path.join(OUT, page_path(lang, slug, kind), "index.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        page = render_page(template, lang, slug, kind)
        with open(target, "w", encoding="utf-8") as out:
            out.write(page)
        t = page_copy(lang, slug, kind)
        stem = DIRECTIONS[slug]["keyword_stem"][lang] if slug else KEYWORD_STEM[lang]
        mentions = visible_text(page).lower().count(stem)
        emphasised = page.count('class="kw"') + page.count('class="accent-word"')
        print(f"{lang}: {os.path.relpath(target, REPO)}  ({os.path.getsize(target) // 1024} KB) · "
              f"'{stem}…' {mentions}x in the text, {emphasised} emphasised · "
              f"title {len(t['page_title'])} / description {len(t['description'])} characters")

    today = datetime.date.today().isoformat()
    urls = ""
    for lang, slug, kind in pages():
        alternates = "".join(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{esc(page_url(code, slug, kind))}"/>\n' for code in LANGS)
        urls += f"  <url>\n    <loc>{esc(page_url(lang, slug, kind))}</loc>\n{alternates}    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n  </url>\n"
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as out:
        out.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')

    # Crawlers read robots.txt only at the host root, so the parent site's robots.txt has to list this sitemap.
    sitemap_url = SETTINGS["base_url"] + "sitemap.xml"
    if urlparse(SETTINGS["base_url"]).path != "/":
        host_robots = os.path.join(REPO, "site", "robots.txt")
        listed = os.path.isfile(host_robots) and sitemap_url in open(host_robots, encoding="utf-8").read()
        if not listed:
            print(f"note: add 'Sitemap: {sitemap_url}' to the host's root robots.txt")

    with open(os.path.join(HERE, "content.py"), encoding="utf-8") as source:
        pending = [line.split("TASDIQLANG", 1)[1].lstrip(": ").strip() for line in source if "TASDIQLANG" in line]
    pending = sorted({item for item in pending if item and not item.startswith("—")})  # the header comment explains the marker itself
    unexplained = sum(1 for line in open(os.path.join(HERE, "content.py"), encoding="utf-8") if line.rstrip().endswith("# TASDIQLANG"))
    if pending or unexplained:
        print(f"\nTASDIQLANG — tasdiqlanmagan bandlar ({len(pending)} izohli, {unexplained} izohsiz belgi):")
        for item in pending:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
