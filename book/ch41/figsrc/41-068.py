import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
m, n, v = 2, 3, (2, 3)
assert all((m + n) * c == m * c + n * c for c in v) and (m + n) * 2 == 10 and (m + n) * 3 == 15
box(ax, 4, 58, 80, 14, 'sujet', label='départ : la règle sur\nles vecteurs ' + r'$(m+n)v=mv+nv$', size='s')
arrow(ax, (44, 58), (44, 49), 'fixe', lw=1.0)
box(ax, 4, 36, 80, 13, 'varie', label='étape qui porte tout :\négaux ⇔ composantes égales', size='s', lw=1.4)
arrow(ax, (24, 36), (24, 27), 'fixe', lw=1.0)
arrow(ax, (64, 36), (64, 27), 'fixe', lw=1.0)
box(ax, 4, 6, 40, 21, 'resultat', label='1re composante\n' + r'$5\times 2=2\times 2+3\times 2$', size='s')
box(ax, 48, 6, 36, 21, 'resultat', label='2e composante\n' + r'$5\times 3=2\times 3+3\times 3$', size='s')
save(fig, '41-068')
