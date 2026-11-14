import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 44, 20, 11, 'fixe', label=r'$x^2-x$', size='s')
text(ax, 24, 49.5, '=', 'encre', 'm')
box(ax, 26, 44, 16, 11, 'sujet', label=r'$x$', size='m')
box(ax, 46, 44, 16, 11, 'autre', label=r'$x-1$', size='m')
f = numberline(ax, 14, 74, 20, -1, 2, 1)
for v, c in ((0, 34), (1, 54)):
    pass
arrow(ax, (34, 43), (f(0), 23), 'sujet')
arrow(ax, (54, 43), (f(1), 23), 'autre')
text(ax, 40.5, 33, r'$x=0$', 'sujet', 's'); text(ax, 61, 33, r'$x=1$', 'autre', 's')
disc(ax, f(0), 20, 1.6, 'limite'); disc(ax, f(1), 20, 1.6, 'limite')
text(ax, 44, 5, 'valeurs interdites', 'limite', 's')
save(fig, '21-119')
