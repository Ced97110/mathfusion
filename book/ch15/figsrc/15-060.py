import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
for i, t in enumerate([r'$9x^2$', r'$-\,50x$', r'$-\,13$']):
    x = 3 + i * 27
    box(ax, x, 22, 24, 10, 'sujet', label=t)
    disc(ax, x + 12, 42, 3, 'varie', label=str(i + 1))
    arrow(ax, (x + 12, 38.5), (x + 12, 32.8), 'varie')
brace(ax, 3, 81, 21.4, 'sujet', '3 termes')
box(ax, 28, 2, 32, 9, 'sujet', label='trinôme', size='l')
save(fig, '15-060')
