import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 14, 64, r'$a$', 'encre', 'l')
text(ax, 46, 64, r'$\eta(a)$', 'encre', 'l')
items = [('3', '3', 'fixe'), ('1/2', '1/2', 'fixe'), (r'$\sqrt{2}$', r'$-\sqrt{2}$', 'varie')]
ys = [50, 38, 26]
for (a, b, r), y in zip(items, ys):
    box(ax, 7, y - 4, 14, 8, r, label=a)
    box(ax, 39, y - 4, 14, 8, r, label=b)
    arrow(ax, (23, y), (37, y), r)
line(ax, [(57, 54), (59, 54), (59, 34), (57, 34)], 'fixe')
text(ax, 72, 44, r'$\eta(a)=a$', 'fixe', 'm')
text(ax, 72, 26, 'bouge', 'varie', 'm')
text(ax, 44, 12, r'$\eta:\sqrt{2}\mapsto-\sqrt{2}$', 'encre', 'm')
save(fig, '63-038')
