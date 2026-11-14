import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
k = 8.0
O = (22, 6)
Q = lambda c: (O[0] + c[0] * k, O[1] + c[1] * k)
u = (1, 3); v = (4, 2); u1 = (2, 1); u2 = (-1, 2)
H = Q(u1)
arrow(ax, O, Q(v), 'autre', lw=1.3)
arrow(ax, O, Q(u), 'sujet', lw=1.3)
arrow(ax, O, H, 'varie', lw=2.2)
arrow(ax, H, Q(u), 'resultat', lw=2.2)
# angle droit en H entre u2 et v
a = (4 / 20 ** 0.5, 2 / 20 ** 0.5); b = (-1 / 5 ** 0.5, 2 / 5 ** 0.5); s = 2.4
sq = [(H[0] + s * a[0], H[1] + s * a[1]), (H[0] + s * (b[0] + a[0]), H[1] + s * (b[1] + a[1])), (H[0] + s * b[0], H[1] + s * b[1])]
ax.plot([p[0] for p in sq], [p[1] for p in sq], color=COL['encre'], lw=0.9, zorder=6)
text(ax, 30, 35.5, r'$u=\langle 1,3\rangle$', 'sujet', 's')
text(ax, 55, 26, r'$v=\langle 4,2\rangle$', 'autre', 's')
text(ax, 41, 4, r'$u_1=\langle 2,1\rangle$', 'varie', 's')
text(ax, 13, 20, r'$u_2=\langle -1,2\rangle$', 'resultat', 's')
text(ax, 42, 12, r'$H$', 'encre', 's')
box(ax, 62, 6, 25, 16, 'fixe', label=r'$u\cdot v=10$' + '\n' + r'$\|v\|^2=20$' + '\n' + 'coefficient 0,5', size='s')
save(fig, '41-139')
