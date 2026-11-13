import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, '256 fonctions, un point chacune', 'encre', 'm')
def group(x, y, w, n, role, label=None):
    box(ax, x, y, w, 18, role, fill=False, dash=True, lw=0.7)
    xs = [x + w * (k + 0.5) / n for k in range(n)]
    for k, px in enumerate(xs):
        disc(ax, px, y + 9, 2.2, 'resultat' if k == 0 else role)
    return xs
xs = group(3, 38, 44, 3, 'sujet')
for a, b in [(0, 1), (1, 2)]:
    arrow(ax, (xs[a] + 2.8, 47), (xs[b] - 2.8, 47), 'varie', both=True, lw=1.1)
text(ax, 25, 62, 'on permute les fils', 'varie', 's')
group(55, 38, 30, 2, 'fixe')
text(ax, 70, 62, 'autre groupe', 'fixe', 's')
line(ax, [(47.6, 47), (54.4, 47)], 'limite', lw=1.0)
ax.plot([51], [47], marker='x', color=COL['limite'], ms=4, zorder=4)
group(3, 12, 20, 1, 'fixe'); group(32, 12, 53, 4, 'fixe')
text(ax, 44, 4, 'vert : un modèle par groupe', 'resultat', 's')
text(ax, 44, 34, 'équivalentes seulement dans un même groupe', 'sujet', 's')
save(fig, '49-262')
