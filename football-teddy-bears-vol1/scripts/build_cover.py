# One-off: build the KDP paperback wrap cover (back | spine | front) with 0.125 in bleed.
# Usage: python3 scripts/build_cover.py . <front_art.png>
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

D, FRONT = sys.argv[1], sys.argv[2]
DPI = 300
PAGES = 84
SPINE = PAGES * 0.002252          # KDP white paper, B&W
BLEED, TW, TH = 0.125, 8.5, 11.0
W_IN, H_IN = 2 * BLEED + 2 * TW + SPINE, TH + 2 * BLEED
W, H = round(W_IN * DPI), round(H_IN * DPI)
px = lambda inches: round(inches * DPI)

NAVY = (16, 28, 58); GOLD = (244, 186, 40); WHITE = (255, 255, 255)
fB = lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", s)
fR = lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# Front panel (spine edge -> right bleed edge): cover-fit the art.
fx0 = px(BLEED + TW + SPINE)
fw, fh = W - fx0, H
# Art sits inside a navy frame (margin m on top/sides of the trim) with a bottom band for the imprint.
art = Image.open(FRONT).convert("RGB")
band = 0.8
m = (TW - (art.width / art.height) * (TH - band)) / (2 - art.width / art.height)  # equal top/side margins
aw, ah = TW - 2 * m, TH - m - band
art = art.resize((px(aw), px(ah)), Image.LANCZOS)
ax, ay = fx0 + px(m), px(BLEED + m)
d.rectangle([ax - 14, ay - 14, ax + art.width + 14, ay + art.height + 14], fill=GOLD)
img.paste(art, (ax, ay))
t = "CEDAR & INK PRESS"
f = fB(72); tw_ = d.textlength(t, font=f)
d.text((fx0 + (px(TW) - tw_) / 2, ay + art.height + px((band - 0.25) / 2)), t, font=f, fill=WHITE)

# Spine: plain navy (too thin for text at 84 pages).

# Back panel (left bleed edge -> spine edge).
bx0, bw = 0, px(BLEED + TW)
L = px(BLEED + 0.6)  # left text margin
d.text((L, px(BLEED + 0.6)), "40 GAME-DAY PAGES", font=fB(92), fill=GOLD)
d.text((L, px(BLEED + 1.05)), "TO COLOR", font=fB(92), fill=GOLD)
blurb = ["Tough, athletic teddy bears in real football action,",
         "from the locker room to the end zone.",
         "",
         "• 40 original illustrations for teens & adults",
         "• Quarterbacks, linemen, defenders, huddles & touchdowns",
         "• Single-sided pages – no bleed-through worries",
         "• Large 8.5 x 11 in format with bold, clean line art"]
for i, line in enumerate(blurb):
    d.text((L, px(BLEED + 1.75) + i * 62), line, font=fR(44), fill=WHITE)

# One row of three sample thumbnails.
thumbs = ["p06", "p18", "p38"]
tw_in, th_in, gap = 2.4, 3.2, 0.25
gx0 = BLEED + (TW - (3 * tw_in + 2 * gap)) / 2
gy0 = BLEED + 4.3
for i, n in enumerate(thumbs):
    x, y = px(gx0 + i * (tw_in + gap)), px(gy0)
    th = Image.open(f"{D}/pages/{n}.png").convert("RGB").resize((px(tw_in), px(th_in)), Image.LANCZOS)
    d.rectangle([x - 12, y - 12, x + px(tw_in) + 12, y + px(th_in) + 12], fill=WHITE)
    img.paste(th, (x, y))
# Barcode zone (KDP adds it): 2 x 1.2 in, 0.25 in from spine edge and bottom trim. Keep empty.
bz = [px(BLEED + TW - 0.25 - 2.0), px(BLEED + TH - 0.25 - 1.2), px(BLEED + TW - 0.25), px(BLEED + TH - 0.25)]
assert gy0 + th_in < BLEED + TH - 0.25 - 1.2, "thumbnails overlap barcode zone"
d.text((L, H - px(BLEED + 0.7)), "CEDAR & INK PRESS", font=fB(44), fill=GOLD)

out_png = f"{D}/output/cover_wrap.png"
img.save(out_png)
# Preview with trim/spine/barcode guides (not for upload).
g = img.copy(); gd = ImageDraw.Draw(g)
for x in [px(BLEED), px(BLEED + TW), px(BLEED + TW + SPINE), W - px(BLEED)]:
    gd.line([x, 0, x, H], fill=(0, 255, 255), width=4)
for y in [px(BLEED), H - px(BLEED)]:
    gd.line([0, y, W, y], fill=(0, 255, 255), width=4)
gd.rectangle(bz, outline=(255, 0, 255), width=6)
g.resize((W // 4, H // 4)).save(f"{D}/output/cover_preview_with_guides.jpg", quality=85)

c = canvas.Canvas(f"{D}/output/cover_wrap.pdf", pagesize=(W_IN * inch, H_IN * inch))
c.drawImage(out_png, 0, 0, W_IN * inch, H_IN * inch)
c.save()
print(f"cover {W_IN:.4f} x {H_IN:.3f} in ({W}x{H}px), spine {SPINE:.4f} in, barcode zone px {bz}")
