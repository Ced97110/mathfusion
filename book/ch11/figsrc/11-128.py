import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def prism(ax, ox, oy, a, b, c, u, role='sujet', z0=0.0, lw=0.5):
    import matplotlib.colors as mc
    base = mc.to_rgb(FILL[role]); P = lambda x, y, z: iso(x, y, z+z0, (ox, oy), u)
    faces = [([P(0,0,c), P(a,0,c), P(a,b,c), P(0,b,c)], 1.0), ([P(0,0,0), P(a,0,0), P(a,0,c), P(0,0,c)], 0.86), ([P(0,0,0), P(0,b,0), P(0,b,c), P(0,0,c)], 0.72)]
    for pts, s in faces:
        ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=tuple(min(1, v*s) for v in base), lw=lw, zorder=2, joinstyle='round'))
fig, ax = canvas(46)
ox, oy, u, C = 12, 12, 6, 0.866
prism(ax, ox, oy, 3, 1.5, 0.5, u, 'varie')
prism(ax, ox, oy, 3, 1.5, 1.5, u, 'sujet', z0=0.5)
text(ax, ox+1.5*C*u+3.5, oy+0.75*u-3.5, '60', 'encre', 's')
text(ax, ox-0.75*C*u-3.5, oy+0.75*u-3, '30', 'encre', 's')
text(ax, ox+3*C*u+4, oy+1.5*u+u, '40', 'encre', 's')
text(ax, 38, 38, 'aire de la base', 'varie', 's', ha='left')
text(ax, 38, 32, '60 × 30 = 1 800', 'varie', ha='left')
text(ax, 38, 24, '× hauteur 40', 'encre', 's', ha='left')
text(ax, 38, 18, '1 800 × 40 = 72 000', 'encre', ha='left')
text(ax, 38, 10, 'V = 72 000 cm³', 'resultat', ha='left', weight='bold')
save(fig, '11-128')
