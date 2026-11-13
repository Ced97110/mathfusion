import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
u = 4; x0 = 14
y = 56
box(ax, x0, y, 5 * u, 5 * u, 'sujet', True, label=r'$x^2$', r=0.3)
box(ax, x0 + 5 * u, y, 4 * u, 5 * u, 'fixe', True, label=r'$4x$', r=0.3)
text(ax, x0 - 3, y + 2.5 * u, r'$x$', 'sujet', 's'); text(ax, x0 + 2.5 * u, y + 5 * u + 2.5, r'$x$', 'sujet', 's')
text(ax, x0 + 7 * u, y + 5 * u + 2.5, '4', 'fixe', 's')
text(ax, x0 + 9 * u + 4, y + 2.5 * u, r'$x\times(x+4)$', 'encre', 'm', ha='left')
y = 12
box(ax, x0, y, 9 * u, 5 * u, 'fixe', True, label=r'$9x$', r=0.3)
text(ax, x0 - 3, y + 2.5 * u, r'$x$', 'sujet', 's'); text(ax, x0 + 4.5 * u, y + 5 * u + 2.5, '9', 'fixe', 's')
text(ax, x0 + 9 * u + 4, y + 3.5 * u, r'$9\times x$', 'encre', 'm', ha='left')
text(ax, x0 + 9 * u + 4, y + 1.5 * u, 'pas de carré', 'limite', 's', ha='left')
save(fig, '23-004')
