import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
box(ax, 2, 50, 84, 44, 'resultat', fill=False, dash=True)
text(ax, 44, 89, 'multiples de 4 : la formule tient', 'resultat', 's', weight='bold')
for k, (a, p) in enumerate((('3 et 2', '6'), ('7 et 2', '14'), ('7 et 6', '42'))):
    y = 78 - k * 11
    box(ax, 8, y - 4, 20, 8, 'varie', label=a, size='s')
    arrow(ax, (28.5, y), (46, y), 'varie'); text(ax, 40, y + 3, p, 'fixe', 's')
box(ax, 50, 56, 32, 28, 'resultat', label=None)
text(ax, 66, 74, r'$\bar{2}$', 'resultat', 'xl'); text(ax, 66, 63, 'toujours la même', 'resultat', 's')
box(ax, 2, 2, 84, 44, 'limite', fill=False, dash=True)
text(ax, 44, 41, 'si deux choix, deux classes', 'limite', 's', weight='bold')
box(ax, 6, 14, 22, 18, 'sujet', label=r'$\bar{a}\cdot\bar{b}$', size='m')
arrow(ax, (29, 26), (50, 31), 'limite'); arrow(ax, (29, 20), (50, 15), 'limite')
box(ax, 52, 26, 14, 10, 'limite', label=r'$\bar{c}$'); box(ax, 52, 10, 14, 10, 'limite', label=r'$\bar{c}\,\prime$')
text(ax, 72, 23, r'$\neq$', 'limite', 'xl', ha='left')
text(ax, 44, 5.5, 'deux résultats : pas un produit', 'limite', 's')
save(fig, '52-077')
