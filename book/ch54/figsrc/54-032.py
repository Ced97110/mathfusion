import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
names = [r'$\mathbb{Z}$ (entiers)', 'polynômes', 'autre anneau intègre']
ys = [50, 33, 16]
for n, y in zip(names, ys):
    box(ax, 2, y, 38, 11, 'fixe', label=n, size='s')
    arrow(ax, (40, y + 5.5), (56, 35), 'varie')
box(ax, 56, 24, 28, 22, 'sujet', label=r'$D$', size='l')
text(ax, 70, 18, 'un nom pour tous', 'sujet', 's')
text(ax, 44, 63, 'Soit $D$ un anneau intègre', 'encre', 'm')
save(fig, '54-032')
