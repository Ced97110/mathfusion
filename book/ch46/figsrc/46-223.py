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
text(ax, 44, 55, '(1 6) : toujours impair', 'autre', 'm')
chip(ax, 4, 40, '(1 6)', 'autre'); text(ax, 24, 44, '1 échange', 'autre', 's', ha='left')
for i, s in enumerate(['(2 3)', '(1 6)', '(2 3)']): chip(ax, 4 + 17 * i, 24, s, 'autre')
text(ax, 56, 28, '3 échanges', 'autre', 's', ha='left')
for i in range(7): box(ax, 4 + 8 * i, 9, 6, 6, 'autre')
text(ax, 62, 12, '7 échanges', 'autre', 's', ha='left')
save(fig, '46-223')
