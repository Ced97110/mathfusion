import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.colors as mc

def para(ax, a, b, c, origin, s, role):
    view = (-1, -1, 1)
    P = lambda p: iso(p[0], p[1], p[2], origin, s)
    cr = lambda p, q: (p[1]*q[2]-p[2]*q[1], p[2]*q[0]-p[0]*q[2], p[0]*q[1]-p[1]*q[0])
    dot = lambda p, q: sum(i*j for i, j in zip(p, q))
    add = lambda *v: tuple(sum(t) for t in zip(*v))
    base = mc.to_rgb(FILL[role])
    for (p, q, r), sh in zip([(a, b, c), (a, c, b), (b, c, a)], [1.0, 0.86, 0.72]):
        n = cr(p, q); sg = 1 if dot(n, r) > 0 else -1
        for off, out in ((0, -sg), (1, sg)):
            if dot(n, view) * out > 0:
                o = tuple(off * t for t in r)
                pts = [P(o), P(add(o, p)), P(add(o, p, q)), P(add(o, q))]
                ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=tuple(v*sh for v in base), lw=0.8, zorder=2, joinstyle='round'))

fig, ax = canvas(64)
# A : parallélogramme plat
poly(ax, [(3, 28), (15, 28), (22, 40), (10, 40)], 'fixe')
# B : carton à angles droits
para(ax, (2, 0, 0), (0, 2, 0), (0, 0, 3), (43, 20), 5, 'autre')
# C : parallélépipède de u, v, w
u, v, w = (2, 0, 0), (1, 2, 0), (1, 1, 3)
O = (72, 16)
para(ax, u, v, w, O, 5, 'sujet')
text(ax, 13, 58, 'parallélogramme', 'fixe', 's')
text(ax, 43, 58, 'carton', 'autre', 's')
text(ax, 74, 58, 'parallélépipède', 'sujet', 's')
text(ax, 13, 10, 'plat : 2 dimensions', 'fixe', 's')
text(ax, 43, 10, 'angles droits', 'autre', 's')
text(ax, 74, 10, 'arêtes inclinées', 'sujet', 's')
text(ax, 74, 4.5, 'base 4 · hauteur 3', 'sujet', 's')
Ptop, Pfoot = iso(2, 1.5, 3, O, 5), iso(2, 1.5, 0, O, 5)
disc(ax, Ptop[0], Ptop[1], 0.7, 'varie')
disc(ax, Pfoot[0], Pfoot[1], 0.7, 'varie')
line(ax, [Ptop, Pfoot], 'varie', lw=1.1, dash=True)
text(ax, Ptop[0] + 2, (Ptop[1] + Pfoot[1]) / 2, '3', 'varie', 's', weight='bold')
text(ax, 77, 13.5, r'$u$', 'encre', 's')
text(ax, 65.5, 19, r'$v$', 'encre', 's')
text(ax, 68.5, 27, r'$w$', 'encre', 's')
save(fig, '41-123')
