import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, X1 = 26, 86
text(ax, 2, 52, 'modulo 1', 'sujet', 'm', ha='left')
box(ax, X0, 47, X1 - X0, 11, 'sujet', label='tous les entiers ensemble', size='s')
text(ax, 2, 32, 'modulo 12', 'fixe', 'm', ha='left')
for i in range(12):
    box(ax, X0 + i * 5, 27, 4.2, 10, 'fixe', r=0.5)
text(ax, 56, 22.5, '12 classes', 'fixe', 's')
text(ax, 2, 10, 'modulo 0', 'varie', 'm', ha='left')
text(ax, X0 + 1.5, 10, '…', 'varie', 'm')
for i, v in enumerate(['−2', '−1', '0', '1', '2']):
    box(ax, X0 + 5 + i * 10.2, 5, 9, 10, 'varie', label=v, size='s')
text(ax, X1 - 1.5, 10, '…', 'varie', 'm')
text(ax, 56, 1.8, 'un entier par classe', 'varie', 's')
save(fig, '43-141')
