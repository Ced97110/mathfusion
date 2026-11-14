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
fig, ax = canvas(88)
yc = 66
text(ax, 44, 83, 'disjoints : même fin', 'resultat', 'm')
disc(ax, 9, yc, 4, 'sujet', label='1'); disc(ax, 79, yc, 4, 'resultat', label='3')
arrow(ax, (13.5, yc + 1), (74.5, yc + 1), 'varie', curve=-0.25); arrow(ax, (13.5, yc - 1), (74.5, yc - 1), 'autre', curve=0.25)
text(ax, 44, yc + 9.5, '(2 6) puis (1 3 5 8)', 'varie', 's'); text(ax, 44, yc - 9.5, '(1 3 5 8) puis (2 6)', 'autre', 's')
yc = 24
text(ax, 44, 42, r'non disjoints : fins $\neq$', 'limite', 'm')
disc(ax, 9, yc, 4, 'sujet', label='1'); disc(ax, 79, yc + 9, 4, 'limite', label='2'); disc(ax, 79, yc - 9, 4, 'limite', label='3')
arrow(ax, (13.3, yc + 1), (74.8, yc + 8), 'varie'); arrow(ax, (13.3, yc - 1), (74.8, yc - 8), 'autre')
text(ax, 40, yc + 10.5, '(1 2) puis (1 3)', 'varie', 's'); text(ax, 40, yc - 10.5, '(1 3) puis (1 2)', 'autre', 's')
save(fig, '46-171')
