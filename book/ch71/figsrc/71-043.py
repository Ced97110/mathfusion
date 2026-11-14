import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'on compare sur chaque base', 'fixe', 's')
box(ax, 14, 44, 24, 10, 'sujet', label=r'$f$'); text(ax, 44, 49, '=', 'encre', 'l'); box(ax, 50, 44, 34, 10, 'autre', label=r'$2e_1^* + 1e_2^*$')
for y, e, v in ((26, r'sur $e_1$', 2), (8, r'sur $e_2$', 1)):
    text(ax, 3, y + 5, e, 'fixe', 's', ha='left')
    box(ax, 19, y, 14, 10, 'sujet', label=str(v)); text(ax, 44, y + 5, '=', 'resultat', 'l'); box(ax, 60, y, 14, 10, 'autre', label=str(v))
save(fig, '71-043')
