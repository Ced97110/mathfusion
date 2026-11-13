import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(66)
text(ax, 22, 60, r'$a + b$ dans $\mathbb{Z}$', 'sujet', 'm'); text(ax, 66, 60, r'$A \cup B$ dans $\mathcal{P}(S)$', 'sujet', 'm')
y = 36
arrow(ax, (4, y), (40, y), 'fixe', lw=0.9); ax.plot([12, 12], [y - 1.2, y + 1.2], color=COL['fixe'], lw=0.8); text(ax, 12, y - 4, '0', 'fixe', 's')
arrow(ax, (12, y + 1), (24, y + 1), 'sujet', curve=-0.5); text(ax, 18, y + 8, r'$a$', 'sujet')
arrow(ax, (24, y + 1), (36, y + 1), 'autre', curve=-0.5); text(ax, 30, y + 8, r'$b$', 'autre')
disc(ax, 36, y, 1.4, 'resultat'); text(ax, 36, y - 4, r'$a + b$', 'resultat', 's')
box(ax, 46, 22, 40, 30, 'fixe', fill=False); text(ax, 50, 48, r'$S$', 'fixe', 's')
for cx, r in ((59, 'sujet'), (73, 'autre')): ax.add_patch(Circle((cx, 36), 9, fc=FILL['resultat'], ec=COL[r], lw=1.0, zorder=2))
text(ax, 55, 36, r'$A$', 'sujet'); text(ax, 77, 36, r'$B$', 'autre')
text(ax, 44, 12, 'deux éléments en entrée,', 'resultat', 's'); text(ax, 44, 7, 'un élément du même ensemble', 'resultat', 's')
save(fig, '42-266')
