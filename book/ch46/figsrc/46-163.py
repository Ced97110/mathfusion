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
fig, ax = canvas(52)
text(ax, 44, 46, r'$\gamma = (i_1\ i_2\ \cdots\ i_r)$', 'sujet', 'xl')
xs = [14, 32, 50, 70]; top = [r'$i_1$', r'$i_2$', r'$\cdots$', r'$i_r$']; bot = ['1', '3', '5', '8']
for x, t, b in zip(xs, top, bot):
    box(ax, x - 7, 28, 14, 9, 'sujet', label=t)
    box(ax, x - 7, 6, 14, 9, 'resultat', label=b)
    arrow(ax, (x, 27.5), (x, 15.5), 'varie')
save(fig, '46-163')
