import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ax_x, y0, u = 30, 34, 9
arrow(ax, (ax_x, y0 - 3.5 * u), (ax_x, y0 + 3.8 * u), 'sujet')
for v in range(-3, 4):
    line(ax, [(ax_x - 1.6, y0 + v * u), (ax_x + 1.6, y0 + v * u)], 'sujet'); text(ax, ax_x - 5, y0 + v * u, f'{v}'.replace('-', '−'), 'sujet', 's')
text(ax, ax_x + 4, y0 + 3.8 * u, r'$y$', 'sujet', 'l', ha='left')
text(ax, ax_x + 6, y0 + 2 * u, 'au-dessus de 0', 'fixe', 's', ha='left'); text(ax, ax_x + 6, y0 - 2 * u, 'en dessous de 0', 'fixe', 's', ha='left')
text(ax, ax_x + 6, y0, 'on y lit le 2e nombre', 'sujet', 's', ha='left')
text(ax, 44, 4, r'axe des $y$', 'sujet', 'l')
save(fig, '19-014')
