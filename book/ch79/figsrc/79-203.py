import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ys = [10, 28, 46, 64]
text(ax, 22, 76, r'sous-groupes de $\mathbb{Z}/8$', 'sujet', 's')
text(ax, 72, 76, 'diviseurs de 8', 'autre', 's')
for i in range(3):
    line(ax, [(22, ys[i] + 4.5), (22, ys[i + 1] - 4.5)], 'fixe')
    line(ax, [(72, ys[i] + 4.5), (72, ys[i + 1] - 4.5)], 'fixe')
for y, lab, n in zip(ys, [r'$\{0\}$', r'$\{0,4\}$', r'$\{0,2,4,6\}$', r'$\mathbb{Z}/8$'], [1, 2, 4, 8]):
    box(ax, 9, y - 4.5, 26, 9, 'sujet', label=lab, size='s')
    disc(ax, 72, y, 4.5, 'autre', label=str(n), size='s')
    line(ax, [(36, y), (67, y)], 'fixe', dash=True)
    text(ax, 51.5, y + 3, 'ordre %d' % n, 'fixe', 's')
save(fig, '79-203')
