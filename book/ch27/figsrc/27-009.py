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

fig, ax = canvas(54)
o, u = (24, 13), 13
for q in ((1.5, 0, 0), (0, 1.5, 0), (0, 0, 1.5)):
    line(ax, [iso(0, 0, 0, o, u), iso(*q, o, u)], 'sujet', lw=1.6)
for lab, q in (('1', (1.5, 0, 0)), ('2', (0, 1.5, 0)), ('3', (0, 0, 1.5))):
    x, y = iso(*q, o, u); text(ax, x + (2.5 if lab == '1' else -2.5 if lab == '2' else 0), y + (2.5 if lab == '3' else 0), lab, 'sujet', 'm')
text(ax, 24, 47, 'pièce : 90° deux à deux', 'sujet', 'm')
O = (58, 14)
line(ax, [O, (84, 14)], 'sujet', lw=1.6); line(ax, [O, (58, 38)], 'sujet', lw=1.6)
line(ax, [O, (72, 28)], 'varie', lw=1.6)
rmark(ax, O, (64, 14), (58, 20), 2.4, 'sujet')
text(ax, 85.5, 14, '1', 'sujet', 'm'); text(ax, 58, 41, '2', 'sujet', 'm'); text(ax, 75, 30, '3', 'varie', 'm')
text(ax, 70, 20.5, '≠ 90°', 'limite', 's')
text(ax, 66, 47, "feuille : l'arête 3 penche", 'varie', 'm')
save(fig, '27-009')
