import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.colors as mc
def face(ax, pts, role, sh=1.0, alpha=1.0, z=2):
    fc = tuple(min(1, v * sh) for v in mc.to_rgb(FILL[role]))
    ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=fc, lw=0.6, zorder=z, joinstyle='round', alpha=alpha))
def P(o, u): return lambda x, y, z: iso(x, y, z, o, u)
def solid(ax, p, a, b, c, role='sujet'):
    face(ax, [p(0,0,c), p(a,0,c), p(a,b,c), p(0,b,c)], role, 1.0)
    face(ax, [p(0,0,0), p(a,0,0), p(a,0,c), p(0,0,c)], role, 0.86)
    face(ax, [p(0,0,0), p(0,b,0), p(0,b,c), p(0,0,c)], role, 0.72)
def hidden(ax, p, a, b, c, role='fixe', lw=0.7):
    for q in [(a,0,0),(0,b,0),(a,b,c)]: line(ax, [p(a,b,0), p(*q)], role, lw=lw, dash=True)
OFF = dict(A=(0,-3), B=(2.8,-0.6), C=(0,-3), D=(-2.8,-0.6), E=(-2.4,-1.4), F=(2.8,0.6), G=(0,3), H=(-2.8,0.6))
def letters(ax, p, a, b, c, keys, role='encre'):
    V = dict(A=(0,0,0), B=(a,0,0), C=(a,b,0), D=(0,b,0), E=(0,0,c), F=(a,0,c), G=(a,b,c), H=(0,b,c))
    for k in keys:
        x, y = p(*V[k]); dx, dy = OFF[k]; text(ax, x+dx, y+dy, '$'+k+'$', role, 'm')
def rmark(ax, c, p1, p2, s=2.2, role='encre'):
    import math
    def un(q):
        d = math.hypot(q[0]-c[0], q[1]-c[1]); return ((q[0]-c[0])/d*s, (q[1]-c[1])/d*s)
    v1, v2 = un(p1), un(p2)
    line(ax, [(c[0]+v1[0], c[1]+v1[1]), (c[0]+v1[0]+v2[0], c[1]+v1[1]+v2[1]), (c[0]+v2[0], c[1]+v2[1])], role, lw=0.7)
def tri(ax, pts, role):
    ax.add_patch(Polygon(pts, closed=True, ec='none', fc=FILL[role], alpha=0.9, zorder=2.6))

fig, ax = canvas(62)
o, u = (28, 17), 11.5
cubes(ax, [(0, 0, 0)], o, u, 'sujet', lw=0.8)
for q in ((1.45, 0, 0), (0, 1.45, 0), (0, 0, 1.45)):
    arrow(ax, iso(0, 0, 0, o, u), iso(*q, o, u), 'varie', lw=1.2)
tx, ty = iso(1.45, 0, 0, o, u); text(ax, tx + 2, ty, 'droite', 'varie', 's', ha='left')
tx, ty = iso(0, 1.45, 0, o, u); text(ax, tx - 2, ty, 'arrière', 'varie', 's', ha='right')
tx, ty = iso(0, 0, 1.45, o, u); text(ax, tx, ty + 3, 'haut', 'varie', 's')
box(ax, 58, 14, 26, 26, 'fixe')
arrow(ax, (62, 18), (81, 18), 'varie', lw=1.2); text(ax, 72, 22.5, 'droite', 'varie', 's')
arrow(ax, (62, 18), (62, 37), 'varie', lw=1.2); text(ax, 65, 36, 'haut', 'varie', 's', ha='left')
text(ax, 24, 54, 'objet : 3 directions', 'sujet', 'm')
text(ax, 71, 46, 'page : 2 directions', 'fixe', 'm')
text(ax, 44, 6, '3 directions dans 2', 'varie', 'm')
save(fig, '27-007')
