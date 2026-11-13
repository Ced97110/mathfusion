import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def setbox(y, n_on):
    box(ax, 28, y - 7, 34, 14, 'fixe', fill=False, dash=True)
    for i in range(3):
        disc(ax, 37 + i * 9, y, 3, 'resultat' if i < n_on else 'fixe')
# verifier
box(ax, 2, 50, 22, 12, 'fixe', label='vérifier', size='s')
box(ax, 28, 50, 16, 12, 'autre', label=r'$(3,\,2)$', size='s')
arrow(ax, (44.5, 56), (50, 56), 'varie')
box(ax, 51, 50, 24, 12, 'varie', label='2 calculs', size='s')
text(ax, 81, 56, '✓', 'resultat', 'l')
# trouver
box(ax, 2, 27, 22, 12, 'fixe', label='trouver', size='s')
setbox(33, 1)
text(ax, 76, 33, 'un seul couple', 'resultat', 's')
# resoudre
box(ax, 2, 4, 22, 12, 'sujet', label='résoudre', size='s', weight='bold')
setbox(10, 3)
text(ax, 76, 10, 'tous, sans oubli', 'resultat', 's')
save(fig, '24-024')
