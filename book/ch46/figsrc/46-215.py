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

fig, ax = canvas(44)
xs = [4, 34, 64]; roles = ['sujet', 'varie', 'resultat']; cards = [('4', '7'), ('7', '4'), ('4', '7')]
caps = ['départ', 'après 1 fois', 'après 2 fois']
for x0, rl, (a, b), cp in zip(xs, roles, cards, caps):
    box(ax, x0, 22, 10, 10, rl, label=a); box(ax, x0 + 12, 22, 10, 10, rl, label=b)
    text(ax, x0 + 11, 15, cp, rl, 's')
for x0 in xs[:2]:
    arrow(ax, (x0 + 24, 27), (x0 + 29, 27), 'varie'); text(ax, x0 + 26.5, 35, '(4 7)', 'varie', 's')
text(ax, 75, 7, '= identité', 'resultat', 's')
save(fig, '46-215')
