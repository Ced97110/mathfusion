import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [(3, 1, 'inverse : 7', 'resultat'), (4, 2, 'pas d’inverse', 'limite'), (5, 5, 'pas d’inverse', 'limite')]
for k, (a, g, v, r) in enumerate(rows):
    y = 44 - k * 17
    disc(ax, 10, y, 5.5, 'sujet', label=str(a), size='l')
    text(ax, 30, y, f'PGCD avec 10 : {g}', 'encre', 's')
    arrow(ax, (42, y), (49, y), r)
    box(ax, 50, y - 5, 36, 10, r, label=v)
save(fig, '47-185')
