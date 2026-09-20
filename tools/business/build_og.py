#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Draws the social preview images of the selling site (what Telegram, Facebook or LinkedIn show for a shared link):
# site/business/assets/og-{uz,ru}.jpg, 1200x630. Text comes from content.py (og_lines, og_sub).
# Requires: python3 -m pip install pillow   (fonts: macOS Arial in /System/Library/Fonts/Supplemental)
# Usage:    python3 tools/business/build_og.py
# Rerun it when the portrait or the texts change. Social networks cache previews, so after a change ask
# Telegram's @WebpageBot to refresh the link.
import os, sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import L, SETTINGS

ASSETS = os.path.normpath(os.path.join(HERE, "..", "..", "site", "business", "assets"))
FONTS = "/System/Library/Fonts/Supplemental"
W, H = 1200, 630
LEFT, TEXT_WIDTH = 66, 600
WHITE, ACCENT, MUTED, LINK = (243, 246, 249), (98, 214, 255), (170, 181, 196), (74, 144, 255)


def font(size, bold=True):
    return ImageFont.truetype(os.path.join(FONTS, "Arial Bold.ttf" if bold else "Arial.ttf"), size)


def glow(center, radius, color, strength):
    layer = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(layer).ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55))
    return layer.point(lambda value: int(value * strength))


def background():
    image = Image.new("RGB", (W, H), (5, 7, 13))
    image = ImageChops.add(image, glow((930, 250), 360, (30, 96, 220), 0.95))
    return ImageChops.add(image, glow((150, 40), 260, (0, 140, 200), 0.22))


def monogram(size):
    # The "C" mark of logo-mark-dark.svg (120-unit box: arc r=40 width 16, dot r=10.5), drawn 4x and scaled down.
    scale = size * 4 / 120
    layer = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    box = [(60 - 48) * scale, (60 - 48) * scale, (60 + 48) * scale, (60 + 48) * scale]
    draw.arc(box, start=35.4, end=315, fill=(255, 255, 255, 255), width=int(16 * scale))
    draw.ellipse([(98 - 10.5) * scale, (57.5 - 10.5) * scale, (98 + 10.5) * scale, (57.5 + 10.5) * scale], fill=(255, 255, 255, 255))
    return layer.resize((size, size), Image.LANCZOS)


def portrait(height):
    source = Image.open(os.path.join(ASSETS, "portrait.webp")).convert("RGBA")
    source = source.crop(source.getchannel("A").getbbox()).transpose(Image.FLIP_LEFT_RIGHT)  # mirrored, as in the site hero
    return source.resize((round(source.width * height / source.height), height), Image.LANCZOS)


def draw_tracked(draw, xy, text, fnt, fill, tracking):
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + tracking


def build(lang):
    t = L[lang]
    image = background()
    draw = ImageDraw.Draw(image)

    figure = portrait(600)
    image.paste(figure, (W - figure.width - 40, H - figure.height), figure)

    mark = monogram(58)
    image.paste(mark, (LEFT, 58), mark)
    draw_tracked(draw, (LEFT + 72, 66), "RAVSHANJON", font(21), WHITE, 1.6)
    draw_tracked(draw, (LEFT + 72, 93), "ISMOILOV", font(15), WHITE, 4.2)

    size = 74
    while max(draw.textlength(text, font=font(size)) for text, _ in t["og_lines"]) > TEXT_WIDTH:
        size -= 2
    y = 186
    for text, accent in t["og_lines"]:
        draw.text((LEFT, y), text, font=font(size), fill=ACCENT if accent else WHITE)
        y += round(size * 1.12)

    y += 22
    for text in t["og_sub"]:
        draw.text((LEFT, y), text, font=font(27, bold=False), fill=MUTED)
        y += 40

    address = SETTINGS["base_url"].split("://", 1)[1].rstrip("/")
    draw.text((LEFT, H - 78), address, font=font(27, bold=False), fill=LINK)

    target = os.path.join(ASSETS, f"og-{lang}.jpg")
    image.save(target, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"{lang}: site/business/assets/og-{lang}.jpg  ({os.path.getsize(target) // 1024} KB, headline {size}px)")


if __name__ == "__main__":
    for language in L:
        build(language)
