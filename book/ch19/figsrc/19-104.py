import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
gx = lambda x: 8 + x * 14; gy = lambda y: 8 + y * 14
A, B, C = (gx(1), gy(1)), (gx(4), gy(3)), (gx(4), gy(1))
line(ax, [(gx(0.4), gy(1) - 0.6 * 2 / 3 * 14), (gx(4.6), gy(3) + 0.6 * 2 / 3 * 14)], 'sujet', lw=1.2)
arrow(ax, A, C, 'resultat', lw=2.0); arrow(ax, C, B, 'varie', lw=2.0)
line(ax, [(C[0] - 2.5, C[1]), (C[0] - 2.5, C[1] + 2.5), (C[0], C[1] + 2.5)], 'fixe')
disc(ax, *A, 1.2, 'sujet'); disc(ax, *B, 1.2, 'sujet')
text(ax, A[0] - 2, A[1] + 4, r'$A$', 'sujet', 'l', ha='right'); text(ax, B[0] - 2.5, B[1] + 3, r'$B$', 'sujet', 'l', ha='right')
text(ax, (A[0] + C[0]) / 2, A[1] - 4, 'avancée 3', 'resultat', 'm')
text(ax, C[0] + 3, (C[1] + B[1]) / 2, 'montée 2', 'varie', 'm', ha='left')
text(ax, C[0] + 2, C[1] - 4, r'$(4,\,1)$', 'fixe', 's', ha='left')
box(ax, 4, 54, 56, 11, 'sujet', label=r'pente $=\frac{2}{3}$ : orange / vert', size='s')
save(fig, '19-104')
