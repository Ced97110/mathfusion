import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
n = lambda v: str(v).replace('-', '−')
t3 = lambda t: '(' + ', '.join(n(v) for v in t) + ')'
f = lambda x1, x2: (x1, 2 * x1 + x2, x1 - x2)
text(ax, 20, 61, 'deux paramètres', 'varie', 'm')
text(ax, 68, 61, r'triplet de $W$', 'sujet', 'm')
for (x1, x2), y in zip([(1, 0), (0, 1), (2, 3)], [46, 34, 22]):
    box(ax, 2, y, 36, 9, 'varie', label=rf'$x_1={x1}$ ; $x_2={x2}$')
    arrow(ax, (40, y + 4.5), (52, y + 4.5), 'sujet')
    box(ax, 54, y, 30, 9, 'sujet', label=t3(f(x1, x2)))
box(ax, 2, 5, 36, 9, 'limite', fill=False, dash=True, label='aucun couple')
text(ax, 46, 9.5, '×', 'limite', 'l')
box(ax, 54, 5, 30, 9, 'limite', label=t3((1, 0, 0)))
save(fig, '58-121')
