import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (1, 3), (4, 2)
d = u[0] * v[0] + u[1] * v[1]
k = d / (v[0] ** 2 + v[1] ** 2)
u1 = (k * v[0], k * v[1])
u2 = (u[0] - u1[0], u[1] - u1[1])
assert u2[0] * v[0] + u2[1] * v[1] == 0
o = (12, 6); s = 8
P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
fig, ax = canvas(48)
arrow(ax, P((0, 0)), P(v), 'fixe', lw=0.8)
arrow(ax, P((0, 0)), P(u), 'sujet', lw=1.2)
arrow(ax, P((0, 0)), P(u1), 'resultat', lw=1.6)
arrow(ax, P(u1), P(u), 'varie', lw=1.6)
# angle droit en bout de u1
a = (v[0] / 4.4721, v[1] / 4.4721); b = (u2[0] / 2.2361, u2[1] / 2.2361); t = 0.35
c = (u1[0], u1[1])
line(ax, [P((c[0] + a[0] * -t, c[1] + a[1] * -t)), P((c[0] - a[0] * t + b[0] * t, c[1] - a[1] * t + b[1] * t)), P((c[0] + b[0] * t, c[1] + b[1] * t))], 'fixe')
text(ax, P(v)[0] + 2, P(v)[1] + 1.5, r'$v$', 'fixe')
text(ax, P(u)[0] - 2, P(u)[1] + 1.5, r'$u$', 'sujet')
text(ax, P(u1)[0] + 1, P(u1)[1] - 4.5, r'$u_1$', 'resultat')
text(ax, 29.5, 24, r'$u_2$', 'varie')
text(ax, 68, 38, r'$u=u_1+u_2$', 'encre', 'l')
text(ax, 68, 28, r'$u_1=\langle 2, 1\rangle$ (sur $v$)', 'resultat', 's')
text(ax, 68, 21, r'$u_2=\langle -1, 2\rangle$ ($\perp v$)', 'varie', 's')
text(ax, 68, 12, r'$u_2\cdot v=-4+4=0$', 'encre', 's')
save(fig, '41-100')
