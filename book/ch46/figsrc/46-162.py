import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math as _m
def ring(ax, cx, cy, R, labels, role='sujet', rd=4.0, arrow_role='varie', size='m', roles=None, aroles=None, curve=-0.3):
    n = len(labels); P = []
    for k in range(n):
        a = _m.radians(90 - 360 * k / n); P.append((cx + R * _m.cos(a), cy + R * _m.sin(a)))
    for k, (x, y) in enumerate(P):
        disc(ax, x, y, rd, (roles or [role] * n)[k], label=labels[k], size=size)
    for k in range(n):
        p, q = P[k], P[(k + 1) % n]; d = _m.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
        arrow(ax, (p[0] + u[0] * (rd + .5), p[1] + u[1] * (rd + .5)), (q[0] - u[0] * (rd + .5), q[1] - u[1] * (rd + .5)),
              (aroles or [arrow_role] * n)[k], curve=curve)
    return P
def selfloop(ax, x, y, r, role='varie'):
    arrow(ax, (x - 1.4, y + r + .2), (x + 1.4, y + r + .2), role, curve=-1.7)
fig, ax = canvas(56)
P = ring(ax, 24, 30, 12, ['1', '3', '5', '8'], 'sujet', aroles=['varie', 'fixe', 'fixe', 'resultat'])
for (x, y), s in zip(P, [r'$i_1$', r'$i_2$', r'$i_3$', r'$i_r$']):
    dx = {0: 0, 1: 7, 2: 0, 3: -7}[P.index((x, y))]; dy = 7 if P.index((x, y)) == 0 else (-7 if P.index((x, y)) == 2 else 0)
    text(ax, x + dx, y + dy, s, 'fixe', 's')
text(ax, 62, 46, r'$\gamma(i_1) = i_2$', 'varie', 'm'); text(ax, 62, 40, '1 va sur 3', 'varie', 's')
text(ax, 62, 28, r'$\gamma(i_r) = i_1$', 'resultat', 'm'); text(ax, 62, 22, '8 va sur 1', 'resultat', 's')
disc(ax, 56, 8, 3.6, 'fixe', label='2'); selfloop(ax, 56, 8, 3.6, 'fixe'); text(ax, 72, 8, 'absent : reste', 'fixe', 's')
save(fig, '46-162')
