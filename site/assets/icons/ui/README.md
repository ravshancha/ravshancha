# Sayt ikonkalari (SVG)

- Manba: `tools/icons/build_icons.py` (chizmalar shu yerda, qo'lda tahrirlanadi)
- Soni: 21 ta
- Kanvas: 64 x 64, art 12..52 (40 px optik quti), chiziq 3 px
- Rang: `currentColor` — CSS'dagi `color` ni oladi, filter kerak emas
- `index.html` ichiga sprite inline joylangan (`#icon-<name>`), bu fayllar zaxira/qayta ishlatish uchun

Yangilash: `python3 tools/icons/build_icons.py --print` va chiqqan sprite'ni `index.html` dagi `<svg class="icon-sprite">` blokiga qo'yish.
