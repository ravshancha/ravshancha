#!/usr/bin/env python3
"""Sayt ikonkalarini SVG qilib chizadi va eksport qiladi.

Chizmalar 24 birlikli panjarada yozilgan, chiqish esa 64x64 (eski PNG kanvasiga mos):
art 12..52 oralig'ida (40 px optik quti), chiziq qalinligi 3 px — bu qiymatlar
`assets/icons/slicons/static/` dagi originallardan o'lchab olingan.

Yozadi:
  site/assets/icons/ui/<name>.svg  — har biri alohida 64x64 SVG
  site/assets/icons/ui/sprite.svg  — barchasi <symbol> ko'rinishida
  index.html ichiga qo'yiladigan sprite matni stdout'ga chiqadi (--print)
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "site" / "assets" / "icons" / "ui"

# 64 px kanvas ichida art 40 px quti (12..52), chiziq 3 px.
SCALE = 40 / 24  # 1.666667
OFFSET = 12
STROKE = 3 / SCALE  # 24-panjaradagi ekvivalent qalinlik = 1.8

# name -> (eski PNG, 24-panjaradagi chizma)
ICONS = {
    "sun": (
        "slicon-r10-c08",
        '<circle cx="12" cy="12" r="4.5"/>'
        '<path d="M12 1.8V5M12 19v3.2M22.2 12H19M5 12H1.8'
        'M19.2 4.8l-2.3 2.3M7.1 16.9l-2.3 2.3M19.2 19.2l-2.3-2.3M7.1 7.1L4.8 4.8"/>',
    ),
    "moon": (
        "slicon-r10-c09",
        '<path d="M20.6 14.3A9.3 9.3 0 1 1 9.7 3.4 7.3 7.3 0 0 0 20.6 14.3z"/>',
    ),
    "chevron-down": (
        "slicon-r05-c03",
        '<path d="M2.4 8.4L12 18l9.6-9.6"/>',
    ),
    "arrow-right": (
        "slicon-r05-c08",
        '<path d="M2.4 12h19.2M13.4 3.8L21.6 12l-8.2 8.2"/>',
    ),
    "arrow-up": (
        "slicon-r05-c09",
        '<path d="M12 21.6V2.4M3.8 10.6L12 2.4l8.2 8.2"/>',
    ),
    "linkedin": (
        "slicon-r17-c06",
        '<path d="M7.3 10.2V20"/><path d="M7.3 5.6v.1"/>'
        '<path d="M13.4 20v-9.8M13.4 14.1a3.6 3.6 0 0 1 7.2 0V20"/>',
    ),
    "twitter": (
        "slicon-r17-c04",
        '<path d="M22.4 4.1a8.6 8.6 0 0 1-2.6 1.3 4.1 4.1 0 0 0-7.1 2.8v.9'
        'A9.9 9.9 0 0 1 4.3 5.1s-3.7 8.3 4.6 12a10.7 10.7 0 0 1-6.5 1.8'
        'c8.3 4.6 18.4 0 18.4-10.6a4.1 4.1 0 0 0-.1-.8 7.1 7.1 0 0 0 1.7-3.4z"/>',
    ),
    "telegram": (
        "slicon-r02-c10",
        '<path d="M3.5 4.4a1.2 1.2 0 0 0-1.7 1.5l2 5.4a1.2 1.2 0 0 1 0 .8l-2 5.4'
        'a1.2 1.2 0 0 0 1.7 1.5l17.6-7.2a1.2 1.2 0 0 0 0-2.2z"/>'
        '<path d="M4.4 12h7.2"/>',
    ),
    "phone": (
        "slicon-r12-c10",
        '<path d="M21.6 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6'
        'A19.8 19.8 0 0 1 1.7 4.1 2 2 0 0 1 3.7 2h3a2 2 0 0 1 2 1.7 12.8 12.8 0 0 0 .7 2.8'
        ' 2 2 0 0 1-.5 2.1L7.7 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4 12.8 12.8 0 0 0 2.8.7'
        ' 2 2 0 0 1 1.7 2z"/>',
    ),
    "facebook": (
        "slicon-r17-c08",
        '<path d="M16 3.4h-1.6a4.4 4.4 0 0 0-4.4 4.4v12.8"/>'
        '<path d="M6.2 10.6h8.6"/>',
    ),
    "youtube": (
        "slicon-r17-c07",
        '<rect x="1.9" y="5.6" width="20.2" height="12.8" rx="4"/>'
        '<path d="M10.2 9.2l5.4 2.8-5.4 2.8z"/>',
    ),
    "code": (
        "slicon-r14-c04",
        '<path d="M16.4 6.2L21.6 12l-5.2 5.8M7.6 6.2L2.4 12l5.2 5.8M13.8 3.6l-3.6 16.8"/>',
    ),
    "bank": (
        "slicon-r08-c01",
        '<path d="M2.4 9.6L12 3.6l9.6 6z"/><path d="M3.6 12.4h16.8"/>'
        '<path d="M6.6 12.9v5.8M12 12.9v5.8M17.4 12.9v5.8"/><path d="M2.4 20.4h19.2"/>',
    ),
    "team": (
        "slicon-r07-c10",
        '<path d="M15.4 20.6v-2a4 4 0 0 0-4-4H5.9a4 4 0 0 0-4 4v2"/>'
        '<circle cx="8.7" cy="6.8" r="3.6"/>'
        '<path d="M22.1 20.6v-2a4 4 0 0 0-3-3.9M15.9 3.5a3.6 3.6 0 0 1 0 6.9"/>',
    ),
    "clock": (
        "slicon-r13-c06",
        '<circle cx="12" cy="12" r="9.8"/><path d="M12 6.2V12l3.9 2.4"/>',
    ),
    "link": (
        "slicon-r04-c04",
        '<path d="M10.2 13.2a4.8 4.8 0 0 0 7.2.5l2.4-2.4a4.8 4.8 0 0 0-6.8-6.8l-1.4 1.4"/>'
        '<path d="M13.8 10.8a4.8 4.8 0 0 0-7.2-.5l-2.4 2.4a4.8 4.8 0 0 0 6.8 6.8l1.4-1.4"/>',
    ),
    "download": (
        "slicon-r03-c08",
        '<path d="M21.6 15.4v4a2.2 2.2 0 0 1-2.2 2.2H4.6a2.2 2.2 0 0 1-2.2-2.2v-4"/>'
        '<path d="M6.8 10.2L12 15.4l5.2-5.2"/><path d="M12 15.4V2.4"/>',
    ),
    "diamond": (
        "—",
        '<path d="M12 2.4L21.6 12 12 21.6 2.4 12z"/>',
    ),
    "mobile": (
        "—",
        '<rect x="6" y="1.8" width="12" height="20.4" rx="2.8"/>'
        '<path d="M10.2 18.8h3.6"/>',
    ),
    "arrow-up-right": (
        "—",
        '<path d="M5.4 18.6L18.6 5.4"/><path d="M8.4 5.4h10.2v10.2"/>',
    ),
    "external": (
        "slicon-r03-c03",
        '<path d="M18.2 13.4v6a2.2 2.2 0 0 1-2.2 2.2H4.8a2.2 2.2 0 0 1-2.2-2.2V8.2'
        'A2.2 2.2 0 0 1 4.8 6h6"/><path d="M15 2.4h6.6V9"/><path d="M10.2 13.8L21.6 2.4"/>',
    ),
}

GROUP_OPEN = (
    f'<g transform="translate({OFFSET} {OFFSET}) scale({SCALE:.6f})" fill="none" '
    f'stroke="currentColor" stroke-width="{STROKE:.2f}" stroke-linecap="round" '
    f'stroke-linejoin="round">'
)


def standalone(body: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">'
        f"{GROUP_OPEN}{body}</g></svg>\n"
    )


def build() -> str:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    symbols = []
    for name, (origin, body) in ICONS.items():
        (OUT_DIR / f"{name}.svg").write_text(standalone(body), encoding="utf-8")
        symbols.append(
            f'<symbol id="icon-{name}" viewBox="0 0 64 64">{GROUP_OPEN}{body}</g></symbol>'
        )

    sprite_symbols = "\n".join(symbols)
    (OUT_DIR / "sprite.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg">\n' + sprite_symbols + "\n</svg>\n",
        encoding="utf-8",
    )
    (OUT_DIR / "README.md").write_text(
        "# Sayt ikonkalari (SVG)\n\n"
        "- Manba: `tools/icons/build_icons.py` (chizmalar shu yerda, qo'lda tahrirlanadi)\n"
        f"- Soni: {len(ICONS)} ta\n"
        "- Kanvas: 64 x 64, art 12..52 (40 px optik quti), chiziq 3 px\n"
        "- Rang: `currentColor` — CSS'dagi `color` ni oladi, filter kerak emas\n"
        "- `index.html` ichiga sprite inline joylangan (`#icon-<name>`), bu fayllar zaxira/qayta ishlatish uchun\n\n"
        "Yangilash: `python3 tools/icons/build_icons.py --print` va chiqqan sprite'ni "
        "`index.html` dagi `<svg class=\"icon-sprite\">` blokiga qo'yish.\n",
        encoding="utf-8",
    )
    return sprite_symbols


if __name__ == "__main__":
    sprite = build()
    print(f"{len(ICONS)} ta ikonka yozildi -> {OUT_DIR}", file=sys.stderr)
    if "--print" in sys.argv:
        print(sprite)
