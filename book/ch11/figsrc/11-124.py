import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def prism(ax, ox, oy, a, b, c, u, role='sujet', z0=0.0, lw=0.5):
    import matplotlib.colors as mc
    base = mc.to_rgb(FILL[role]); P = lambda x, y, z: iso(x, y, z+z0, (ox, oy), u)
    faces = [([P(0,0,c), P(a,0,c), P(a,b,c), P(0,b,c)], 1.0), ([P(0,0,0), P(a,0,0), P(a,0,c), P(0,0,c)], 0.86), ([P(0,0,0), P(0,b,0), P(0,b,c), P(0,0,c)], 0.72)]
    for pts, s in faces:
        ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=tuple(min(1, v*s) for v in base), lw=lw, zorder=2, joinstyle='round'))
fig, ax = canvas(60)
u = 9
# bassin 1 : 2 x 1 x 0,5
prism(ax, 14, 18, 2, 1, 0.5, u, 'sujet')
# bassin 2 : 4 cubes
cubes(ax, [(i, 0, k) for i in range(2) for k in range(2)], (56, 18), u, 'sujet')
text(ax, 44, 56, 'même fond : 2 m²', 'fixe', 'm')
text(ax, 20, 11, 'profondeur 0,5 m', 'varie', 's'); text(ax, 62, 11, 'profondeur 2 m', 'varie', 's')
text(ax, 20, 4, 'V = 1 m³', 'resultat', weight='bold'); text(ax, 62, 4, 'V = 4 m³', 'resultat', weight='bold')
save(fig, '11-124')
