import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 4, 36, 22, 0, 4, labels=False, arrow_right=False)
disc(ax, f(3), 22, 1.5, 'sujet'); text(ax, f(3), 30, 'point', 'sujet', 's')
text(ax, f(0), 16, r'$O$', 'fixe', 's')
arrow(ax, (42, 28), (61, 28), 'varie'); text(ax, 51.5, 32, 'coordonnée', 'varie', 's')
arrow(ax, (61, 17), (42, 17), 'varie'); text(ax, 51.5, 12.5, 'graphe', 'varie', 's')
box(ax, 63, 15, 20, 15, 'autre', label='3', size='xl'); text(ax, 73, 36, 'nombre', 'autre', 's')
save(fig, '12-061')
