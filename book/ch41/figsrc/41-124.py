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

fig, ax = canvas(76)
v, w = (2, 0, 0), (1, 2, 0)
OA, OB = (22, 30), (66, 30)
para(ax, v, w, (1, 1, 3), OA, 5, 'sujet')
para(ax, v, w, (1, 1, -3), OB, 5, 'autre')
for O in (OA, OB):
    pts = [iso(0, 0, 0, O, 5), iso(2, 0, 0, O, 5), iso(3, 2, 0, O, 5), iso(1, 2, 0, O, 5), iso(0, 0, 0, O, 5)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COL['fixe'], lw=0.9, ls='--', zorder=3)
text(ax, 22, 71, r'$u$ au-dessus de la base', 'sujet', 's')
text(ax, 66, 71, r'$u$ en dessous de la base', 'autre', 's')
text(ax, 24, 14, r'$u\cdot(v\times w)=12$', 'sujet', 'm')
text(ax, 68, 14, r'$u\cdot(v\times w)=-12$', 'autre', 'm')
text(ax, 25, 36.5, 'base', 'fixe', 's')
text(ax, 68.5, 36.5, 'base', 'fixe', 's')
box(ax, 4, 1, 80, 8, 'resultat', label=r'volume : 12 dans les deux', size='m')
save(fig, '41-124')
