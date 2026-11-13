import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
def P(cx, cy, R, a): return (cx + R * cos(radians(a)), cy + R * sin(radians(a)))
def circ(ax, cx, cy, R, ext=4):
    disc(ax, cx, cy, R, 'fixe', fill=False)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.0):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw); arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.2): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(66)
cx, cy, R = 24, 33, 20
circ(ax, cx, cy, R, ext=3)
p = P(cx, cy, R, 300)
line(ax, [(cx, cy), p], 'sujet', lw=1.1)
line(ax, [p, (p[0], cy)], 'fixe', lw=0.8, dash=True)
dot(ax, p, 'sujet', 1.5)
text(ax, p[0] + 2, p[1] - 3, r'$P$ à 300°', 'sujet', 's', ha='left')
bx, bw = 52, 34
box(ax, bx, 46, bw, 13, 'sujet', label='1. P à droite ?  → cos +', size='s')
box(ax, bx, 28, bw, 13, 'sujet', label='2. P en bas ?  → sin −', size='s')
box(ax, bx, 8, bw, 13, 'resultat', label='− ÷ + : tan −', size='s')
arrow(ax, (bx + 10, 28), (bx + 10, 21.8), 'varie')
arrow(ax, (bx + 24, 28), (bx + 24, 21.8), 'varie')
save(fig, '28-068')
