import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x0, x1 = 14, 74
fx = lambda v: x0 + (v + 8) / 16 * (x1 - x0)
text(ax, 44, 73, r'idéal engendré par $2$ : $2$ est-il dedans ?', 'sujet', 's')
# row A: 2Z, products 2 x (even)
text(ax, 44, 63, r'dans $2\mathbb{Z}$ : $2\times$ un pair', 'fixe', 's')
line(ax, [(fx(-8) - 3, 52), (fx(8) + 3, 52)], 'fixe')
for v in range(-8, 9, 2):
    if v % 4 == 0:
        disc(ax, fx(v), 52, 1.6, 'sujet')
    else:
        disc(ax, fx(v), 52, 1.6, 'limite' if v == 2 else 'fixe', fill=False)
text(ax, fx(2), 45, '2 absent', 'limite', 's')
# row B: Z, products 2 x (integer)
text(ax, 44, 31, r'dans $\mathbb{Z}$ : $2\times$ un entier', 'fixe', 's')
line(ax, [(fx(-8) - 3, 20), (fx(8) + 3, 20)], 'fixe')
for v in range(-8, 9, 2):
    disc(ax, fx(v), 20, 1.6, 'resultat' if v == 2 else 'sujet')
text(ax, fx(2), 13, r'$2=1\times2$ présent', 'resultat', 's')
save(fig, '56-211')
