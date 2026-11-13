import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 8; r2, r3, r5 = 2 ** 0.5, 3 ** 0.5, 5 ** 0.5; y = 14
text(ax, 17, y + r3 * u + 4, 'aires 2 et 3', 'fixe', 's')
box(ax, 4, y, r2 * u, r2 * u, 'sujet', label='2', size='s')
box(ax, 4 + r2 * u, y, r3 * u, r3 * u, 'autre', label='3', size='s')
brace(ax, 4, 4 + (r2 + r3) * u, y - 1, 'fixe', r'$\approx3{,}146$', down=True)
arrow(ax, (32, y + 13), (42, y + 13), 'varie')
S = (r2 + r3) * u
box(ax, 44, y, S, S, 'varie')
text(ax, 44 + S / 2, y + S - 3.4, r'aire $\approx9{,}9$', 'varie', 's')
box(ax, 44, y, r5 * u, r5 * u, 'limite', fill=False, dash=True, label='aire 5', size='s')
text(ax, 44 + S / 2, y - 3, r'côté $\approx3{,}146$', 'fixe', 's')
save(fig, '22-105')
