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
fig, ax = canvas(52)
y = 18
f = numberline(ax, 6, 78, y, 0, 840, 120, labels=False, arrow_right=False)
box(ax, f(0), y - 2.5, f(360) - f(0), 5, 'resultat', fill=True, r=0.4)
numberline(ax, 6, 78, y, 0, 840, 120, labels=False, arrow_right=False)
for v, role in [(0, 'fixe'), (120, 'resultat'), (360, 'fixe'), (480, 'varie'), (840, 'sujet')]:
    text(ax, f(v), y - 6, f'{v}°', role, 's', weight='bold' if role != 'fixe' else 'normal')
dot(ax, (f(840), y), 'sujet', 1.5); dot(ax, (f(480), y), 'varie', 1.5); dot(ax, (f(120), y), 'resultat', 1.5)
arrow(ax, (f(840), y + 2), (f(480), y + 2), 'varie', curve=0.5)
arrow(ax, (f(480), y + 2), (f(120), y + 2), 'varie', curve=0.5)
text(ax, f(660), y + 12.5, '− 360°', 'varie', 's')
text(ax, f(300), y + 12.5, '− 360°', 'varie', 's')
text(ax, f(840) - 2, y + 20, 'départ', 'sujet', 's', ha='center')
text(ax, f(120), y + 20, 'on s’arrête', 'resultat', 's')
text(ax, f(180), y - 12.5, 'entre 0° et 360°', 'resultat', 's')
save(fig, '28-076')
