import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 2, 58, r'$K$ sur $F$', 'sujet', 's', ha='left')
text(ax, 2, 38, r'$E$ sur $K$', 'autre', 's', ha='left')
text(ax, 2, 16, r'$E$ sur $F$', 'resultat', 's', ha='left')
for x, s in zip([26, 41], ['1', r'$\sqrt{2}$']):
    box(ax, x, 52, 13, 12, 'sujet', label=s)
for x, s in zip([26, 41], ['1', r'$\sqrt{3}$']):
    box(ax, x, 32, 13, 12, 'autre', label=s)
for x, s in zip([26, 41, 56, 71], ['1', r'$\sqrt{2}$', r'$\sqrt{3}$', r'$\sqrt{6}$']):
    box(ax, x, 10, 13, 12, 'resultat', label=s)
arrow(ax, (40, 32), (40, 23), 'varie')
text(ax, 44, 27.5, 'produits deux à deux', 'varie', 's', ha='left')
text(ax, 44, 4, r'$2\times2=4$ briques : contrôle', 'encre', 's')
save(fig, '61-107')
