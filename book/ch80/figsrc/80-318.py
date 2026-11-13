import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 6; x0, y0 = 27, 6
box(ax, x0, y0 + 3 * u, 2 * u, 2 * u, 'sujet', label='4', size='l')
box(ax, x0 + 2 * u, y0 + 3 * u, 3 * u, 2 * u, 'varie', label='6', size='l')
box(ax, x0, y0, 2 * u, 3 * u, 'varie', label='6', size='l')
box(ax, x0 + 2 * u, y0, 3 * u, 3 * u, 'autre', label='9', size='l')
brace(ax, x0, x0 + 2 * u, y0 + 5 * u + 1, 'sujet', label='2', down=False)
brace(ax, x0 + 2 * u, x0 + 5 * u, y0 + 5 * u + 1, 'autre', label='3', down=False)
text(ax, 22, y0 + 4 * u, '2', 'sujet', 'm'); text(ax, 22, y0 + 1.5 * u, '3', 'autre', 'm')
text(ax, 73, 34, r'$(2 + 3)^2 = 25$', 'sujet', 'm'); text(ax, 73, 20, r'$4+6+6+9 = 25$', 'resultat', 'm')
save(fig, '80-318')
