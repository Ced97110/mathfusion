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
fig, ax = canvas(70)
xs = [14, 31, 48, 65]; ns = ['1', '3', '5', '8']
for y, rd_role in [(46, 'resultat'), (14, 'limite')]:
    for k, (x, n) in enumerate(zip(xs, ns)):
        disc(ax, x, y, 4, 'sujet', label=n)
        if k: arrow(ax, (xs[k - 1] + 4.6, y), (x - 4.6, y), 'fixe')
arrow(ax, (65, 50.8), (14, 50.8), 'resultat', curve=0.3)
text(ax, 39, 64, 'vrai : 8 revient sur 1', 'resultat', 'm')
arrow(ax, (65, 18.8), (31, 18.8), 'limite', curve=0.35)
text(ax, 48, 30, 'faux : 1 et 8 donnent 3', 'limite', 'm')
save(fig, '46-176')
