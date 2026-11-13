import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
P = {6: (44, 66), 10: (16, 22), 15: (72, 22)}
def mid(a, b, f): return (P[a][0] + (P[b][0] - P[a][0]) * f, P[a][1] + (P[b][1] - P[a][1]) * f)
for a, b, g in ((6, 10, 2), (6, 15, 3), (10, 15, 5)):
    (x1, y1), (x2, y2) = P[a], P[b]; L = math.hypot(x2 - x1, y2 - y1); u = (6.3 * (x2 - x1) / L, 6.3 * (y2 - y1) / L)
    line(ax, [(x1 + u[0], y1 + u[1]), (x2 - u[0], y2 - u[1])], 'limite', lw=1.1)
    mx, my = mid(a, b, 0.5)
    dx = -5 if a == 6 and b == 10 else (5 if a == 6 else 0)
    dy = 0 if a == 6 else -4
    box(ax, mx + dx - 6, my + dy - 3, 12, 6, 'limite', label=f'PGCD {g}', size='s', r=0.6)
for v, (x, y) in P.items():
    disc(ax, x, y, 6, 'sujet', label=str(v), size='m')
text(ax, 44, 40, 'PGCD des trois : 1', 'resultat', 's')
text(ax, 44, 8, 'ordre au plus 30, pas 900', 'limite', 'm')
text(ax, 44, 77, 'chaque paire a un diviseur', 'limite', 's')
save(fig, '45-199')
