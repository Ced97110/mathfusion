import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
k = 0.9
gy = 6
cx, cy, r = 27, gy + 22 * k, 20 * k
line(ax, [(3, gy), (51, gy)], 'fixe', lw=1.0)
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=1.0, zorder=2))
line(ax, [(cx - r - 1, cy), (cx + r + 1, cy)], 'fixe', dash=True, lw=0.7)
for deg, lab, tl in ((-45, '7,86 m', r'$t=1$'), (45, '36,14 m', r'$t=3$')):
    a = np.radians(deg)
    px, py = cx + r * np.cos(a), cy + r * np.sin(a)
    line(ax, [(cx, cy), (px, py)], 'sujet', lw=1.0)
    line(ax, [(px, cy), (px, py)], 'varie', lw=1.5)
    disc(ax, px, py, 1.4, 'resultat')
    text(ax, px - 2.5, py + (-3.0 if deg < 0 else 3.0), tl, 'fixe', 's', ha='right')
    text(ax, px + 2.2, py + (-1.5 if deg < 0 else 1.5), lab, 'resultat', 's', ha='left')
disc(ax, cx, cy, 0.9, 'sujet')
box(ax, 55, 36, 31, 10, 'varie', label='côté du triangle', size='s')
box(ax, 55, 22, 31, 9, 'fixe', label='+ 22 : le centre', size='s')
box(ax, 55, 8, 31, 9, 'resultat', label='hauteur de la cabine', size='s')
arrow(ax, (70, 35.5), (70, 31.5), 'fixe')
arrow(ax, (70, 21.5), (70, 17.5), 'fixe')
save(fig, '30-137')
