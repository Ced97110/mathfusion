import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u = 9.0
fig, ax = canvas(78)
box(ax, 6, 64, u, 8, 'sujet'); text(ax, 6 + u + 2, 68, 'aire 1', 'sujet', 'm', ha='left')
arrow(ax, (10, 63.5), (10, 55.5), 'varie'); text(ax, 14, 59.5, r'$B$ : $\times2$', 'varie', 's', ha='left')
box(ax, 6, 46, 2 * u, 8, 'varie'); text(ax, 6 + 2 * u + 2, 50, 'aire 2', 'varie', 'm', ha='left')
arrow(ax, (10, 45.5), (10, 37.5), 'autre'); text(ax, 14, 41.5, r'$A$ : $\times3$', 'autre', 's', ha='left')
box(ax, 6, 28, 6 * u, 8, 'resultat', label=r'aire 6 $=\det A\times\det B$', size='s')
arrow(ax, (46, 27.5), (46, 20.5), 'varie')
box(ax, 4, 4, 80, 16, 'varie', label=r'$\eta(AB)=\eta(A)\,\eta(B)$', size='m', weight='bold')
save(fig, '76-109')
