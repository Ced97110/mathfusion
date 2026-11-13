import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for y, a, b in ((34, '5', '6'), (16, '3', '10')):
    box(ax, 3, y, 30, 10, 'fixe', label=rf'$n_{a} \in \{{1, {b}\}}$', size='m')
    arrow(ax, (34, y + 5), (55, y + 5), 'limite')
    text(ax, 44.5, y + 9, r'$\neq 1$', 'limite', 'm')
    box(ax, 56, y, 28, 10, 'varie', label=rf'$n_{a} = {b}$', size='l')
text(ax, 44, 4, 'hypothèse à réfuter', 'varie', 'm')
save(fig, '50-185')
