import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(r'$5 + 0 = 5$', '0'), (r'$5 \times 1 = 5$', '1'), (r'$\alpha \circ 1_S = \alpha$', r'$1_S$')]
for (eq, n), y in zip(rows, [48, 30, 12]):
    text(ax, 16, y, eq, 'encre', 'm'); disc(ax, 44, y, 5, 'sujet', label=n, size='l'); arrow(ax, (49.5, y), (61, y), 'sujet')
box(ax, 62, 6, 24, 48, 'sujet', label='élément\nneutre\n(ne change\nrien)', size='m')
save(fig, '44-043')
