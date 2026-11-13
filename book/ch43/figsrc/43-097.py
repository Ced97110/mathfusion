import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = [(58, (3, 6), 0), (38, (1, 4), 1), (18, (2, 5), 2)]
for y, (a, b), t in rows:
    for x, n in ((8, a), (19, b)):
        disc(ax, x, y, 3.8, 'sujet', label=str(n))
    arrow(ax, (24, y), (31, y), 'varie')
    box(ax, 32, y - 6, 22, 12, 'autre', label=r'$\{%d,\ %d\}$' % (a, b))
    arrow(ax, (55, y), (67, y), 'varie')
    disc(ax, 76, y, 4.5, 'resultat', label=str(t))
text(ax, 28, 70, '1. regrouper (surjection)', 'varie', 's')
text(ax, 64, 70, '2. placer (injection)', 'varie', 's')
save(fig, '43-097')
