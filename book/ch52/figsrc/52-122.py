import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 22, 72, r'dans $R/P$', 'autre', 's'); text(ax, 66, 72, r'dans $R$', 'sujet', 's')
rows = [(r'$\bar a\bar b=\bar0$', r'$ab\in P$'), (r'$\bar a=\bar0$', r'$a\in P$'), (r'$\bar1\neq\bar0$', r'$P\neq R$')]
for k, (l, r) in enumerate(rows):
    y = 56 - 18 * k
    box(ax, 4, y, 36, 12, 'autre', label=l); box(ax, 48, y, 36, 12, 'sujet', label=r)
    arrow(ax, (40.5, y + 6), (47.5, y + 6), 'varie', both=True)
save(fig, '52-122')
