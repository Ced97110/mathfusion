import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
u = 3.4; x0 = 5
text(ax, 44, 81, r'$25 \times 23$', 'sujet', 'l')
brace(ax, x0, x0 + 23 * u, 70, 'sujet', label='23', down=False)
box(ax, x0, 60, 20 * u, 8, 'varie', label='20')
box(ax, x0 + 20 * u, 60, 3 * u, 8, 'autre', label='3', size='s')
box(ax, 4, 36, 42, 9, 'varie', label=r'$25 \times 20 = 500$', size='s')
box(ax, 52, 36, 32, 9, 'autre', label=r'$25 \times 3 = 75$', size='s')
arrow(ax, (x0 + 10 * u, 59), (25, 46), 'varie'); arrow(ax, (x0 + 21.5 * u, 59), (68, 46), 'autre')
box(ax, 22, 8, 44, 10, 'resultat', label=r'$500 + 75 = 575$')
arrow(ax, (25, 35), (38, 19), 'varie'); arrow(ax, (68, 35), (52, 19), 'autre')
save(fig, '10-062')
