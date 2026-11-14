import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(46)
text(ax, 22, 40, 'un produit', 'sujet', 'm')
text(ax, 66, 40, 'une somme', 'resultat', 'm')
box(ax, 2, 22, 40, 12, 'sujet', label='2 sin 45° cos 15°', size='s')
box(ax, 46, 22, 40, 12, 'resultat', label='sin 60° + sin 30°', size='s')
arrow(ax, (42.5, 28), (45.5, 28), 'varie', lw=1.2)
text(ax, 22, 16, '≈ 1,366', 'sujet', 'm')
text(ax, 66, 16, '≈ 1,366', 'resultat', 'm')
text(ax, 44, 7, 'même valeur, écriture changée', 'varie', 's')
save(fig, '35-055')
