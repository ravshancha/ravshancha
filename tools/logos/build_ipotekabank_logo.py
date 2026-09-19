#!/usr/bin/env python3
"""Ipotekabank logotipini taxlangan holatdan gorizontal lokapga o'giradi.

Manba `src/ipotekabank-stacked-light.png` (2585x1797) — rasmiy taxlangan
variant: doira belgisi tepada, "ipotekabank / otp group" wordmark pastda.
Rasmda atigi ikki rang bor: to'q yashil #006538 (halqa, "ipoteka", "otp group")
va yorqin yashil #4eaf30 (ichki nuqta, "bank").

Sayt tajriba bo'limida logolar bir qatorda turadi (Kapitalbank kabi), shuning
uchun ikki qism ajratilib yonma-yon joylashtiriladi.

To'q mavzu uchun #006538 saqlanmaydi: #05070d fonda kontrasti 2.8:1 ga tushadi.
Uning o'rniga butun logo yorqin yashil (#4eaf30, kontrast 7:1) bilan chiziladi.
`src/ipotekabank-stacked-dark.png` — rasmiy oq monoxrom variant; hozir
ishlatilmaydi, zaxira sifatida turibdi.

Yozadi:
  site/assets/ipotekabank-logo-dark.png
  site/assets/ipotekabank-logo-light.png
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(__file__).resolve().parent / "src" / "ipotekabank-stacked-light.png"
OUT_DIR = ROOT / "site" / "assets"

# Manba kanvasidagi kesimlar (alfa profilidan o'lchangan).
MARK = (794, 0, 1791, 999)     # doira belgisi
WORD = (0, 1118, 2585, 1797)   # "ipotekabank" + "otp group"

MARK_HEIGHT = 240              # chiqishdagi belgi balandligi (ekranda ~45 px, 5x zaxira)
WORD_RATIO = 0.85              # wordmark balandligi belgiga nisbatan
GAP_RATIO = 0.20               # belgi va wordmark orasidagi bo'shliq

DARK_GREEN = (0, 101, 56)
BRIGHT_GREEN = (78, 175, 48)

# Mavzu -> rang almashtirish jadvali (bo'sh jadval = asl ranglar).
THEMES = {
    "light": {},
    "dark": {DARK_GREEN: BRIGHT_GREEN},
}


def recolor(image: Image.Image, mapping: dict) -> Image.Image:
    """Ranglarni almashtiradi. Manbada faqat ikki aniq rang bor, shuning uchun
    to'liq o'lchamda, resize'dan oldin bajariladi — aks holda chekka piksellar
    aralashib, aniq moslik yo'qoladi."""
    if not mapping:
        return image
    out = image.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a and (r, g, b) in mapping:
                px[x, y] = mapping[(r, g, b)] + (a,)
    return out


def lockup(image: Image.Image) -> Image.Image:
    mark = image.crop(MARK)
    word = image.crop(WORD)

    mark_w = round(mark.width * MARK_HEIGHT / mark.height)
    mark = mark.resize((mark_w, MARK_HEIGHT), Image.LANCZOS)

    word_h = round(MARK_HEIGHT * WORD_RATIO)
    word_w = round(word.width * word_h / word.height)
    word = word.resize((word_w, word_h), Image.LANCZOS)

    gap = round(MARK_HEIGHT * GAP_RATIO)
    out = Image.new("RGBA", (mark_w + gap + word_w, MARK_HEIGHT), (0, 0, 0, 0))
    out.alpha_composite(mark, (0, 0))
    out.alpha_composite(word, (mark_w + gap, (MARK_HEIGHT - word_h) // 2))
    return out


def main() -> None:
    source = Image.open(SRC).convert("RGBA")
    for theme, mapping in THEMES.items():
        out = lockup(recolor(source, mapping))
        path = OUT_DIR / f"ipotekabank-logo-{theme}.png"
        out.save(path, optimize=True)
        print(f"{path.relative_to(ROOT)} — {out.width}x{out.height}")


if __name__ == "__main__":
    main()
