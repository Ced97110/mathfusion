import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, S = 12, 12, 17.0
X = lambda x, y: (ox + x * S, oy + y * S)
line(ax, [X(0, 0), X(3.5, 3.5)], 'fixe', lw=1.7, dash=True)
line(ax, [X(0, 0), X(3.6, 0)], 'fixe', lw=0.5); line(ax, [X(0, 0), X(0, 3.6)], 'fixe', lw=0.5)
def tick(p, q, n, role):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    for k in range(n):
        o = (k - (n - 1) / 2) * 1.2; cx, cy = mx + ux * o, my + uy * o
        line(ax, [(cx - uy * 1.6, cy + ux * 1.6), (cx + uy * 1.6, cy - ux * 1.6)], role, 1.0)
line(ax, [X(1, 3), X(2, 2)], 'sujet', lw=0.9); line(ax, [X(2, 2), X(3, 1)], 'varie', lw=0.9)
tick(X(1, 3), X(2, 2), 1, 'sujet'); tick(X(2, 2), X(3, 1), 1, 'varie')
tick(X(0, 0), X(1, 3), 2, 'sujet'); tick(X(0, 0), X(3, 1), 2, 'varie')
line(ax, [X(0, 0), X(1, 3)], 'sujet', lw=1.3); line(ax, [X(0, 0), X(3, 1)], 'varie', lw=1.3)
disc(ax, *X(1, 3), 1.3, 'sujet'); disc(ax, *X(3, 1), 1.3, 'varie'); disc(ax, *X(2, 2), 1.3, 'resultat'); disc(ax, *X(0, 0), 1.3, 'encre')
text(ax, X(1, 3)[0] + 2.5, X(1, 3)[1] + 2, r'$(1,\ 3)$', 'sujet', 'm', ha='left')
text(ax, X(3, 1)[0] + 2.5, X(3, 1)[1] + 3, r'$(3,\ 1)$', 'varie', 'm', ha='left')
text(ax, X(2, 2)[0] + 3, X(2, 2)[1] + 3, 'milieu', 'resultat', 's', ha='left')
text(ax, X(3.5, 3.5)[0] + 1.5, X(3.5, 3.5)[1] - 5, r'$y=x$', 'fixe', 'm', ha='left')
text(ax, X(0.35, 2.2)[0] - 2, X(0.35, 2.2)[1], r'$1^2+3^2=10$', 'sujet', 's', ha='right')
text(ax, X(2.2, 0.35)[0], X(2.2, 0.35)[1] - 5, r'$3^2+1^2=10$', 'varie', 's')
text(ax, 44, 76, 'mêmes marques : mêmes longueurs', 'resultat', 's')
save(fig, '33-070')
