import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
y = 14
f = numberline(ax, 6, 70, y, -8, 8, every=8, arrow_right=False)
for v, r in ((3, 'sujet'), (-3, 'autre'), (8, 'sujet'), (-8, 'autre')):
    disc(ax, f(v), y, 1.6, r)
text(ax, f(3), y - 4, '3', 'sujet', 's'); text(ax, f(-3), y - 4, r'$-3$', 'autre', 's')
arrow(ax, (f(-3), y + 2), (f(3), y + 2), 'varie', curve=-0.5, both=True)
arrow(ax, (f(-8), y + 2), (f(8), y + 2), 'varie', curve=-0.3, both=True)
text(ax, f(0), 33, 'chaque nombre et son opposé', 'encre', 's')
save(fig, '13-031')
