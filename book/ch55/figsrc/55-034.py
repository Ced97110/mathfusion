import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$1 + 0\cdot x + 2x^2$', 'sujet', 'l')
arrow(ax, (44, 54), (44, 42), 'varie')
text(ax, 48, 48, 'on range', 'varie', 's', ha='left')
for k, (v, p) in enumerate([('1', r'$x^0$'), ('0', r'$x^1$'), ('2', r'$x^2$')]):
    x = 20 + k * 17
    box(ax, x, 29, 14, 11, 'sujet', label=v)
    text(ax, x + 7, 24.5, p, 'fixe', 's')
text(ax, 44, 15, r'$x$ : aucun nombre, juste une place', 'fixe', 's')
text(ax, 44, 7, r'$F[x]$ : toutes ces listes', 'sujet', 'm')
save(fig, '55-034')
