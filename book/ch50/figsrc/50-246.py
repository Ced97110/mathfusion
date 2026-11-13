import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'ordre $pq = 6$', 'encre', 'm', weight='bold')
for j in range(3):
    box(ax, 8 + 12 * j, 42, 11, 11, 'sujet'); box(ax, 8 + 12 * j, 30, 11, 11, 'varie')
text(ax, 50, 51, r'$q$-Sylow normal', 'sujet', 's', ha='left'); text(ax, 50, 46.5, r'$q = 3$ : cyclique', 'sujet', 's', ha='left')
text(ax, 50, 37, 'autres éléments', 'varie', 's', ha='left')
arrow(ax, (26, 28), (26, 20), 'fixe')
box(ax, 14, 8, 11, 11, 'sujet'); box(ax, 27, 8, 11, 11, 'varie')
text(ax, 42, 16, r'quotient : $p = 2$', 'resultat', 's', ha='left'); text(ax, 42, 11, 'cyclique', 'resultat', 's', ha='left')
text(ax, 62, 62, '2 étapes abéliennes', 'resultat', 's')
save(fig, '50-246')
