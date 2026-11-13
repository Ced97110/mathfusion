import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools
fig, ax = canvas(92)
perms = list(itertools.permutations((1, 2, 3)))
assert len(perms) == 6 == 3 * 2 * 1
text(ax, 44, 86, r'$S_3$ : 6 rangements des racines', 'sujet', 'l', weight='bold')
text(ax, 44, 78, '3 choix × 2 choix × 1 choix = 6', 'encre', 's')
for k, p in enumerate(perms):
    col, row = k % 2, k // 2
    x, y = 2 + 44 * col, 52 - 15 * row
    label = r'$r_{%d}\ \ r_{%d}\ \ r_{%d}$' % p
    box(ax, x, y, 40, 11, 'sujet', label=label, size='m')
text(ax, 44, 13, 'chaque isomorphisme', 'resultat', 's')
text(ax, 44, 9, 'réalise l’un de ces rangements', 'resultat', 's')
save(fig, '62-159')
