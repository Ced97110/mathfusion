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
cyc(ax, 16, 47, 7, [1, 2, 3, 4], 'sujet', rad=2.6, hl=(0, 1), lab=False)
arrow(ax, (30, 47), (44, 47), 'varie'); text(ax, 37, 52, r'$\times$ (1 2)', 'varie', 's'); text(ax, 37, 41, 'coupé', 'resultat', 's')
cyc(ax, 54, 47, 0, [1], 'resultat', rad=2.6, lab=False); cyc(ax, 71, 47, 6, [2, 3, 4], 'resultat', rad=2.6, lab=False)
text(ax, 16, 35, '(1 2 3 4)', 'sujet'); text(ax, 63, 35, '(1)(2 3 4)', 'resultat')
cyc(ax, 9, 17, 4.5, [1, 2], 'sujet', rad=2.6, hl=(0,), lab=False); cyc(ax, 25, 17, 4.5, [3, 4], 'autre', rad=2.6, hl=(0,), lab=False)
arrow(ax, (35, 17), (48, 17), 'varie'); text(ax, 41.5, 22, r'$\times$ (1 3)', 'varie', 's'); text(ax, 41.5, 11, 'soudés', 'resultat', 's')
cyc(ax, 68, 17, 7, [1, 2, 3, 4], 'resultat', rad=2.6, hl=(0, 2), lab=False)
text(ax, 17, 5, '(1 2)(3 4)', 'sujet'); text(ax, 68, 5, '(1 2 3 4)', 'resultat')
save(fig, '46-211')
