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
fig, ax = canvas(68)
rows = [(48, 'écriture de départ', [('(1 3 5 8)', 18, 'sujet', 0), ('(2 6)', 12, 'autre', 0)]),
        (28, 'ordre échangé', [('(2 6)', 12, 'autre', 0), ('(1 3 5 8)', 18, 'sujet', 0)]),
        (8, 'cycles à un nombre ajoutés', [('(1 3 5 8)', 18, 'sujet', 0), ('(2 6)', 12, 'autre', 0), ('(4)', 9, 'fixe', 1), ('(7)', 9, 'fixe', 1)])]
for y, lab, items in rows:
    text(ax, 3, y + 12, lab, 'encre', 's', ha='left')
    x = 3
    for s, w, role, dash in items:
        box(ax, x, y, w, 9, role, label=s, size='s', dash=bool(dash)); x += w + 2
    arrow(ax, (x - 0.5, y + 4.5), (61, y + 4.5), 'fixe')
box(ax, 62, 8, 24, 49, 'resultat', label='même mélange')
save(fig, '46-174')
