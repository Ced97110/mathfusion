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
text(ax, 44, 55, '(2 6)', 'sujet', 'xl')
text(ax, 2, 41, 'avant', 'fixe', 's', ha='left'); text(ax, 2, 11, 'après', 'fixe', 's', ha='left')
for i in range(8):
    n = i + 1; x = 16 + i * 9.0; mv = n in (2, 6)
    box(ax, x - 3.8, 36, 7.6, 8, 'varie' if mv else 'fixe', label=str(n))
    box(ax, x - 3.8, 6, 7.6, 8, 'varie' if mv else 'fixe', label=str(n) if False else str({2: 6, 6: 2}.get(n, n)))
    if not mv: line(ax, [(x, 35.5), (x, 14.5)], 'fixe', dash=True)
f = lambda n: 16 + (n - 1) * 9.0
arrow(ax, (f(2) + 1, 35.5), (f(6) - 1, 14.5), 'varie'); arrow(ax, (f(6) - 1, 35.5), (f(2) + 1, 14.5), 'varie')
text(ax, 50, 1.5, 'pointillés : restent en place', 'fixe', 's')
save(fig, '46-166')
