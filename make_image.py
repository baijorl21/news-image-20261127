#!/usr/bin/env python3
"""Draw a one-page world-news front page for Friday 27 November 2026.

Original PIL drawing from scratch: no photos, logos, or external assets.
Output: entry.png (1024x1024) beside this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"

PAPER = (247, 243, 233)
INK = (24, 28, 38)
NAVY = (18, 38, 74)
RED = (178, 34, 34)
GOLD = (201, 148, 38)
GREY = (92, 96, 104)
CARD = (255, 253, 247)
LINE = (205, 198, 180)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, text, font, max_w, fill=INK, leading=6):
    for ln in wrap(text, font, max_w):
        d.text((x, y), ln, font=font, fill=fill)
        y += font.size + leading
    return y


def centered(y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


# ---------- masthead ----------
d.rectangle([0, 0, W, 122], fill=NAVY)
d.rectangle([0, 122, W, 130], fill=GOLD)
centered(14, "THE WORLD IN ONE PAGE", F(SERIF_B, 50), (255, 255, 255))
centered(76, "FRIDAY  27  NOVEMBER  2026", F(SANS_B, 26), (255, 214, 120))

# ---------- lead story ----------
ly = 146
d.text((36, ly), "MIDDLE EAST  ·  KUWAIT", font=F(SANS_B, 22), fill=RED)
ly = text_block(36, ly + 30, "Two Italians killed in Kuwait drone strike",
                F(SERIF_B, 40), 700, leading=4)
ly = text_block(36, ly + 6,
                "Rheinmetall technicians Antonio Saccoccio, 65, and Emanuele Lo Russo, 36, "
                "died after drones hit an air-defence station. Kuwait and Italy blame Iran; Tehran denies it.",
                F(SANS, 20), 700, fill=(52, 56, 66), leading=5)
# drone icon
cx, cy = 870, 215
d.ellipse([cx - 26, cy - 16, cx + 26, cy + 16], fill=NAVY)
for dx, dy in [(-58, -34), (58, -34), (-58, 34), (58, 34)]:
    d.line([cx, cy, cx + dx, cy + dy], fill=NAVY, width=7)
    d.ellipse([cx + dx - 22, cy + dy - 7, cx + dx + 22, cy + dy + 7], outline=RED, width=5)
d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=GOLD)
d.line([36, 350, W - 36, 350], fill=LINE, width=3)

# ---------- cards ----------
cards = [
    ("GAZA", RED, "Israeli strikes kill 10; Hamas weighs response",
     "Deputy education minister Khaled Abu Nada died in Deir al-Balah. Hamas chief Khalil al-Hayya warned attacks cannot be accepted.", "burst"),
    ("UNITED STATES", NAVY, "Thanksgiving storm: 900,000 without power",
     "Gusts hit 70 mph and 400+ flights were cancelled. New York postponed the 100th Macy's parade for the first time, to Saturday.", "storm"),
    ("UNITED KINGDOM", NAVY, "Net migration falls to 77,000, lowest since 1997",
     "ONS figures for the year to June 2026, down from 204,000 a year earlier and a 944,000 peak in 2023, excluding the pandemic years.", "chart"),
    ("THAILAND · BANGKOK", RED, "Refinery blast injures 9; all units shut",
     "Fire at Bangchak's Phra Khanong plant was out in 30 minutes. The 120,000-barrel-a-day refinery halted production.", "flame"),
    ("NEW ZEALAND", NAVY, "Final election count due today, 2pm",
     "About 400,000 special votes decide a 131-seat parliament. Preliminary: National 42, Labour 36; coalition holds 67.", "ballot"),
    ("SPAIN · IBIZA", NAVY, "Diesel tanker capsizes off Ibiza; one dead",
     "The Med Emre, carrying up to 7,000 tonnes of diesel, overturned 25 nautical miles offshore. All 17 crew rescued; one later died.", "ship"),
]

gx, gy, gw, gh, gap = 36, 360, 466, 170, 14
for i, (region, accent, head, body, icon) in enumerate(cards):
    x = gx + (i % 2) * (gw + gap)
    y = gy + (i // 2) * (gh + gap)
    d.rounded_rectangle([x, y, x + gw, y + gh], radius=14, fill=CARD, outline=LINE, width=2)
    d.rectangle([x, y, x + 10, y + gh], fill=accent)
    d.text((x + 24, y + 10), region, font=F(SANS_B, 19), fill=accent)
    hy = text_block(x + 24, y + 36, head, F(SERIF_B, 24), gw - 48, leading=3)
    text_block(x + 24, hy + 4, body, F(SANS, 17), gw - 48, fill=(52, 56, 66), leading=4)
    ix, iy = x + gw - 44, y + 20
    if icon == "burst":
        for a in range(0, 360, 45):
            import math
            d.line([ix, iy, ix + 13 * math.cos(math.radians(a)), iy + 13 * math.sin(math.radians(a))], fill=RED, width=4)
        d.ellipse([ix - 5, iy - 5, ix + 5, iy + 5], fill=GOLD)
    elif icon == "storm":
        d.ellipse([ix - 18, iy - 10, ix + 18, iy + 8], fill=NAVY)
        d.polygon([(ix - 2, iy + 4), (ix + 8, iy + 4), (ix + 1, iy + 14), (ix + 10, iy + 14), (ix - 5, iy + 26), (ix - 1, iy + 14), (ix - 9, iy + 14)], fill=GOLD)
    elif icon == "chart":
        d.line([ix - 16, iy - 10, ix - 4, iy + 1, ix + 5, iy - 4, ix + 14, iy + 9], fill=NAVY, width=5)
        d.polygon([(ix + 6, iy + 9), (ix + 17, iy + 9), (ix + 14, iy + 17)], fill=NAVY)
    elif icon == "flame":
        d.polygon([(ix, iy - 15), (ix + 11, iy + 3), (ix + 5, iy + 14), (ix - 5, iy + 14), (ix - 11, iy + 3)], fill=RED)
        d.polygon([(ix, iy - 2), (ix + 5, iy + 8), (ix - 5, iy + 8)], fill=GOLD)
    elif icon == "ballot":
        d.rectangle([ix - 15, iy - 4, ix + 15, iy + 14], outline=NAVY, width=4)
        d.line([ix - 8, iy + 5, ix - 1, iy + 11, ix + 9, iy - 10], fill=RED, width=5)
    elif icon == "ship":
        d.polygon([(ix - 18, iy + 3), (ix + 18, iy + 3), (ix + 11, iy + 13), (ix - 11, iy + 13)], fill=NAVY)
        d.rectangle([ix - 3, iy - 11, ix + 7, iy + 3], fill=RED)
        d.arc([ix - 18, iy + 9, ix - 3, iy + 20], 0, 180, fill=NAVY, width=3)
        d.arc([ix - 1, iy + 9, ix + 14, iy + 20], 0, 180, fill=NAVY, width=3)

# ---------- bottom strip: chess + footer ----------
by = gy + 3 * gh + 2 * gap + 14
d.rectangle([36, by, W - 36, by + 76], fill=NAVY)
d.text((56, by + 9), "GENEVA · CHESS", font=F(SANS_B, 18), fill=(255, 214, 120))
text_block(56, by + 33, "Gukesh–Sindarov Game 3: 60-move draw, 1.5–1.5. Rest day today.",
           F(SANS_B, 20), 800, fill=(255, 255, 255), leading=3)
# pawn icon
px, py = 920, by + 40
d.ellipse([px - 11, py - 26, px + 11, py - 4], fill=(255, 255, 255))
d.polygon([(px - 14, py + 16), (px + 14, py + 16), (px + 6, py - 6), (px - 6, py - 6)], fill=(255, 255, 255))
d.rectangle([px - 18, py + 16, px + 18, py + 24], fill=GOLD)
centered(by + 84, "Summarised from 27 November 2026 wire reports  ·  Reuters · BBC · AP · CNN", F(SANS, 17), GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print(out, os.path.getsize(out))
