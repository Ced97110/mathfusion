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

fig, ax = canvas(64)
text(ax, 11, 58, r'$(a\ c)(a\ b)$', 'sujet', 'm'); text(ax, 77, 58, r'$(a\ b)(b\ c)$', 'autre', 'm')
chip(ax, 4, 44, '(1 2)'); chip(ax, 4, 22, '(1 3)'); arrow(ax, (11, 43.5), (11, 30.5), 'varie')
chip(ax, 70, 44, '(2 3)', 'autre'); chip(ax, 70, 22, '(1 2)', 'autre'); arrow(ax, (77, 43.5), (77, 30.5), 'varie')
cyc(ax, 44, 34, 8, [1, 2, 3], 'resultat')
arrow(ax, (20, 26), (33, 28.5), 'fixe'); arrow(ax, (68, 26), (55.5, 28.5), 'fixe')
text(ax, 44, 14, '(1 2 3)', 'resultat', 'm')
save(fig, '46-218')
