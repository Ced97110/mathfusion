import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def prism(ax, ox, oy, a, b, c, u, role='sujet', z0=0.0, lw=0.5):
    import matplotlib.colors as mc
    base = mc.to_rgb(FILL[role]); P = lambda x, y, z: iso(x, y, z+z0, (ox, oy), u)
    faces = [([P(0,0,c), P(a,0,c), P(a,b,c), P(0,b,c)], 1.0), ([P(0,0,0), P(a,0,0), P(a,0,c), P(0,0,c)], 0.86), ([P(0,0,0), P(0,b,0), P(0,b,c), P(0,0,c)], 0.72)]
    for pts, s in faces:
        ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=tuple(min(1, v*s) for v in base), lw=lw, zorder=2, joinstyle='round'))
def cyl(ax, cx, yb, r, h, role):
    k = 0.577; n = 40
    ang = [2*math.pi*i/n for i in range(n+1)]
    cy0 = yb + k*r
    ax.add_patch(Rectangle((cx-r, cy0), 2*r, h, ec='none', fc=FILL[role], zorder=2))
    low = [(cx+r*math.cos(a), cy0+k*r*math.sin(a)) for a in ang if math.sin(a) <= 0 or True]
    ax.add_patch(Polygon([(cx+r*math.cos(a), cy0+k*r*math.sin(a)) for a in ang], closed=True, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((cx-r, cy0), 2*r, h, ec='none', fc=FILL[role], zorder=2.1))
    line(ax, [(cx-r, cy0), (cx-r, cy0+h)], role); line(ax, [(cx+r, cy0), (cx+r, cy0+h)], role)
    ax.add_patch(Polygon([(cx+r*math.cos(a), cy0+h+k*r*math.sin(a)) for a in ang], closed=True, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2.2))
C = 0.866
def prism_c(ax, cx, yb, a, b, c, u, role):
    ox = cx - (a-b)/2*C*u
    prism(ax, ox, yb, a, b, c, u, role)
fig, ax = canvas(54)
yb = 24; u = 4
prism_c(ax, 12, yb, 3, 2, 1.5, u, 'sujet')
prism_c(ax, 34, yb, 2, 1.5, 0.5, u, 'sujet')
prism_c(ax, 55, yb, 1, 1, 1, u, 'sujet')
cyl(ax, 77, yb, 4.5, 6, 'limite')
text(ax, 44, 49, 'pavé : 6 faces rectangulaires', 'sujet', 's')
for x, nm, vd, role in ((12, 'boîte', 'pavé', 'resultat'), (34, 'livre', 'pavé', 'resultat'), (55, 'dé', 'cube : pavé', 'resultat'), (77, 'conserve', 'cylindre', 'limite')):
    text(ax, x, 16, nm, 'encre', 's'); text(ax, x, 9, vd, role, 's', weight='bold')
save(fig, '11-127')
