import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
o = (16, 14); u = 26
P = lambda a, b: (o[0] + a * u, o[1] + b * u)
arrow(ax, P(0, 0), P(1.0, 0), 'fixe'); arrow(ax, P(0, 0), P(0, 1.0), 'fixe')
line(ax, [P(1, 0), P(1, 1)], 'fixe', dash=True); line(ax, [P(0, 1), P(1, 1)], 'fixe', dash=True)
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.4)
text(ax, P(1, 0)[0] + 2, P(1, 0)[1] - 4, r'$e_1$', 'fixe', 'm', ha='left')
text(ax, P(0, 1)[0] - 2, P(0, 1)[1] + 3, r'$e_2$', 'fixe', 'm', ha='right')
text(ax, P(1, 1)[0] + 2, P(1, 1)[1] + 3, r'$u_1 = e_1 + e_2$', 'varie', 'm', ha='left')
text(ax, 60, 22, r'$B(e_1, e_1) = 0$', 'fixe', 's')
text(ax, 60, 14, r'$B(e_2, e_2) = 0$', 'fixe', 's')
box(ax, 48, 53, 38, 9, 'resultat', label=r'$B(u_1, u_1) = 2 \neq 0$')
save(fig, '71-164')
