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
text(ax, 44, 58, r'$a = 4,\ b = 5,\ c = 9$', 'encre', 'm')
text(ax, 4, 51, r'$(b\ c)(a\ b)$', 'sujet', 'm', ha='left')
chip(ax, 4, 38, '(4 5)'); chip(ax, 26, 38, '(5 9)'); arrow(ax, (19, 42), (25, 42), 'varie')
text(ax, 4, 27, r'$(a\ c)(b\ c)$', 'autre', 'm', ha='left')
chip(ax, 4, 14, '(5 9)', 'autre'); chip(ax, 26, 14, '(4 9)', 'autre'); arrow(ax, (19, 18), (25, 18), 'varie')
cyc(ax, 72, 30, 8, [4, 9, 5], 'resultat')
arrow(ax, (42, 42), (66.5, 38.5), 'fixe'); arrow(ax, (42, 18), (61.5, 24), 'fixe')
text(ax, 72, 14, '(4 9 5)', 'resultat', 'm')
text(ax, 51, 30, '=', 'resultat', 'xl', weight='bold')
text(ax, 84, 51, 'on lit de gauche à droite', 'fixe', 's', ha='right')
save(fig, '46-216')
