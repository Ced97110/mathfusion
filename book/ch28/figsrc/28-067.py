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
cx, cy, R = 30, 32, 24
poly(ax, [(cx, cy), (cx, cy + R + 3), (cx - R - 3, cy + R + 3), (cx - R - 3, cy)], 'fixe')
circ(ax, cx, cy, R, ext=3)
for a in (100, 170):
    p = P(cx, cy, R, a); dot(ax, p, 'fixe', 1.0)
    text(ax, p[0] + (1 if a == 100 else -1) * 0, p[1] + 3.2 if a == 100 else p[1] + 3.2, f'{a}°', 'fixe', 's')
p = P(cx, cy, R, 130)
line(ax, [(cx, cy), p], 'sujet', lw=1.1)
line(ax, [p, (p[0], cy)], 'fixe', lw=0.8, dash=True)
line(ax, [p, (cx, p[1])], 'fixe', lw=0.8, dash=True)
dot(ax, p, 'sujet', 1.5)
text(ax, p[0] - 2, p[1] + 3.5, r'$P$ à 130°', 'sujet', 's', ha='right')
text(ax, cx - 8, cy + R + 1, 'II', 'sujet', 'l', weight='bold') if False else None
text(ax, 72, 52, r'$\cos < 0$', 'varie', 'm')
text(ax, 72, 40, r'$\sin > 0$', 'varie', 'm')
text(ax, 72, 28, r'$\tan < 0$', 'varie', 'm')
text(ax, 72, 16, 'quadrant II', 'sujet', 's')
save(fig, '28-067')
