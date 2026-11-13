import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(62)
bx0, bx1 = 8, 80
step = (bx1 - bx0) / 100
text(ax, 8, 57, 'crayon : 14 cm', 'varie', 's', ha='left')
ax.add_patch(Rectangle((bx0, 44), bx1 - bx0, 8, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=1))
ax.add_patch(Rectangle((bx0, 44), 14 * step, 8, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
text(ax, 8, 40, '0 mètre entier', 'fixe', 's', ha='left')
arrow(ax, (44, 38), (44, 28), 'varie')
text(ax, 47, 33, 'on coupe en 100', 'varie', 's', ha='left')
ax.add_patch(Rectangle((bx0, 14), 14 * step, 8, ec='none', fc=FILL['varie'], zorder=1.5))
for i in range(101):
    ax.plot([bx0 + i * step] * 2, [14, 22], color=COL['varie'] if i <= 14 else COL['fixe'], lw=0.3, zorder=2)
line(ax, [(bx0, 14), (bx1, 14), (bx1, 22), (bx0, 22), (bx0, 14)], 'fixe', lw=0.8)
text(ax, 8, 9, '14 parts de 1/100', 'resultat', 's', ha='left')
save(fig, '08-015')
