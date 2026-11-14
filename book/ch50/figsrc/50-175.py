import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'sous-groupes normaux de $G$', 'encre', 'm')
def row(y, n, role, lab):
    for i in range(n): box(ax, 3 + 4.8 * i, y, 4.4, 8, role, r=0.5)
    if lab: text(ax, 3 + 4.8 * n + 2, y + 4, lab, role, 's', ha='left')
row(50, 1, 'fixe', r'$\{e\}$ : 1 élément')
row(36, 5, 'resultat', r'$Q$ normal : 5 éléments')
row(22, 15, 'sujet', None)
text(ax, 44, 15.5, r'$G$ : 15 éléments', 'sujet', 'm')
text(ax, 44, 6.5, r'$Q$ ni $\{e\}$ ni $G$ : $G$ pas simple', 'resultat', 's')
save(fig, '50-175')
