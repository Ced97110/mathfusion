import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(70)
numberline(ax, 12, 82, 14, 0, 28, step=1, labels=True, arrow_right=False, every=7, size='s')
text(ax, 47, 6, 'nombre de facteurs', 'fixe', 's')
line(ax, [(12, 14), (12, 60)], 'fixe')
for v, lab in [(1, '1'), (4, '4'), (8, '8')]:
    y = 14 + 5 * v
    line(ax, [(10.8, y), (12, y)], 'fixe')
    text(ax, 8.5, y, lab, 'fixe', 's')
text(ax, 8, 63, 'produit', 'fixe', 's')
ax.plot([14.5, 82], [19, 19], color=COL['sujet'], lw=0.9, zorder=1)
for n in range(1, 29):
    disc(ax, 12 + 2.5 * n, 19, 0.55, 'sujet', fill=True)
text(ax, 58, 23.5, 'base 1 : toujours 1', 'sujet', 's')
ax.plot([14.5, 17, 19.5], [24, 34, 54], color=COL['limite'], lw=0.9, zorder=1)
for x, y in [(14.5, 24), (17, 34), (19.5, 54)]:
    disc(ax, x, y, 0.8, 'limite', fill=True)
arrow(ax, (19.5, 54), (22, 61), 'limite')
text(ax, 40, 50, 'base 2 : 2, 4, 8, …', 'limite', 's')
text(ax, 70, 38, '1²⁸ = 1', 'resultat', 'l')
arrow(ax, (78, 35), (81.5, 21), 'resultat')
save(fig, '04-077')
