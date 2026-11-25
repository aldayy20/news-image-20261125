#!/usr/bin/env python3
"""Render the 25 November 2026 world-news poster (1024x1024 PNG).

Run:  python3 render.py            -> writes entry.png beside this file
Uses only Pillow + the DejaVu fonts shipped with most Linux systems.
The graded entrypoint is main.ts, which copies the rendered entry.png
to $MAKEFUN_OUTPUT_DIR/entry.png. This script is kept in the repo so
anyone can regenerate the image from source.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (185, 28, 28)
DARKRED = (127, 29, 29)
BLUE = (29, 78, 216)
NAVY = (30, 58, 138)
TEAL = (13, 116, 128)
AMBER = (180, 83, 9)
GREEN = (21, 101, 52)
GREY = (87, 83, 78)
LIGHT = (255, 255, 255)
PANEL = (255, 255, 255)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def kicker(draw, x, y, label, colour):
    f = font(FB, 21)
    w = int(draw.textlength(label, font=f)) + 22
    draw.rounded_rectangle([x, y, x + w, y + 32], radius=4, fill=colour)
    draw.text((x + 11, y + 4), label, font=f, fill=LIGHT)
    return w


def panel(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=PANEL, outline=(210, 205, 192), width=2)


def main():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)

    # ---- top black bar: the date, unmissable -------------------------------
    d.rectangle([0, 0, W, 62], fill=INK)
    d.text((24, 12), "WEDNESDAY, 25 NOVEMBER 2026", font=font(FB, 32), fill=LIGHT)
    d.text((W - 24 - d.textlength("ONE DAY  •  ONE IMAGE", font=font(FB, 24)), 18),
           "ONE DAY  •  ONE IMAGE", font=font(FB, 24), fill=(251, 191, 36))

    # ---- masthead ------------------------------------------------------------
    d.text((24, 74), "THE WORLD IN ONE IMAGE", font=font(FB, 58), fill=INK)
    d.text((24, 140), "Seven stories that defined the day — from Tiangong to Hormuz.",
           font=font(FR, 24), fill=GREY)
    d.line([24, 178, W - 24, 178], fill=INK, width=3)

    # ---- HERO: Shenzhou-24 --------------------------------------------------
    x, y, w, h = 24, 192, 976, 218
    panel(d, x, y, w, h)
    d.rounded_rectangle([x, y, x + 320, y + h], radius=10, fill=NAVY)
    d.rounded_rectangle([x + 300, y, x + 320, y + h], radius=0, fill=NAVY)
    d.text((x + 26, y + 18), "1st", font=font(FB, 92), fill=LIGHT)
    d.text((x + 26, y + 128), "PAKISTANI", font=font(FB, 40), fill=LIGHT)
    d.text((x + 26, y + 172), "IN ORBIT", font=font(FB, 40), fill=(147, 197, 253))
    kicker(d, x + 350, y + 18, "SPACE  •  SHENZHOU-24", NAVY)
    d.text((x + 350, y + 62), "A FOREIGNER ON TIANGONG",
           font=font(FB, 34), fill=INK)
    text_block(d, x + 350, y + 118,
               "Muhammad Zeeshan Ali, 40, docks 3.5 hours after liftoff "
               "— the first Pakistani in space and the first foreign "
               "astronaut on China's station.",
               font(FR, 20), INK, 600, leading=25)

    # ---- Row 2: Hormuz | Huawei ---------------------------------------------
    y2, h2 = 426, 218
    # Hormuz
    x, w = 24, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "WAR  •  STRAIT OF HORMUZ", DARKRED)
    d.text((x + 18, y2 + 58), "2 MORE TANKERS", font=font(FB, 38), fill=INK)
    d.text((x + 18, y2 + 100), "HIT MINES", font=font(FB, 38), fill=INK)
    text_block(d, x + 18, y2 + 148,
               "Iran's Guards say two tankers hit mines and caught fire; "
               "Tehran offers to reopen the strait if the US lifts its "
               "blockade.",
               font(FR, 19), INK, w - 36, leading=23)
    # Huawei
    x, w = 524, 476
    panel(d, x, y2, w, h2)
    kicker(d, x + 18, y2 + 16, "TECH  •  US COURT", AMBER)
    d.text((x + 18, y2 + 58), "HUAWEI GUILTY", font=font(FB, 38), fill=INK)
    d.text((x + 18, y2 + 100), "OF THEFT", font=font(FB, 38), fill=INK)
    text_block(d, x + 18, y2 + 148,
               "A New York jury convicts Huawei of conspiring to steal "
               "trade secrets — but acquits it of racketeering.",
               font(FR, 19), INK, w - 36, leading=23)

    # ---- Row 3: Colombia | Indonesia | Ukraine -------------------------------
    y3, h3, w3 = 660, 196, 312
    # Colombia
    x = 24
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "COLOMBIA", TEAL)
    d.text((x + 16, y3 + 54), "ALL HOSTAGES", font=font(FB, 27), fill=INK)
    d.text((x + 16, y3 + 86), "FREED", font=font(FB, 27), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Troops storm a Cartagena supermarket after a day-long "
               "siege; one captor killed.",
               font(FR, 18), INK, w3 - 32, leading=23)
    # Indonesia
    x = 356
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "INDONESIA", GREEN)
    d.text((x + 16, y3 + 54), "MINERS", font=font(FB, 30), fill=INK)
    d.text((x + 16, y3 + 86), "TRAPPED", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Rescuers search for dozens trapped in a flooded illegal "
               "gold mine in West Java.",
               font(FR, 18), INK, w3 - 32, leading=23)
    # Ukraine
    x = 688
    panel(d, x, y3, w3, h3)
    kicker(d, x + 16, y3 + 14, "UKRAINE", BLUE)
    d.text((x + 16, y3 + 54), "€115BN", font=font(FB, 30), fill=INK)
    d.text((x + 16, y3 + 86), "NEEDED", font=font(FB, 30), fill=INK)
    text_block(d, x + 16, y3 + 124,
               "Zelensky says Kyiv needs €115bn for 2027 as the US "
               "pauses Patriot supplies.",
               font(FR, 18), INK, w3 - 32, leading=23)

    # ---- Sport strip -----------------------------------------------------------
    y4, h4 = 872, 104
    panel(d, 24, y4, 976, h4)
    kicker(d, 42, y4 + 14, "SPORT", GREEN)
    d.text((42, y4 + 52), "Senegal get their AFCON title back — court restores 2025 crown.",
           font=font(FB, 22), fill=INK)
    d.text((42, y4 + 82), "Morocco vow to challenge the ruling; the trophy returns to Dakar.",
           font=font(FR, 18), fill=GREY)

    # ---- footer ------------------------------------------------------------------
    d.line([24, 982, W - 24, 982], fill=(210, 205, 192), width=2)
    d.text((24, 988), "Sources: Reuters, AP, Xinhua, France 24, Yonhap, Bloomberg",
           font=font(FR, 13), fill=GREY)
    d.text((24, 1006), "Also: Australia–Solomon treaty; Shanghai party chief probed; "
           "Bangladesh wage +36%; N. Korea expels Swiss envoy; UK sabotage warning.",
           font=font(FR, 13), fill=GREY)

    im.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", im.size)


if __name__ == "__main__":
    main()
