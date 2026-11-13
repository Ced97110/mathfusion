import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, r'$G$ : horloge à 12', 'sujet', 'm')
rows = ['0   3   6   9', '1   4   7   10', '2   5   8   11']
ys = [46, 32, 18]
for t, y in zip(rows, ys):
    box(ax, 3, y - 6, 38, 12, 'sujet', label=t, size='s')
arrow(ax, (43, 32), (55, 32), 'varie')
text(ax, 49, 37, r'$/N$', 'varie', 'm')
text(ax, 71, 61, r'$G/N$', 'resultat', 'm')
for y, l in zip(ys, ['0', '1', '2']):
    disc(ax, 71, y, 5, 'resultat', label=l)
text(ax, 44, 5, r'$12\ \div\ 4 = 3$ éléments', 'encre', 's')
save(fig, '47-141')
