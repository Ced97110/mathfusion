import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
c, x0 = 11, 24
res = [2, 4, 0, 2, 4]
text(ax, 44, 58, r'modulo 6, sans le 0', 'fixe', 's')
text(ax, 11, 42, r'$k$', 'fixe', 'm')
text(ax, 11, 24, r'$2\times k$', 'sujet', 'm')
for i in range(5):
    x = x0 + i * c
    box(ax, x, 37, c, 10, 'fixe', label=str(i + 1), r=0.3)
    arrow(ax, (x + c / 2, 37), (x + c / 2, 31), 'varie')
    box(ax, x, 21, c, 10, 'limite' if res[i] == 0 else 'sujet', label=str(res[i]), r=0.3)
text(ax, x0 + 2.5 * c, 12, '0 sort de l’ensemble', 'limite', 's')
text(ax, x0 + 2.5 * c, 6, 'le 1 n’apparaît jamais', 'limite', 's')
save(fig, '44-164')
