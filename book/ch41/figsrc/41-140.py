import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
k = 5.0
O = (44, 4)
Q = lambda c: (O[0] + c[0] * k, O[1] + c[1] * k)
arrow(ax, O, Q((4, 2)), 'autre', lw=1.5)
arrow(ax, O, Q((-1, 2)), 'resultat', lw=1.5)
a = (4 / 20 ** 0.5, 2 / 20 ** 0.5); b = (-1 / 5 ** 0.5, 2 / 5 ** 0.5); s = 3.0
sq = [(O[0] + s * a[0], O[1] + s * a[1]), (O[0] + s * (a[0] + b[0]), O[1] + s * (a[1] + b[1])), (O[0] + s * b[0], O[1] + s * b[1])]
ax.plot([p[0] for p in sq], [p[1] for p in sq], color=COL['encre'], lw=0.9, zorder=4)
text(ax, 71, 17, r'$v=\langle 4,2\rangle$', 'autre', 's')
text(ax, 28, 17, r'$u_2=\langle -1,2\rangle$', 'resultat', 's')
box(ax, 4, 46, 36, 9, 'fixe', label=r'$(-1)\times4=-4$', size='s')
box(ax, 48, 46, 36, 9, 'fixe', label=r'$2\times2=4$', size='s')
box(ax, 24, 29, 40, 9, 'resultat', label=r'$u_2\cdot v=-4+4=0$', size='m')
arrow(ax, (22, 45.5), (34, 38.5), 'fixe')
arrow(ax, (66, 45.5), (54, 38.5), 'fixe')
save(fig, '41-140')
