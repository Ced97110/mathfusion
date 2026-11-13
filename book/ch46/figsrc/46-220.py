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
for y, s, rl, ch, lab in ((58, r'$\sigma$', 'sujet', ('(1 3)', '(1 2)'), r'$m = 2$'), (38, r'$\sigma^{-1}$', 'varie', ('(1 2)', '(1 3)'), None), (18, r'$\sigma$', 'autre', ('(1 2)', '(2 3)'), r'$k = 2$')):
    text(ax, 3, y, s, rl, 'm', ha='left')
    chip(ax, 14, y - 4, ch[0], rl); chip(ax, 31, y - 4, ch[1], rl)
    if lab: text(ax, 48, y, lab, rl, 'm', ha='left')
text(ax, 14, 48, 'ordre renversé : inverse de σ', 'varie', 's', ha='left')
line(ax, [(60, 38), (64, 38), (64, 18), (60, 18)], 'resultat', lw=1.2)
text(ax, 76, 32, '= identité', 'resultat', 's'); text(ax, 76, 24, r'$k + m = 4$', 'resultat', 's')
text(ax, 44, 5, r'$k+m$ pair : même parité', 'resultat', 's')
text(ax, 14, 28, 'autre écriture de σ ↓', 'autre', 's', ha='left')
save(fig, '46-220')
