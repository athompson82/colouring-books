# One-off: build a 3x3 contact sheet (rows = scenes, columns = styles) from the downloaded samples.
import sys
from PIL import Image, ImageDraw, ImageFont

D = sys.argv[1]
styles = [("A", "A - Plush athletic"), ("B", "B - Comic muscular"), ("C", "C - Hybrid mascot")]
scenes = [("05-game-face", "Game Face"), ("18-stiff-arm", "Stiff Arm"), ("06-tunnel", "Through the Tunnel")]

TW, TH, PAD, HDR, LBL = 600, 800, 24, 70, 220
W = LBL + 3 * (TW + PAD) + PAD
H = HDR + 3 * (TH + PAD) + PAD
sheet = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
except OSError:
    f = ImageFont.load_default()

for c, (_, name) in enumerate(styles):
    d.text((LBL + PAD + c * (TW + PAD), 20), name, fill="black", font=f)
for r, (key, name) in enumerate(scenes):
    y = HDR + PAD + r * (TH + PAD)
    d.text((16, y + TH // 2), name.replace(" ", "\n", 1) if len(name) > 12 else name, fill="black", font=f)
    for c, (s, _) in enumerate(styles):
        im = Image.open(f"{D}/{key}_style{s}.png").convert("RGB")
        im.thumbnail((TW, TH))
        x = LBL + PAD + c * (TW + PAD)
        sheet.paste(im, (x + (TW - im.width) // 2, y + (TH - im.height) // 2))
        d.rectangle([x - 1, y - 1, x + TW, y + TH], outline="#999999")
sheet.save(f"{D}/contact_sheet.png")
print("saved", f"{D}/contact_sheet.png", sheet.size)
