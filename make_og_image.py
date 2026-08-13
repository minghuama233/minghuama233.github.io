"""Generate a 1200x630 Open Graph / Twitter share image."""
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1200, 630
FONTS = r"C:\Windows\Fonts"


def font(name, size):
    return ImageFont.truetype(rf"{FONTS}\{name}", size)


# --- Background: vertical gradient (deep slate -> indigo) ---
top = (15, 23, 42)      # #0f172a
bot = (30, 41, 90)      # #1e295a
bg = Image.new("RGB", (W, H))
px = bg.load()
for y in range(H):
    t = y / (H - 1)
    px_row = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
    for x in range(W):
        px[x, y] = px_row
draw = ImageDraw.Draw(bg)

# --- Accent bar on the left ---
draw.rectangle([0, 0, 12, H], fill=(79, 140, 255))

# --- Circular bio photo on the right ---
photo = Image.open("images/bio-photo.jpg").convert("RGB")
size = 340
photo = ImageOps.fit(photo, (size, size), Image.LANCZOS)
mask = Image.new("L", (size, size), 0)
ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
# ring
ring = Image.new("RGBA", (size + 16, size + 16), (0, 0, 0, 0))
ImageDraw.Draw(ring).ellipse([0, 0, size + 15, size + 15], fill=(79, 140, 255, 255))
px_x, px_y = W - size - 90, (H - size) // 2
bg.paste(ring, (px_x - 8, px_y - 8), ring)
bg.paste(photo, (px_x, px_y), mask)

# --- Text block on the left ---
x = 70
name_f = font("arialbd.ttf", 68)
role_f = font("arial.ttf", 36)
tag_f = font("arialbd.ttf", 28)
url_f = font("arial.ttf", 28)

draw.text((x, 150), "Dr. Minghua Ma", font=name_f, fill=(255, 255, 255))
draw.text((x, 240), "Senior Researcher", font=role_f, fill=(203, 213, 225))
draw.text((x, 288), "Microsoft M365 Research", font=role_f, fill=(203, 213, 225))

# tag pills
tags = ["AIOps", "Cloud Reliability", "AI Agents"]
tx = x
ty = 380
for tag in tags:
    tb = draw.textbbox((0, 0), tag, font=tag_f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    pad = 18
    draw.rounded_rectangle([tx, ty, tx + tw + pad * 2, ty + th + pad * 2],
                           radius=(th + pad * 2) // 2, fill=(79, 140, 255))
    draw.text((tx + pad, ty + pad - tb[1]), tag, font=tag_f, fill=(255, 255, 255))
    tx += tw + pad * 2 + 16

# CTA / url
draw.text((x, 500), "minghuama233.github.io", font=url_f, fill=(148, 163, 184))

bg.save("images/og-image.png", "PNG")
print("Wrote images/og-image.png", bg.size)
