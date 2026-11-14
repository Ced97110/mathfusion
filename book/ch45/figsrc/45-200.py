import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def tri(cx, vals, edges, role, title):
    P = [(cx, 48), (cx - 14, 20), (cx + 14, 20)]
    for (a, b), g in zip(((0, 1), (0, 2), (1, 2)), edges):
        (x1, y1), (x2, y2) = P[a], P[b]; L = math.hypot(x2 - x1, y2 - y1); u = (6.0 * (x2 - x1) / L, 6.0 * (y2 - y1) / L)
        line(ax, [(x1 + u[0], y1 + u[1]), (x2 - u[0], y2 - u[1])], role, lw=1.1)
        mx, my = (P[a][0] + P[b][0]) / 2, (P[a][1] + P[b][1]) / 2
        ox = -4 if (a, b) == (0, 1) else (4 if (a, b) == (0, 2) else 0)
        oy = 0 if a == 0 else -3.5
        text(ax, mx + ox, my + oy, str(g), role, 'm', weight='bold')
    for v, p in zip(vals, P):
        disc(ax, p[0], p[1], 5.5, 'sujet', label=str(v), size='m')
    text(ax, cx, 62, title, role, 's')
tri(22, (4, 3, 5), (1, 1, 1), 'resultat', 'toutes les paires : 1')
tri(66, (6, 10, 15), (2, 3, 5), 'limite', 'des paires partagent')
line(ax, [(44, 8), (44, 60)], 'fixe', dash=True, lw=0.6)
text(ax, 22, 8, 'deux à deux', 'resultat', 'm'); text(ax, 66, 8, 'pas deux à deux', 'limite', 'm')
save(fig, '45-200')
