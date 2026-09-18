# CV generator

`cv_data.py` holds the CV content in Uzbek, Russian and English; `build_cv.py` renders it to `site/cv/Ravshanjon-Ismoilov-CV-{uz,ru,en}.pdf` with reportlab (A4, Arial).

```bash
python3 -m pip install reportlab
python3 tools/cv/build_cv.py          # writes into site/cv/
```

The site header's "CV" button links to the PDF of the currently selected language. After editing the content, rebuild and commit the PDFs together with the data file.
