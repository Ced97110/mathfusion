import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 3.2; x0 = 10; y0 = 22
box(ax, x0, y0, 20 * u, 7 * u, 'sujet', label=r'$7 \times 20$', size='m')
box(ax, x0 + 20 * u, y0, 3 * u, 7 * u, 'varie', label=r'$7 \times 3$', size='s')
brace(ax, x0, x0 + 20 * u, y0, 'sujet', label='20')
brace(ax, x0 + 20 * u, x0 + 23 * u, y0, 'varie', label='3')
brace(ax, x0, x0 + 23 * u, y0 + 7 * u, 'fixe', label=r'$20 + 3 = 23$', down=False)
arrow(ax, (6, y0), (6, y0 + 7 * u), 'fixe', both=True); text(ax, 3, y0 + 3.5 * u, '7', 'encre', 'm')
save(fig, '10-057')
