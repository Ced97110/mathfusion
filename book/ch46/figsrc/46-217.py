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

fig, ax = canvas(60)
xs = [10, 22, 34, 46]
for c, s in zip(xs, '1234'):
    text(ax, c, 53, s, 'sujet', 'm')
rows = [(40, '(3 4)(1 2)', (0, 1), (2, 3)), (18, '(1 2)(3 4)', (2, 3), (0, 1))]
for y, lab, first, second in rows:
    for c in xs:
        disc(ax, c, y, 2.2, 'fixe')
    for (a, b), rl, n in ((first, 'varie', '1'), (second, 'autre', '2')):
        line(ax, [(xs[a], y - 3), (xs[a], y - 6), (xs[b], y - 6), (xs[b], y - 3)], rl, lw=1.2)
        text(ax, (xs[a] + xs[b]) / 2, y - 9, n, rl, 's')
    text(ax, 56, y, lab, 'encre', 'm', ha='left')
line(ax, [(74, 40), (78, 40), (78, 18), (74, 18)], 'resultat', lw=1.2)
text(ax, 83, 29, '=', 'resultat', 'l')
text(ax, 44, 4, 'même résultat', 'resultat', 's')
save(fig, '46-217')
