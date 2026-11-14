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
fig, ax = canvas(60)
text(ax, 44, 55, '(1 3 5 8)', 'sujet', 'xl')
for i in range(8):
    n = i + 1; mv = n in (1, 3, 5, 8); x = 5 + i * 10.5
    box(ax, x, 12, 8.5, 9, 'varie' if mv else 'fixe', label=str(n))
    if mv: arrow(ax, (44 + (x + 4.25 - 44) * 0.2, 51), (x + 4.25, 22), 'sujet')
text(ax, 26, 6, 'écrits : ils bougent', 'varie', 's'); text(ax, 68, 6, 'absents : immobiles', 'fixe', 's')
save(fig, '46-164')
