import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
c = 3.2; y = 24
for x, n in [(8, 4), (40, 7)]:
    s = n * c
    poly(ax, [(x, y), (x + s, y), (x + s, y + s), (x, y + s)], 'sujet')
    for i in range(1, n):
        line(ax, [(x + i * c, y), (x + i * c, y + s)], 'sujet', lw=0.4)
        line(ax, [(x, y + i * c), (x + s, y + i * c)], 'sujet', lw=0.4)
    text(ax, x + s / 2, y + s + 3, f'côté {n} m', 'sujet', 's')
    text(ax, x + s / 2, y - 4, f'aire {n * n} m²', 'sujet', 'm')
    text(ax, x + s / 2, y - 11, f'{n * n} est le carré de {n}', 'encre', 's')
save(fig, '23-009')
