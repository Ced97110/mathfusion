import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$\varphi(n) = n \cdot 1$ dans le corps à 4 éléments', 'sujet', 'm')
# value of n*1 in the field with 4 elements: 1+1=0, so the sum is 1 when n is odd, 0 when n is even
rows = [(3, 1), (4, 0), (5, 1)]
for k, (n, v) in enumerate(rows):
    y = 52 - k * 17
    text(ax, 9, y, f'{n} termes', 'encre', 's')
    for i in range(n):
        disc(ax, 22 + i * 6.2, y, 2.3, 'sujet')
    arrow(ax, (55, y), (62, y), 'varie')
    box(ax, 63, y - 5, 22, 10, 'resultat', label=rf'$\varphi({n}) = {v}$')
text(ax, 44, 4,'chaque disque vaut 1', 'sujet', 's')
save(fig, '67-061')
