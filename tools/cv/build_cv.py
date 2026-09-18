# -*- coding: utf-8 -*-
# Builds site/cv/Ravshanjon-Ismoilov-CV-{uz,ru,en}.pdf from cv_data.py.
# Requires: python3 -m pip install reportlab   (fonts: macOS Arial in /System/Library/Fonts/Supplemental)
# Usage:    python3 tools/cv/build_cv.py [output-dir]
import io, os, sys, html, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, HRFlowable, KeepTogether, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cv_data import L, CERTS, CONTACT, NAME
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, "..", "..", "site", "cv"))
os.makedirs(OUT, exist_ok=True)

FD = "/System/Library/Fonts/Supplemental"
pdfmetrics.registerFont(TTFont("Arial", f"{FD}/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", f"{FD}/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", f"{FD}/Arial Italic.ttf"))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", f"{FD}/Arial Bold Italic.ttf"))
registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")

ACCENT = colors.HexColor("#095fd8"); TEXT = colors.HexColor("#1b2430"); MUTED = colors.HexColor("#55606b"); LINE = colors.HexColor("#d9e2ee"); GRAY = colors.HexColor("#8a939d")
base = ParagraphStyle("base", fontName="Arial", fontSize=9.3, leading=12.8, textColor=TEXT)
S = dict(
    name=ParagraphStyle("name", parent=base, fontName="Arial-Bold", fontSize=21, leading=24),
    title=ParagraphStyle("title", parent=base, fontName="Arial-Bold", fontSize=11, leading=14, textColor=ACCENT, spaceBefore=2),
    contacts=ParagraphStyle("contacts", parent=base, fontSize=8.3, leading=11.8, textColor=MUTED, alignment=TA_RIGHT),
    h2=ParagraphStyle("h2", parent=base, fontName="Arial-Bold", fontSize=8.5, leading=11, textColor=ACCENT, spaceBefore=8),
    body=base,
    jobhead=ParagraphStyle("jobhead", parent=base, fontSize=9.7, leading=13),
    period=ParagraphStyle("period", parent=base, fontSize=8.5, leading=13, textColor=MUTED, alignment=TA_RIGHT),
    loc=ParagraphStyle("loc", parent=base, fontSize=8.3, leading=10.5, textColor=GRAY),
    blockhead=ParagraphStyle("blockhead", parent=base, fontName="Arial-Bold", fontSize=9.1, leading=12.3, spaceBefore=2),
    bullet=ParagraphStyle("bullet", parent=base, fontSize=9.0, leading=12.1, leftIndent=10, bulletIndent=1, spaceAfter=0.6),
    tech=ParagraphStyle("tech", parent=base, fontSize=8.3, leading=10.8, textColor=MUTED, spaceBefore=1),
    muted=ParagraphStyle("muted", parent=base, fontSize=8.5, leading=11.3, textColor=MUTED),
)
W = A4[0] - 26 * mm

def esc(s): return html.escape(s, quote=False)
def rich(s):  # plain text with optional <i>tech</i> tail
    parts = re.split(r"<i>(.*?)</i>", s)
    out = []
    for i, p in enumerate(parts):
        out.append(f'<font size="8.3" color="#55606b">{esc(p)}</font>' if i % 2 else esc(p))
    return "".join(out)
def h2(label, first=None, keep=True):
    items = [Paragraph(esc(label).upper(), S["h2"]), HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=1.5, spaceAfter=3.5)]
    items = items + ([first] if first else [])
    return KeepTogether(items) if keep else items
def nopad(t, extra=()):
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)] + list(extra)))
    return t

def build(lang):
    d = L[lang]; lb = d["labels"]; c = CONTACT
    story = []
    left = [Paragraph(esc(NAME), S["name"]), Paragraph(esc(d["title"]), S["title"])]
    right = [Paragraph(f'{esc(d["location"])} · <a href="tel:+998999420770">{c["phone"]}</a><br/>'
                       f'<a href="mailto:{c["email"]}">{c["email"]}</a> · <a href="https://{c["tg"]}">{c["tg"]}</a><br/>'
                       f'<a href="https://{c["site"]}">{c["site"]}</a> · <a href="https://{c["li"]}">{c["li"]}</a> · <a href="https://{c["gh"]}">{c["gh"]}</a>', S["contacts"])]
    story.append(nopad(Table([[left, right]], colWidths=[W * 0.42, W * 0.58]), [("VALIGN", (0, 0), (-1, -1), "BOTTOM")]))
    story.append(HRFlowable(width="100%", thickness=1.6, color=ACCENT, spaceBefore=5, spaceAfter=2))
    story.append(h2(lb["summary"], Paragraph(esc(d["summary"]), S["body"])))
    jobs = []
    prefix = h2(lb["exp"], keep=False)          # section heading travels with the first job (no nested KeepTogether)
    for j in d["jobs"]:
        head = nopad(Table([[Paragraph(f'<b>{esc(j["co"])}</b> · <font color="#095fd8"><b>{esc(j["role"])}</b></font>', S["jobhead"]), Paragraph(esc(j["period"]), S["period"])]], colWidths=[W - 56 * mm, 56 * mm]))
        block = prefix + [head, Paragraph(esc(j["loc"]), S["loc"])]; prefix = []
        first = True
        for b in j["blocks"]:
            items = []
            if b.get("head"): items.append(Paragraph(esc(b["head"]), S["blockhead"]))
            items += [Paragraph(rich(x), S["bullet"], bulletText="•") for x in b["bullets"]]
            if b.get("tech"): items.append(Paragraph(f'<b>{esc(lb["tech"])}:</b> {esc(b["tech"])}', S["tech"]))
            if first:
                block = [KeepTogether(block + items[:2])] + items[2:]; first = False
            else:
                block += items
        jobs += block + [Spacer(1, 5)]
    story += jobs
    colL = h2(lb["edu"], keep=False) + [Paragraph(f'<b>{esc(a)}</b><br/>{esc(b)}<br/><font color="#55606b" size="8.5">{esc(y)}</font>', S["body"]) for a, b, y in d["edu"]]
    colL += h2(lb["langs"], Paragraph(" · ".join(esc(x) for x in d["langs"]), S["body"]), keep=False) + h2(lb["format"], Paragraph(esc(d["workformat"]), S["body"]), keep=False) + h2(lb["qualities"], Paragraph(esc(d["qualities"]), S["body"]), keep=False)
    certs = sorted(CERTS + d["certs_extra"], key=lambda t: t[0], reverse=True)
    colR = h2(lb["skills"], keep=False) + [Paragraph(f'<b>{esc(a)}:</b> {esc(b)}', S["body"]) for a, b in d["skills"]]
    colR += h2(lb["certs"], keep=False) + [Paragraph(f'<b>{esc(y)} · {esc(o)}</b> — {esc(t)}', S["body"]) for y, o, t in certs]
    story.append(nopad(Table([[colL, colR]], colWidths=[W / 2, W / 2]), [("RIGHTPADDING", (0, 0), (0, 0), 9), ("LEFTPADDING", (1, 0), (1, 0), 9)]))
    def footer(canvas, doc):
        canvas.saveState(); canvas.setFont("Arial", 7.6); canvas.setFillColor(GRAY)
        canvas.drawString(13 * mm, 8 * mm, f"{NAME} · CV"); canvas.drawRightString(A4[0] - 13 * mm, 8 * mm, f"{d['updated']} · {doc.page}"); canvas.restoreState()
    pdf = os.path.join(OUT, f"Ravshanjon-Ismoilov-CV-{lang}.pdf")
    doc = SimpleDocTemplate(pdf, pagesize=A4, leftMargin=13 * mm, rightMargin=13 * mm, topMargin=12 * mm, bottomMargin=14 * mm, title=f"{NAME} — CV", author=NAME, subject=d["title"], lang=lang)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"{lang}: {os.path.basename(pdf)} pages={doc.page} size={os.path.getsize(pdf)//1024} KB")

for lang in ["uz", "ru", "en"]: build(lang)
