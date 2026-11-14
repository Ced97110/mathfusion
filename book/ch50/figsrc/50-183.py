import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(84)
text(ax, 44, 77, r'$A_4$ : 12 éléments', 'encre', 'l')
text(ax, 44, 67, r'$n_3 = 4$ : $4 \times 2 = 8$ d’ordre 3', 'sujet', 'm')
for i in range(4):
    cx = 13 + i * 20.5
    ax.add_patch(Ellipse((cx, 54), 15, 8, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=1))
    for d in (-2.6, 2.6): disc(ax, cx + d, 54, 1.5, 'sujet')
text(ax, 44, 43, 'quatre sous-groupes de 3', 'sujet', 's')
text(ax, 44, 32, r'$n_2 = 1$ : les 4 restants', 'resultat', 'm')
box(ax, 22, 14, 44, 13, 'resultat', fill=True)
for i in range(4): disc(ax, 30 + i * 9.3, 20.5, 1.7, 'fixe' if i == 0 else 'resultat')
text(ax, 30, 10, r'$e$', 'fixe', 's')
text(ax, 58, 10, 'un seul sous-groupe', 'resultat', 's')
save(fig, '50-183')
