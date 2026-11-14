import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
P = {'A': (13, 62, '00000'), 'B': (75, 62, '00111'), 'C': (13, 14, '11100'), 'D': (75, 14, '11011')}
for cx, cy, w in P.values():
    box(ax, cx - 11, cy - 4, 22, 8, 'sujet', label=w)

def edge(p, q, t, lab, val):
    role = 'resultat' if val == 3 else 'fixe'
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    m = (p[0] + t * dx, p[1] + t * dy)
    h = min(3.2 / abs(ux) if ux else 99, 2.7 / abs(uy) if uy else 99)
    line(ax, [p, (m[0] - ux * h, m[1] - uy * h)], role, lw=1.2)
    line(ax, [(m[0] + ux * h, m[1] + uy * h), q], role, lw=1.2)
    box(ax, m[0] - 3, m[1] - 2.5, 6, 5, role, label=lab, size='m', r=0.5)

edge((24, 62), (64, 62), 0.5, '3', 3)
edge((13, 58), (13, 18), 0.5, '3', 3)
edge((75, 58), (75, 18), 0.5, '3', 3)
edge((24, 14), (64, 14), 0.5, '3', 3)
edge((24, 58), (64, 18), 0.25, '4', 4)
edge((64, 58), (24, 18), 0.25, '4', 4)
text(ax, 44, 77, r'$d=3$ : la plus petite des six', 'resultat', 'm')
save(fig, '68-061')
