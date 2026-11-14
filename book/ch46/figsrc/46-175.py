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
fig, ax = canvas(74)
rows = [(62, [1, 3, 5, 8]), (46, [2, 6]), (30, [4]), (14, [7])]
for y, ns in rows:
    text(ax, 3, y, f'départ {ns[0]}', 'encre', 's', ha='left')
    xs = [30 + 11 * k for k in range(len(ns))]
    for k, (x, n) in enumerate(zip(xs, ns)):
        disc(ax, x, y, 3.6, 'varie' if k == 0 else 'sujet', label=str(n), size='s')
        if k: arrow(ax, (xs[k - 1] + 4.2, y), (x - 4.2, y), 'fixe')
    if len(ns) > 1: arrow(ax, (xs[-1], y + 4.2), (xs[0], y + 4.2), 'resultat', curve=0.3)
    else: selfloop(ax, xs[0], y, 3.6, 'resultat')
text(ax, 74, 70, 'retour au départ', 'resultat', 's')
text(ax, 44, 3.5, 'boucles toutes séparées', 'sujet', 's')
save(fig, '46-175')
