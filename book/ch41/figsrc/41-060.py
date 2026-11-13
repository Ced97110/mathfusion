import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 0.3
O = (6, 24)
u, v = (180, 0), (50, 86.6)
T = lambda p, q: (p[0] + k * q[0], p[1] + k * q[1])
U, V, S = T(O, u), T(O, v), T(O, (230, 86.6))
assert abs((U[0] + k * v[0]) - S[0]) < 1e-9 and abs((V[0] + k * u[0]) - S[0]) < 1e-9
arrow(ax, O, U, 'sujet', lw=1.8)
arrow(ax, U, S, 'autre', lw=1.8)
arrow(ax, O, V, 'autre', lw=1.8)
arrow(ax, V, S, 'sujet', lw=1.8)
arrow(ax, O, S, 'resultat', lw=1.2)
text(ax, 32, 20, r'$u$ puis $v$', 'fixe', 's')
text(ax, 16, 40, r'$v$ puis $u$', 'fixe', 's', ha='right')
text(ax, 44, 36, r'$u+v=v+u$', 'resultat', 's')
text(ax, 44, 11, r'$180+50=50+180=230$', 'encre', 's')
text(ax, 44, 4, r'$0+86{,}60=86{,}60+0$', 'encre', 's')
save(fig, '41-060')
