import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$x_2$ s’approche de $1$', 'varie', 'm')
text(ax, 20, 62, r'$x_2$', 'varie', 'm'); text(ax, 66, 62, 'pente', 'resultat', 'm')
for i, (a, b) in enumerate([('1,1', '2,1'), ('1,01', '2,01'), ('1,001', '2,001')]):
    y = 44 - i * 17
    box(ax, 6, y, 28, 11, 'varie', label=a)
    arrow(ax, (36, y + 5.5), (52, y + 5.5), 'fixe')
    box(ax, 54, y, 28, 11, 'resultat', label=b)
arrow(ax, (3, 56), (3, 6), 'varie')
save(fig, '21-144')
