import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'Trois chemins : le même corps ?', 'encre', 'l')
ys = [44, 28, 12]
paths = [r'$\sqrt[3]{2}$ d’abord, puis $j$', r'$j$ d’abord, puis $\sqrt[3]{2}$', r'$j\sqrt[3]{2}$ d’abord']
box(ax, 2, 24, 12, 10, 'fixe', label=r'$\mathbb{Q}$')
for i, y in enumerate(ys):
    arrow(ax, (14, 29), (23, y + 4), 'fixe')
    box(ax, 24, y - 1, 38, 10, 'varie', label=paths[i], size='s')
    arrow(ax, (62, y + 4), (68, y + 4), 'varie')
    box(ax, 69, y - 1, 17, 10, 'sujet', label=r'$E_%d$' % (i + 1))
save(fig, '62-067')
