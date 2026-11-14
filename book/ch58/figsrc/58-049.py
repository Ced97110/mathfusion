import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 52, r'$R^{(n)}$', 'sujet', 22)
cw, ch = 9.0, 8.0
def cells(x, y, n):
    for i in range(n): box(ax, x + i * cw, y, cw, ch, 'sujet', label=r'$x_%d$' % (i + 1), r=0.6)
cells(6, 18, 2)
cells(44, 18, 4)
arrow(ax, (36, 44), (15, 28), 'varie', lw=1.1)
arrow(ax, (52, 44), (62, 28), 'varie', lw=1.1)
text(ax, 18, 38, r'$n=2$', 'varie', 'm')
text(ax, 66, 38, r'$n=4$', 'varie', 'm')
text(ax, 20, 7, r'$R$ : nature des cases', 'sujet', 's')
text(ax, 66, 7, r'$n$ : nombre de cases', 'varie', 's')
save(fig, '58-049')
