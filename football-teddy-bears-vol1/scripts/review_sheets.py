# One-off: two 5x4 review contact sheets of the 40 pages, numbered.
from PIL import Image, ImageDraw, ImageFont
import sys
D = sys.argv[1]
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
TW, TH, P = 450, 600, 20
for s in range(2):
    sheet = Image.new("RGB", (5*(TW+P)+P, 4*(TH+P+40)+P), "white"); d = ImageDraw.Draw(sheet)
    for i in range(20):
        n = s*20 + i + 1; r, c = divmod(i, 5)
        x, y = P + c*(TW+P), P + r*(TH+P+40)
        im = Image.open(f"{D}/pages/p{n:02d}.png").convert("RGB").resize((TW, TH))
        sheet.paste(im, (x, y+40)); d.rectangle([x, y+40, x+TW, y+40+TH], outline="#999")
        d.text((x, y), f"p{n:02d}", fill="black", font=f)
    sheet.save(f"{D}/pages/review_{s*20+1:02d}-{s*20+20:02d}.jpg", quality=88)
