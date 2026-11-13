import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
box(ax, 2, 55, 46, 12, 'sujet', label=r"$x\in(A\cup B)'$", size='m')
box(ax, 2, 31, 46, 12, 'sujet', label=r"$x\notin A\cup B$", size='m')
box(ax, 2, 7, 46, 12, 'resultat', label=r"$x\notin A$ et $x\notin B$", size='m')
arrow(ax, (25, 55), (25, 43), 'varie', 1.4); arrow(ax, (25, 31), (25, 19), 'varie', 1.4)
text(ax, 30, 49, 'définition du\ncomplémentaire', 'varie', 's', ha='left')
text(ax, 30, 25, 'définition de\nl’union', 'varie', 's', ha='left')
save(fig, '42-282')
