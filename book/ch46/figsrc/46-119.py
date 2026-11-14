import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
for n in range(1, 13):
    x = 7.2 + (n - 1) * 6.7
    ok = 12 % n == 0
    disc(ax, x, 24, 2.7, 'resultat' if ok else 'limite', fill=True, label=str(n), size='s')
text(ax, 44, 36, 'nombre d’éléments d’un sous-groupe', 'encre', 'm')
text(ax, 44, 13, 'vert : diviseur de 12, il existe', 'resultat', 's')
text(ax, 44, 6, 'rouge : ne divise pas 12, impossible', 'limite', 's')
save(fig, '46-119')
