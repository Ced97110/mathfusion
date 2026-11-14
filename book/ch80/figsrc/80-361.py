import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'un chiffre par élément 1, 2, 3', 'fixe', 's')
text(ax, 3, 45, r'$\{2\}$', 'sujet', 'l', ha='left')
text(ax, 3, 17, r'$\{1,3\}$', 'autre', 'l', ha='left')
xs = [38, 53, 68]
for x, a, b in zip(xs, '010', '101'):
    box(ax, x - 6, 40, 12, 10, 'sujet', label=a, size='l')
    box(ax, x - 6, 12, 12, 10, 'autre', label=b, size='l')
for x, a, b in zip(xs, '010', '101'):
    ok = a < b
    text(ax, x, 31, f'{a} < {b}' if ok else f'{a} > {b}', 'resultat' if ok else 'limite', 'm')
text(ax, 44, 3, 'aucune partout plus petite', 'limite', 's')
save(fig, '80-361')
