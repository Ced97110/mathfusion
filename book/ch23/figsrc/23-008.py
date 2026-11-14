import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 6.5; X = 5 * u; B = 3 * u; ox = 18; oy = 16
box(ax, ox, oy, X, X, 'sujet', True, label=r'$x^2$', size='l')
box(ax, ox + X, oy, B, X, 'fixe', True, label=r'$3x$')
box(ax, ox, oy + X, X, B, 'fixe', True, label=r'$3x$')
box(ax, ox + X, oy + X, B, B, 'varie', False, dash=True)
text(ax, ox + X + B / 2, oy + X + B / 2, '9', 'varie', 'l')
text(ax, ox + X / 2, oy - 3.5, r'$x$', 'sujet', 's'); text(ax, ox + X + B / 2, oy - 3.5, '3', 'fixe', 's')
text(ax, ox - 4, oy + X / 2, r'$x$', 'sujet', 's'); text(ax, ox - 4, oy + X + B / 2, '3', 'fixe', 's')
text(ax, 44, 5, r'$x^2+6x$ : il manque le coin 9', 'encre', 'm')
save(fig, '23-008')
