import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
pairs = [(x, y) for x in range(1, 6) for y in range(x, 6)]
oy = 18
def plot(ox, pts, role, sx, sy, link, ylab):
    arrow(ax, (ox - 1, oy), (ox + 34, oy), 'fixe', lw=0.7)
    arrow(ax, (ox, oy - 1), (ox, oy + 44), 'fixe', lw=0.7)
    for v in (5, 10):  # graduations de l'axe horizontal
        ax.plot([ox + v * sx] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.8, zorder=1.5)
        text(ax, ox + v * sx, oy - 3.2, str(v), 'fixe', 's')
    for v in (10, 20):  # graduations de l'axe vertical
        ax.plot([ox - 1, ox + 1], [oy + v * sy] * 2, color=COL['fixe'], lw=0.8, zorder=1.5)
        text(ax, ox - 2.2, oy + v * sy, str(v), 'fixe', 's', ha='right')
    if link: line(ax, [(ox + 1 * sx, oy + 2 * sy), (ox + 10 * sx, oy + 20 * sy)], role, lw=0.8, dash=True)
    for (s, v) in pts:
        disc(ax, ox + s * sx, oy + v * sy, 1.1, role)
    text(ax, ox + 33, oy - 7, 'somme', role, 's', ha='right')
    text(ax, ox + 2, oy + 47, ylab, role, 's', ha='left')
sums = sorted({x + y for x, y in pairs})
plot(10, [(s, 2 * s) for s in sums], 'autre', 3.0, 1.9, True, 'double')
plot(54, [(x + y, x * y) for x, y in pairs], 'sujet', 2.8, 1.6, False, 'produit')
text(ax, 26, 4, 'une droite : lien', 'autre', 's'); text(ax, 70, 4, 'aucune droite : aucun lien', 'sujet', 's')
save(fig, '55-086')
