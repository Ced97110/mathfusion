import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

from matplotlib.patches import Circle
fig, ax = canvas(92)
box(ax, 2, 72, 56, 13, 'sujet', label=r"$x\in A'\cap B'$", size='m')
box(ax, 2, 41, 56, 16, 'varie', label=r"$x\notin A$ et $x\notin B$" + "\n" + r"donc $x\notin A\cup B$", size='s', lw=1.8)
box(ax, 2, 12, 56, 13, 'resultat', label=r"$x\in(A\cup B)'$", size='m')
arrow(ax, (50, 72), (50, 57), 'varie'); arrow(ax, (50, 41), (50, 25), 'varie')
text(ax, 2, 89, 'départ', 'sujet', 's', ha='left')
text(ax, 2, 61, 'étape qui porte le poids', 'varie', 's', ha='left')
text(ax, 2, 29, 'arrivée', 'resultat', 's', ha='left')
box(ax, 62, 36, 24, 22, 'fixe', fill=False)
ax.add_patch(Circle((69, 49), 5.5, fc=FILL['sujet'], ec=COL['sujet'], lw=0.8, zorder=2))
ax.add_patch(Circle((78, 49), 5.5, fc=FILL['autre'], ec=COL['autre'], lw=0.8, zorder=2))
text(ax, 67, 49, r'$A$', 'sujet', 's'); text(ax, 80, 49, r'$B$', 'autre', 's')
disc(ax, 65, 40, 1.1, 'varie'); text(ax, 69, 40, r'$x$', 'varie', 's')
save(fig, '42-281')
