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
s, h = 4.6, 2.92
p = P((44, 8), 7.5)
A, B, C, D = (0,0,0), (s,0,0), (s,s,0), (0,s,0); T = (s/2, s/2, h)
face(ax, [p(*A), p(*B), p(*T)], 'fixe', 0.86)
face(ax, [p(*A), p(*D), p(*T)], 'fixe', 0.72)
for q in (B, D): line(ax, [p(*C), p(*q)], 'fixe', lw=0.8, dash=True)
line(ax, [p(*C), p(*T)], 'varie', lw=1.4, dash=True)
line(ax, [p(s/2, s/2, 0), p(*T)], 'encre', lw=0.8, dash=True)
for q in (A, B, D): line(ax, [p(*q), p(*T)], 'varie', lw=1.6)
mid = lambda q: ((p(*q)[0] + p(*T)[0]) / 2, (p(*q)[1] + p(*T)[1]) / 2)
text(ax, 66, 54, 'arête montante', 'varie', 's')
arrow(ax, (66, 51.5), (mid(B)[0] + 0.6, mid(B)[1] + 0.6), 'varie', lw=0.7)
text(ax, 18, 56, 'hauteur 146 m', 'encre', 's')
arrow(ax, (18, 53.5), (43, 36), 'encre', lw=0.7)
ab = ((p(*A)[0] + p(*B)[0]) / 2, (p(*A)[1] + p(*B)[1]) / 2)
text(ax, 70, 5.5, 'côté de la base', 'fixe', 's')
arrow(ax, (70, 8), (ab[0] + 1, ab[1] - 0.6), 'fixe', lw=0.7)
save(fig, '27-004')
