# Build the KDP interior PDF (8.5 x 11 in, no bleed, single-sided pages).
# Layout: title, copyright, "belongs to", colour test, then 40 x (illustration on right page + blank back) = 84 pages.
import os, sys
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

import json
D = sys.argv[1]
C = json.load(open(f"{D}/book.json"))
OUT = f"{D}/output/interior_8.5x11.pdf"
os.makedirs(f"{D}/output", exist_ok=True)
os.makedirs(f"{D}/output/print_pages", exist_ok=True)
pdfmetrics.registerFont(TTFont("Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Reg", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))

W, H = 8.5 * inch, 11 * inch
c = canvas.Canvas(OUT, pagesize=(W, H))
c.setTitle(C["title"] + ": " + C["subtitle"])

def centred(text, y, font, size):
    c.setFont(font, size); c.drawCentredString(W / 2, y, text)

# 1. Title page
centred(C["title"].upper(), H - 2.0 * inch, "Bold", 34)
centred(C["subtitle"].upper(), H - 2.6 * inch, "Bold", 24)
centred(C["tagline"], H - 3.1 * inch, "Reg", 14)
ref = Image.open(f"{D}/" + C["title_page_image"]).convert("L")
c.drawImage(ImageReader(ref), (W - 4.5 * inch) / 2, 1.6 * inch, 4.5 * inch, 6.0 * inch)
centred("Volume 1", 1.0 * inch, "Reg", 12)
c.showPage()

# 2. Copyright page
c.setFont("Reg", 10)
lines = [C["title"] + ": " + C["subtitle"] + " (Volume 1)", "",
         "Copyright © 2026. All rights reserved.", "",
         "No part of this book may be reproduced or distributed in any form",
         "without prior written permission, except for personal use of the pages.", "",
         "All characters, teams and uniforms in this book are fictional.",
         "This book is not affiliated with or endorsed by any league, team or brand."]
for i, t in enumerate(lines):
    c.drawCentredString(W / 2, 3.0 * inch - i * 14, t)
c.showPage()

# 3. "This book belongs to"
centred("THIS BOOK BELONGS TO", H / 2 + 0.6 * inch, "Bold", 26)
c.setLineWidth(2); c.line(1.5 * inch, H / 2 - 0.4 * inch, W - 1.5 * inch, H / 2 - 0.4 * inch)
c.showPage()

# 4. Colour test page
centred("TEST YOUR COLORS", H - 1.3 * inch, "Bold", 24)
centred("Try your markers and pencils here before you start.", H - 1.75 * inch, "Reg", 12)
c.setLineWidth(1.5)
cols, rows, bw, bh, gap = 4, 6, 1.5 * inch, 1.1 * inch, 0.25 * inch
x0 = (W - (cols * bw + (cols - 1) * gap)) / 2
for r in range(rows):
    for k in range(cols):
        c.roundRect(x0 + k * (bw + gap), H - 2.4 * inch - (r + 1) * bh - r * gap, bw, bh, 10)
c.showPage()

# 5-84. Illustrations on right-hand pages, blank backs.
# Art box: 10 in tall x 7.467 in wide (keeps the 3:4 art ratio), centred, >= 0.5 in from every edge.
AH = 10 * inch; AW = AH * 1792 / 2400
for n in range(1, 41):
    im = Image.open(f"{D}/pages/p{n:02d}.png").convert("L").resize((2240, 3000), Image.LANCZOS)
    path = f"{D}/output/print_pages/p{n:02d}_300dpi.jpg"
    im.save(path, quality=92, subsampling=0)
    c.drawImage(path, (W - AW) / 2, (H - AH) / 2, AW, AH)
    c.showPage()
    c.showPage()  # blank back

c.save()
print("pages:", c.getPageNumber() - 1, "->", OUT)
