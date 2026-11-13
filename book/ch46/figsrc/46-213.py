import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def cyc(ax, cx, cy, r, nums, role, rad=3.0, hl=(), lab=True):
    n = len(nums)
    start = {1: 90, 2: 180, 3: 90, 4: 135}.get(n, 90)
    pts = [(cx + r * math.cos(math.radians(start - 360 * i / n)), cy + r * math.sin(math.radians(start - 360 * i / n))) for i in range(n)]
    if n >= 2:
        for i in range(n):
            p, q = pts[i], pts[(i + 1) % n]
            d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
            arrow(ax, (p[0] + ux * (rad + 0.3), p[1] + uy * (rad + 0.3)), (q[0] - ux * (rad + 0.3), q[1] - uy * (rad + 0.3)), role, lw=0.8, curve=0.5 if n == 2 else 0.0)
    for i, (p, v) in enumerate(zip(pts, nums)):
        disc(ax, p[0], p[1], rad, 'varie' if i in hl else role, label=str(v) if lab else None, size='s')
    return pts

def chip(ax, x, y, s, role='sujet', w=14, h=8, dash=False, fill=True):
    box(ax, x, y, w, h, role, fill=fill, label=s, size='m', dash=dash)

fig, ax = canvas(68)
f = numberline(ax, 8, 68, 30, 0, 5, labels=False, arrow_right=False)
for v in range(6):
    role = 'resultat' if v in (0, 2, 4) else ('limite' if v == 1 else 'fixe')
    disc(ax, f(v), 30, 3.2, role, label=str(v), size='m')
for a, b in ((4, 2), (2, 0)):
    arrow(ax, (f(a), 33.8), (f(b), 33.8), 'varie', curve=0.6)
    text(ax, (f(a) + f(b)) / 2, 46, r'$r \to r-2$', 'varie', 's')
text(ax, 44, 64, "l'identité en $r$ échanges", 'encre', 'm')
line(ax, [(f(1), 26.6), (f(1), 21)], 'limite')
text(ax, 22, 18, '1 échange déplace une carte', 'limite', 's')
text(ax, 62, 18, '0, 2, 4 : pair', 'resultat', 's')
text(ax, 44, 55, 'on retire 2 échanges à la fois', 'varie', 's')
text(ax, 44, 8, 'la descente finit à 0 : r est pair', 'resultat', 's')
save(fig, '46-213')
