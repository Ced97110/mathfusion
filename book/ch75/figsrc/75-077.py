import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 14
text(ax, 44, 74, r'même direction $u$', 'resultat', 's')
arrow(ax, (8, 64), (8 + 2 * u, 64), 'varie', lw=1.3); text(ax, 8 + u, 68, r'$\tau_{u,c}$', 'varie', 's')
arrow(ax, (8 + 2 * u, 64), (8 + 3.2 * u, 64), 'autre', lw=1.3); text(ax, 8 + 2.6 * u, 68, r"$\tau_{u,c'}$", 'autre', 's')
brace(ax, 8, 8 + 3.2 * u, 60, 'resultat', label=r"$\tau_{u,c+c'}$ : $c+c'$")
line(ax, [(4, 40), (84, 40)], 'fixe', dash=True)
text(ax, 44, 34, 'directions différentes', 'limite', 's')
arrow(ax, (16, 8), (16 + 2 * u, 8), 'varie', lw=1.3); text(ax, 16 + u, 4, r'$\tau_{e,1}$', 'varie', 's')
arrow(ax, (16 + 2 * u, 8), (16 + 2 * u, 8 + 1.2 * u), 'autre', lw=1.3); text(ax, 16 + 2 * u - 2, 8 + 0.6 * u, r'$\tau_{f,1}$', 'autre', 's', ha='right')
line(ax, [(16 + 2 * u + 2, 8 + 0.6 * u), (53.5, 8 + 0.6 * u)], 'limite', dash=True)
box(ax, 54, 14, 30, 9, 'limite', label='pas de somme', size='s')
save(fig, '75-077')
