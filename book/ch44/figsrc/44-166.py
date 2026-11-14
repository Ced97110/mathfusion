import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c, x0 = 8.5, 14
row2 = [0, 2, 4, 6, 0, 2, 4, 6]
text(ax, 44, 60, 'table modulo 8', 'fixe', 's')
for n, y in [(2, 44), (4, 33), (6, 22)]:
    text(ax, 7, y + c / 2, f'{n}', 'varie', 'm')
    for k in range(8):
        box(ax, x0 + k * c, y, c, c, 'varie', label=str(row2[k]) if n == 2 else None, r=0.2, size='s')
text(ax, 44, 13, 'tous les nombres sont pairs', 'varie', 's')
text(ax, 44, 6, '1 est impair : impossible', 'limite', 's')
save(fig, '44-166')
