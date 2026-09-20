#!/usr/bin/env python3
"""Apelsin logotipini PWA ikonkasidan kesib, ikki mavzuga tayyorlaydi.

Manba `src/apelsin-pwa-512.png` (512x512) — apelsin.uz saytining 2021-yilgi
PWA ikonkasi (Wayback Machine nusxasi, 2021-11-16). Bank 2022-yilda Uzum Bank
nomiga o'tgan, shuning uchun rasmiy sayt endi Apelsin logotipini bermaydi;
arxivdagi yagona to'liq lokap shu ikonka ichida turibdi.

Kvadrat kanvasda lokap gorizontal markazda: chapda hamyon belgisi (0..133),
so'ng 37 px bo'shliq, o'ngda "Apelsin" wordmark (171..511). Kanvasning qolgan
qismi shaffof, shuning uchun lokap aynan (0, 189)-(512, 324) to'rtburchakdan
kesiladi — 512x135. Bu manbadagi eng katta o'lcham.

Wordmark rangi #00527d. Yorug' mavzuda (#ffffff karta foni) kontrast 8.4:1 —
o'zgarishsiz qoladi. To'q mavzuda (#0b1220 karta foni) esa atigi 2.2:1 ga
tushadi, shuning uchun wordmark oq rangga bo'yaladi (kontrast 17:1). Hamyon
belgisi ikkala mavzuda ham o'z rangida: to'q sariq #f47034 ikkala fonda
yetarlicha ajralib turadi.

Yozadi:
  site/assets/apelsin-logo-dark.png
  site/assets/apelsin-logo-light.png
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(__file__).resolve().parent / "src" / "apelsin-pwa-512.png"
OUT_DIR = ROOT / "site" / "assets"

LOCKUP = (0, 189, 512, 324)   # kvadrat kanvasdagi lokap (alfa profilidan o'lchangan)
WORD_X = 171                  # lokap ichida wordmark boshlanadigan ustun

WHITE = (255, 255, 255)

# Mavzu -> wordmark rangi (None = manbadagi #00527d saqlanadi).
THEMES = {
    "light": None,
    "dark": WHITE,
}


def paint_word(image: Image.Image, color) -> Image.Image:
    """Wordmark piksellarining RGB qismini almashtiradi, alfani tegmay qoldiradi.

    Wordmark bir tekis rangda va faqat alfa bilan silliqlangan, shuning uchun
    RGB'ni to'g'ridan-to'g'ri yozish chetlarni buzmaydi. Hamyon belgisi
    (x < WORD_X) tegilmaydi — undagi gradient va yashil barg saqlanadi."""
    if color is None:
        return image
    out = image.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(WORD_X, out.width):
            a = px[x, y][3]
            if a:
                px[x, y] = color + (a,)
    return out


def main() -> None:
    source = Image.open(SRC).convert("RGBA").crop(LOCKUP)
    for theme, color in THEMES.items():
        out = paint_word(source, color)
        path = OUT_DIR / f"apelsin-logo-{theme}.png"
        out.save(path, optimize=True)
        print(f"{path.relative_to(ROOT)} — {out.width}x{out.height}")


if __name__ == "__main__":
    main()
