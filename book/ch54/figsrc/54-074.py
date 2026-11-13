import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R, r = 23, 36, 14.5, 3.6
pts = [(cx + R * math.cos(math.radians(90 - 60 * i)), cy + R * math.sin(math.radians(90 - 60 * i))) for i in range(6)]
for i, (x, y) in enumerate(pts):
    disc(ax, x, y, r, 'sujet', label=str(i))
for i in range(6):
    (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % 6]
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * (r + 0.5), y0 + uy * (r + 0.5)), (x1 - ux * (r + 0.5), y1 - uy * (r + 0.5)), 'varie')
text(ax, cx, 60, 'ℤ/6', 'sujet', 'l')
text(ax, cx, 9, 'flèche : + 1 ; au 6ᵉ pas, 0', 'sujet', 's')
box(ax, 50, 36, 36, 12, 'limite', label='2 × 3 = 0', size='l')
text(ax, 68, 31, 'deux nombres non nuls', 'limite', 's')
text(ax, 68, 22, 'ℤ/6 n’est pas un corps', 'limite', 's')
save(fig, '54-074')
