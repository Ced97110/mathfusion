import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, 'un disque = un facteur −1', 'encre', 'm')
for row, n in enumerate([2, 3, 4]):
    y = 40 - row * 16
    pair = n % 2 == 0
    role = 'resultat' if pair else 'varie'
    text(ax, 12, y, f'n = {n}', 'encre', 's')
    for i in range(n):
        x = 28 + i * 8.5
        disc(ax, x, y, 3.4, 'sujet')
        line(ax, [(x - 1.7, y), (x + 1.7, y)], 'sujet', lw=1.1)
    text(ax, 72, y, '= +1' if pair else '= −1', role, 'l')
save(fig, '32-053')
