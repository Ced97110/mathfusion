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

fig, ax = canvas(62)
chip(ax, 4, 50, '(1 3)'); chip(ax, 21, 50, '(1 2)'); text(ax, 40, 54, r'$m = 2$', 'sujet', ha='left')
chip(ax, 4, 34, '(1 2)', 'autre'); chip(ax, 21, 34, '(2 3)', 'autre'); text(ax, 40, 38, r'$k = 2$', 'autre', ha='left')
box(ax, 60, 39.5, 22, 9, 'resultat', label='(1 2 3)')
arrow(ax, (52, 54), (68, 49), 'fixe'); arrow(ax, (52, 38), (68, 39), 'fixe')
arrow(ax, (20, 32), (20, 17.5), 'varie')
chip(ax, 4, 8, '(1 2)', 'autre'); chip(ax, 21, 8, '(2 3)', 'autre'); chip(ax, 38, 8, '(1 2)'); chip(ax, 55, 8, '(1 3)')
text(ax, 79, 12, '= identité', 'resultat', 's')
text(ax, 62, 24, r'$m + k = 4$ : pair', 'varie', 's')
save(fig, '46-212')
