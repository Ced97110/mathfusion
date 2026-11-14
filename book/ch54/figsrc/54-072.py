import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R, r = 23, 36, 14.5, 3.6
pts = [(cx + R * math.cos(math.radians(90 - 72 * i)), cy + R * math.sin(math.radians(90 - 72 * i))) for i in range(5)]
for i, (x, y) in enumerate(pts):
    disc(ax, x, y, r, 'sujet', label=str(i))
for i in range(5):
    (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % 5]
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * (r + 0.5), y0 + uy * (r + 0.5)), (x1 - ux * (r + 0.5), y1 - uy * (r + 0.5)), 'varie')
text(ax, cx, 60, 'ℤ/5', 'sujet', 'l')
text(ax, cx, 9, 'flèche : + 1 ; au 5ᵉ pas, 0', 'sujet', 's')
text(ax, 67, 60, 'ℚ', 'autre', 'l')
arrow(ax, (50, 36), (85, 36), 'fixe', lw=0.9)
text(ax, 50, 31, '0', 'fixe', 's')
for k, x in enumerate((58, 67, 76), 1):
    disc(ax, x, 36, 1.3, 'autre')
    text(ax, x, 41, str(k), 'autre', 's')
text(ax, 67, 9, 'jamais 0 : caractéristique 0', 'autre', 's')
save(fig, '54-072')
