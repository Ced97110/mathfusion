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

fig, ax = canvas(66)
X = [4 + 17 * i for i in range(4)]
for x, s in zip(X, ['(1 3)', '(2 4)', '(1 3)', '(2 4)']): chip(ax, x, 56, s)
arrow(ax, (X[2] + 7, 55.5), (X[3] + 7, 42.5), 'varie'); arrow(ax, (X[3] + 7, 55.5), (X[2] + 7, 42.5), 'varie')
text(ax, 4, 49, 'on échange les deux', 'varie', 's', ha='left')
for x, s, rl in zip(X, ['(1 3)', '(2 4)', '(2 4)', '(1 3)'], ['sujet', 'varie', 'varie', 'sujet']): chip(ax, x, 34, s, rl)
text(ax, 4, 27, 'on supprime les deux (2 4)', 'varie', 's', ha='left')
chip(ax, X[0], 12, '(1 3)'); chip(ax, X[1], 12, '', 'fixe', dash=True, fill=False); chip(ax, X[2], 12, '', 'fixe', dash=True, fill=False); chip(ax, X[3], 12, '(1 3)')
text(ax, 72, 60, r'$r = 4$', 'sujet', 'm', ha='left'); text(ax, 72, 16, r'$r - 2 = 2$', 'resultat', 'm', ha='left')
save(fig, '46-219')
