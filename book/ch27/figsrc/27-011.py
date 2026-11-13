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

fig, ax = canvas(80)
A_, C_, G_ = (8, 54), (38, 54), (38, 66)
poly(ax, [A_, C_, G_], 'fixe')
rmark(ax, C_, A_, G_, 2.4, 'fixe')
text(ax, 23, 50.5, '5', 'fixe', 'm'); text(ax, 41.5, 60, '2', 'fixe', 'm'); text(ax, 14, 56.2, r'$\alpha$', 'fixe', 's')
box(ax, 50, 51, 34, 14, 'fixe', label=r'$\tan\alpha = 2 \div 5 = 0{,}4$', size='m')
text(ax, 67, 70, 'calcul déjà connu', 'fixe', 's')
a, b, c = 4, 3, 2
p = P((26, 8), 5.2)
solid(ax, p, a, b, c, 'fixe'); hidden(ax, p, a, b, c)
tri(ax, [p(0,0,0), p(a,b,0), p(a,b,c)], 'varie')
line(ax, [p(0,0,0), p(a,b,c)], 'varie', lw=1.6)
line(ax, [p(0,0,0), p(a,b,0)], 'varie', lw=1.0, dash=True)
line(ax, [p(a,b,0), p(a,b,c)], 'varie', lw=1.0, dash=True)
box(ax, 52, 14, 32, 14, 'varie', label='nouveau :\ntrouver ce triangle', size='s')
arrow(ax, (52, 21), (45, 21), 'varie', lw=1.2)
save(fig, '27-011')
