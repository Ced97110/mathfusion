import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
k = 0.9
gy = 6
cx, cy, r = 27, gy + 22 * k, 20 * k
line(ax, [(3, gy), (51, gy)], 'fixe', lw=1.0)
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=1.0, zorder=2))
line(ax, [(cx - r - 1, cy), (cx + r + 1, cy)], 'fixe', dash=True, lw=0.7)
a = np.radians(-45)
px, py = cx + r * np.cos(a), cy + r * np.sin(a)
line(ax, [(cx, cy), (px, py)], 'sujet', lw=1.3)
line(ax, [(px, cy), (px, py)], 'varie', lw=1.3)
disc(ax, cx, cy, 0.9, 'sujet')
disc(ax, px, py, 1.5, 'resultat')
line(ax, [(px, py), (px, gy)], 'resultat', lw=0.6, dash=True)
text(ax, cx + 5, cy - 9, '20 m', 'sujet', 's', ha='right')
text(ax, px + 2, (cy + py) / 2 + 1.5, '14,14 m', 'varie', 's', ha='left')
text(ax, cx + 6.5, cy + 2.2, r'$45°$', 'fixe', 's')
text(ax, px + 2, (py + gy) / 2 - 1, '7,86 m', 'resultat', 's', ha='left')
arrow(ax, (6, gy), (6, cy), 'fixe', both=True, lw=0.7)
text(ax, 7.5, (gy + cy) / 2 + 3, '22 m', 'fixe', 's', ha='left')
box(ax, 55, 36, 31, 9, 'sujet', label=r'formule : $7{,}86$ m', size='s')
box(ax, 55, 22, 31, 9, 'varie', label=r'$22-14{,}14=7{,}86$', size='s')
box(ax, 55, 8, 31, 9, 'resultat', label='même résultat', size='s')
arrow(ax, (70, 35.5), (70, 31.5), 'fixe')
arrow(ax, (70, 21.5), (70, 17.5), 'fixe')
save(fig, '30-136')
