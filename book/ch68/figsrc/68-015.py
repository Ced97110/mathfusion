import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
xs = [14, 44, 74]
for x, w in zip(xs, ['000', '100', '110']):
    disc(ax, x, 28, 5.5, 'sujet', label=w)
arrow(ax, (19.8, 28), (38.2, 28), 'varie', lw=1.3)
arrow(ax, (49.8, 28), (68.2, 28), 'varie', lw=1.3)
text(ax, 29, 33, '1 arête :\nbit 1 inversé', 'varie', 's')
text(ax, 59, 33, '1 arête :\nbit 2 inversé', 'varie', 's')
arrow(ax, (14, 22.3), (74, 22.3), 'limite', curve=0.3)
text(ax, 44, 7, '000 et 110 : 2 bits diffèrent, pas d’arête', 'limite', 's')
text(ax, 44, 44, 'une arête = un seul bit change', 'sujet', 'm')
save(fig, '68-015')
