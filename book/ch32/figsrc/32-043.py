import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, tip=False, dash=False):
    n = max(2, int(abs(a1 - a0) / 3) + 1)
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / (n - 1)) for i in range(n)], role, lw, dash)
    if tip:
        s = 1 if a1 > a0 else -1
        arrow(ax, P(cx, cy, R, a1 - s * 6), P(cx, cy, R, a1), role, lw)
def dot(ax, x, y, role, r=1.2): disc(ax, x, y, r, role)
def frame(ax, cx, cy, R, vert=True):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
    if vert: line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)

fig, ax = canvas(58)
text(ax, 44, 52, '$n$ : un entier', 'sujet', 'm')
for i, (n, r) in enumerate(((-2, '−690°'), (-1, '−330°'), (0, '30°'), (1, '390°'), (2, '750°'))):
    x = 5 + 16 * i
    box(ax, x, 34, 13, 9, 'sujet', label=f'{n}'.replace('-', '−'), size='m')
    arrow(ax, (x + 6.5, 33), (x + 6.5, 22), 'varie')
    box(ax, x, 11, 13, 9, 'resultat', label=r, size='s')
text(ax, 44, 4.5, '30° + 360°$n$', 'resultat', 'm')
save(fig, '32-043')
