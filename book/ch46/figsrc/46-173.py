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
text(ax, 44, 65, 'mélange = boucles séparées', 'sujet', 'm')
ring(ax, 26, 46, 10, ['1', '3', '5', '8'], 'sujet', rd=4)
ring(ax, 66, 46, 8, ['2', '6'], 'autre', rd=4, arrow_role='varie')
text(ax, 26, 29, '(1 3 5 8)', 'sujet', 's'); text(ax, 66, 29, '(2 6)', 'autre', 's')
for x, n in [(26, '4'), (58, '7')]:
    disc(ax, x, 14, 4, 'fixe', label=n); selfloop(ax, x, 14, 4, 'fixe'); text(ax, x + 9, 14, f'({n})', 'fixe', 's')
text(ax, 44, 3.5, '4 + 2 + 1 + 1 = 8 cartes', 'resultat', 's')
save(fig, '46-173')
