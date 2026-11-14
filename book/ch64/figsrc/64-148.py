import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
Rr, r, cy = 11, 2.2, 38

def edge(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    return (p[0] + dx / n * d, p[1] + dy / n * d)

def cluster(cx, visited, arcs):
    ax.add_patch(Circle((cx, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
    pts = [(cx + Rr * math.cos(math.radians(90 * k)), cy + Rr * math.sin(math.radians(90 * k))) for k in range(4)]
    for (i, j, c) in arcs:
        arrow(ax, edge(pts[i], pts[j], r), edge(pts[j], pts[i], r), 'varie', curve=c)
    for k, p in enumerate(pts):
        disc(ax, p[0], p[1], r, 'sujet' if k in visited else 'fixe')
        a = math.radians(90 * k)
        text(ax, cx + (Rr + 6.5) * math.cos(a), cy + (Rr + 5.5) * math.sin(a), f'{90 * k}°', 'sujet' if k in visited else 'fixe', 's')

# gauche : le point à 90° donne 90, 180, 270, 0
cluster(24, {0, 1, 2, 3}, [(0, 1, 0.414), (1, 2, 0.414), (2, 3, 0.414), (3, 0, 0.414)])
# droite : le point à 180° donne 180, 0
cluster(66, {0, 2}, [(0, 2, 0.5), (2, 0, 0.5)])
text(ax, 24, 14, '90° : les 4 points', 'resultat', 'm')
text(ax, 24, 8, 'racine primitive', 'resultat', 'm')
text(ax, 66, 14, '180° : 2 points seulement', 'limite', 'm')
text(ax, 66, 8, 'pas primitive', 'limite', 'm')
save(fig, '64-148')
