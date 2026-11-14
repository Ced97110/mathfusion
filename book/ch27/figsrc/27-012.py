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

import math
fig, ax = canvas(76)
a, b, c = 5, 2, 3
p = P((20, 10), 9)
solid(ax, p, a, b, c, 'sujet'); hidden(ax, p, a, b, c)
A_, C_, G_ = p(0,0,0), p(a,b,0), p(a,b,c)
ax.add_patch(Polygon([A_, C_, G_], closed=True, ec='none', fc=COL['varie'], alpha=0.35, zorder=2.6))
line(ax, [A_, C_], 'varie', lw=1.2, dash=True)
line(ax, [C_, G_], 'varie', lw=1.2, dash=True)
line(ax, [A_, G_], 'varie', lw=1.8)
for k, q, d in (('A', A_, (-3, -2)), ('C', C_, (2.8, -1.6)), ('G', G_, (0, 3))):
    text(ax, q[0]+d[0], q[1]+d[1], '$'+k+'$', 'encre', 'm')
rmark(ax, C_, A_, G_, 2.0, 'varie')
ang = lambda q: math.degrees(math.atan2(q[1] - A_[1], q[0] - A_[0]))
a0, a1 = ang(C_), ang(G_)
line(ax, [(A_[0] + 9 * math.cos(math.radians(t)), A_[1] + 9 * math.sin(math.radians(t))) for t in (a0 + (a1-a0)*i/8 for i in range(9))], 'varie', lw=0.9)
am = math.radians((a0 + a1) / 2)
text(ax, A_[0] + 12.5 * math.cos(am), A_[1] + 12.5 * math.sin(am), r'$\alpha$', 'varie', 'm')
text(ax, 76, 22, 'boîte', 'sujet', 's')
arrow(ax, (71, 22), (60, 22), 'sujet', lw=0.7)
text(ax, 71, 62, 'triangle $ACG$', 'varie', 's')
mid = ((A_[0]+G_[0]+C_[0])/3, (A_[1]+G_[1]+C_[1])/3)
arrow(ax, (66, 59), (mid[0]+3, mid[1]+3), 'varie', lw=0.8)
text(ax, 72, 42, 'angle droit en $C$', 'varie', 's')
arrow(ax, (63, 42), (C_[0]+3.2, C_[1]+0.3), 'varie', lw=0.6)
save(fig, '27-012')
