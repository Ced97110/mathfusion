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
s = 4.5
O = (14, 22)
para(ax, (2, 0, 0), (1, 2, 0), (1, 1, 3), O, s, 'sujet')
pts = [iso(0, 0, 0, O, s), iso(2, 0, 0, O, s), iso(3, 2, 0, O, s), iso(1, 2, 0, O, s), iso(0, 0, 0, O, s)]
ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COL['varie'], lw=1.2, ls='--', zorder=3)
p0, p1 = iso(1, 1, 0, O, s), iso(1, 1, 3, O, s)
line(ax, [p0, p1], 'resultat', lw=1.2, dash=True)
text(ax, 15, 11, 'base : aire 4', 'varie', 's')
text(ax, 29, 33, r'$h=3$', 'resultat', 's')
box(ax, 44, 46, 42, 12, 'sujet', label=r'volume = base $\times$ hauteur', size='s')
box(ax, 44, 27, 42, 12, 'varie', label=r'hauteur $=\|u\|\cos\varphi$', size='s', weight='bold')
box(ax, 44, 8, 42, 12, 'resultat', label=r'$=u\cdot(v\times w)=12$', size='s')
arrow(ax, (65, 45.5), (65, 39.5), 'fixe')
arrow(ax, (65, 26.5), (65, 20.5), 'fixe')
text(ax, 78, 42.5, 'départ', 'fixe', 's')
text(ax, 80, 23.5, 'étape clé', 'varie', 's')
save(fig, '41-126')
