import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for i in range(5): box(ax, 6, 47 - 7.5 * i, 30, 5.5, 'sujet', label=r'$x$')
box(ax, 6, 5, 20, 5.5, 'autre', label=r'$y$')
line(ax, [(36, 15), (36, 54)], 'fixe', dash=True)
text(ax, 41, 32, 'même lettre, même longueur', 'sujet', 's', ha='left')
text(ax, 30, 8, 'autre lettre : peut différer', 'autre', 's', ha='left')
save(fig, '15-009')
