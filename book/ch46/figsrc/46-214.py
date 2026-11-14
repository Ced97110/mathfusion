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

fig, ax = canvas(76)
cols = [48, 59, 70, 81]
for c, s in zip(cols, 'abcd'):
    text(ax, c, 68, '$%s$' % s, 'encre', 'm')
text(ax, 3, 72, 'haut : dernier échange (a b)', 'sujet', 's', ha='left')
text(ax, 3, 64, 'bas : avant-dernier échange', 'varie', 's', ha='left')
rows = [((0, 1), '(a b) : identique'), ((1, 2), '(b c) : partage b'), ((0, 2), '(a c) : partage a'), ((2, 3), '(c d) : rien en commun')]
for i, (pr, desc) in enumerate(rows):
    y = 52 - 14 * i
    for c in cols:
        disc(ax, c, y, 1.6, 'fixe')
    line(ax, [(cols[0], y + 2), (cols[0], y + 4.5), (cols[1], y + 4.5), (cols[1], y + 2)], 'sujet', lw=1.2)
    a, b = pr
    line(ax, [(cols[a], y - 2), (cols[a], y - 4.5), (cols[b], y - 4.5), (cols[b], y - 2)], 'varie', lw=1.2)
    text(ax, 3, y, desc, 'encre', 's', ha='left')
save(fig, '46-214')
