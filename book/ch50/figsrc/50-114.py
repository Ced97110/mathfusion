import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X, Wd, Hh = 22, 64, 11
box(ax, X, 50, Wd, Hh, 'sujet', label=r'$H$ agit sur les conjugués de $K$', size='s')
box(ax, X, 28, Wd, Hh, 'varie', label=r'stabilisateur de $K$ $=N(K)\cap H$', size='s', weight='bold')
box(ax, X, 6, Wd, Hh, 'resultat', label=r'nombre $=[H:N(K)\cap H]$', size='s')
text(ax, 11, 55.5, 'départ', 'sujet', 's'); text(ax, 11, 33.5, 'étape\nclé', 'varie', 's'); text(ax, 11, 11.5, 'arrivée', 'resultat', 's')
arrow(ax, (40, 50), (40, 39), 'fixe'); arrow(ax, (40, 28), (40, 17), 'fixe')
text(ax, 44, 44.5, r'orbite de $K$ = conjugués', 'fixe', 's', ha='left')
text(ax, 44, 22.5, 'formule du chapitre 49', 'fixe', 's', ha='left')
save(fig, '50-114')
