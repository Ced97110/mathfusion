import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 34, 44, r'$x$', 'sujet', 'xl')
text(ax, 44, 44, r'$<$', 'varie', 'xl', weight='bold')
text(ax, 54, 44, r'$36$', 'autre', 'xl')
text(ax, 44, 38, 'x plus petit que 36', 'varie', 's')
f = numberline(ax, 6, 76, 16, 0, 40, step=5, every=2)
for v in (10, 25, 35):
    disc(ax, f(v), 16, 1.1, 'sujet'); text(ax, f(v), 21, f'{v}', 'sujet', 's')
disc(ax, f(36), 16, 1.1, 'autre'); text(ax, f(36) + 4.5, 21, '36', 'autre', 's')
brace(ax, f(0), f(36), 27, 'sujet', label=r'toutes les valeurs de $x$', down=False)
save(fig, '12-033')
