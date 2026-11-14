import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 2, 62, 'x = 25 : on teste des y', 'encre', 's', ha='left', weight='bold')
for i in range(5):
    box(ax, 2 + 17 * i, 48, 15, 9, 'resultat' if i == 4 else 'fixe', label=f'{i + 1}²={(i + 1) ** 2}', size='s')
text(ax, 2, 40, 'x = −3 : on teste des y', 'encre', 's', ha='left', weight='bold')
for i in range(3):
    box(ax, 2 + 17 * i, 26, 15, 9, 'fixe', label=f'{i + 1}²={(i + 1) ** 2}', size='s')
text(ax, 54, 30.5, '… ne finit jamais', 'limite', 's', ha='left')
box(ax, 2, 6, 40, 9, 'varie', label='signe de −3 : négatif', size='s')
arrow(ax, (43, 10.5), (49, 10.5), 'varie')
box(ax, 50, 6, 36, 9, 'limite', label='aucun y ne convient', size='s')
save(fig, '70-167')
