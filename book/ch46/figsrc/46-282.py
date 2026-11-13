import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$\det A$ = somme de termes', 'encre', 'm')
text(ax, 44, 52, 'chacun avec le signe de sa permutation', 'fixe', 's')
for y, a, s, t, r in [(30, 'identité', '+1', r'$+\,a_{11}a_{22}$', 'resultat'), (10, 'échange', '−1', r'$-\,a_{12}a_{21}$', 'limite')]:
    box(ax, 3, y, 26, 11, 'sujet', label=a)
    arrow(ax, (30, y + 5.5), (38, y + 5.5), 'varie')
    box(ax, 39, y, 16, 11, r, label=s)
    arrow(ax, (56, y + 5.5), (62, y + 5.5), 'varie')
    box(ax, 63, y, 23, 11, r, label=t, size='s')
text(ax, 21, 45, 'permutation', 'sujet', 's')
text(ax, 47, 45, 'signature', 'fixe', 's')
text(ax, 74, 45, 'terme', 'fixe', 's')
save(fig, '46-282')
