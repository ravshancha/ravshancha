#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Draws the social preview images of the dentistry page (what Telegram, Facebook or LinkedIn show for a shared link):
# site/dental/assets/og-{uz,ru}.jpg, og-<direction>-{uz,ru}.jpg (patients) and og-<direction>-klinikalar-{uz,ru}.jpg, 1200x630. Text comes from content.py (og_lines, og_sub).
# Requires: python3 -m pip install pillow   (fonts: macOS Arial, or Liberation Sans — its metric twin — on Linux)
# Usage:    python3 tools/dental/build_og.py [main|<direction> ...]   (no arguments: every page; a direction = both its pages)
# Rerun it when the portrait, the product logo or the texts change. Social networks cache previews, so after a change
# ask Telegram's @WebpageBot to refresh the link.
import os, sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_site import og_name, page_copy, page_url, pages
from content import DIRECTIONS, SETTINGS

ASSETS = os.path.normpath(os.path.join(HERE, "..", "..", "site", "dental", "assets"))
FONT_FILES = [
    ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"),
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"),
]
FONTS = next((pair for pair in FONT_FILES if all(os.path.isfile(path) for path in pair)), None)
W, H = 1200, 630
LEFT, TEXT_WIDTH = 66, 640
WHITE, SOFT, MUTED, MARK = (255, 255, 255), (222, 233, 255), (190, 211, 250), (74, 140, 240)


def font(size, bold=True):
    if not FONTS:
        raise SystemExit("build_og.py: neither Arial nor Liberation Sans is installed")
    return ImageFont.truetype(FONTS[0] if bold else FONTS[1], size)


def background():
    # Dental Navigator blue, darker towards the text side, with a soft light behind the portrait.
    top, bottom = (9, 40, 104), (21, 96, 200)
    column = Image.new("RGB", (1, H))
    for y in range(H):
        ratio = y / (H - 1)
        column.putpixel((0, y), tuple(round(a + (b - a) * ratio) for a, b in zip(top, bottom)))
    image = column.resize((W, H))
    layer = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(layer).ellipse([930 - 330, 260 - 330, 930 + 330, 260 + 330], fill=(74, 140, 240))
    return ImageChops.add(image, layer.filter(ImageFilter.GaussianBlur(170)).point(lambda value: int(value * 0.6)))


def portrait(height):
    source = Image.open(os.path.join(ASSETS, "portrait.webp")).convert("RGBA")
    source = source.crop(source.getchannel("A").getbbox()).transpose(Image.FLIP_LEFT_RIGHT)  # mirrored, as in the page hero
    return source.resize((round(source.width * height / source.height), height), Image.LANCZOS)


def product_logo(height):
    source = Image.open(os.path.join(ASSETS, "product-logo.png")).convert("RGBA")
    return source.resize((round(source.width * height / source.height), height), Image.LANCZOS)


def draw_tracked(draw, xy, text, fnt, fill, tracking):
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + tracking


def build(lang, slug=None, kind="main"):
    t = page_copy(lang, slug, kind)
    image = background()
    draw = ImageDraw.Draw(image)

    if kind == "patients":  # patients see the product mark, not the person who sells it to clinics
        mark = product_logo(380)
        image.paste(mark, (930 - mark.width // 2, H // 2 - mark.height // 2), mark)
    else:
        figure = portrait(600)
        image.paste(figure, (W - figure.width - 40, H - figure.height), figure)

    # The product mark sits on a white tile: the glossy blue tooth would sink into the blue background.
    logo = product_logo(56)
    draw.rounded_rectangle([LEFT, 52, LEFT + 76, 52 + 76], radius=18, fill=WHITE)
    image.paste(logo, (LEFT + (76 - logo.width) // 2, 52 + (76 - logo.height) // 2), logo)
    draw_tracked(draw, (LEFT + 94, 62), SETTINGS["product"].upper(), font(23), WHITE, 1.8)
    draw.text((LEFT + 94, 94), SETTINGS["person"], font=font(19, bold=False), fill=MUTED)

    size = 74
    while max(draw.textlength(text, font=font(size)) for text, _ in t["og_lines"]) > TEXT_WIDTH:
        size -= 2
    y = 190
    for text, accent in t["og_lines"]:
        if accent:  # the niche word gets the same marker underline as on the page
            width = draw.textlength(text, font=font(size))
            draw.rounded_rectangle([LEFT - 4, y + round(size * 0.78), LEFT + width + 4, y + round(size * 1.06)], radius=6, fill=MARK)
        draw.text((LEFT, y), text, font=font(size), fill=WHITE if accent else SOFT)
        y += round(size * 1.14)

    y += 20
    for text in t["og_sub"]:
        draw.text((LEFT, y), text, font=font(27, bold=False), fill=MUTED)
        y += 40

    address = page_url(lang, slug, kind).split("://", 1)[1].rstrip("/")
    draw.text((LEFT, H - 78), address, font=font(27, bold=False), fill=SOFT)

    target = os.path.join(ASSETS, og_name(lang, slug, kind))
    image.save(target, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"{lang}: site/dental/assets/{og_name(lang, slug, kind)}  ({os.path.getsize(target) // 1024} KB, headline {size}px)")


if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    unknown = wanted - set(DIRECTIONS) - {"main"}
    if unknown:
        raise SystemExit(f"build_og.py: unknown pages: {', '.join(sorted(unknown))}")
    for language, direction, kind in pages():
        if not wanted or (direction or "main") in wanted:
            build(language, direction, kind)
