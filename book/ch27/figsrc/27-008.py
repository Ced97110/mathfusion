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
fig, ax = canvas(52)
poly(ax, [(6, 14), (26, 14), (26, 34), (6, 34)], 'sujet')
rmark(ax, (6, 14), (12, 14), (6, 20), 2.6, 'resultat')
text(ax, 15, 22, '90°', 'resultat', 'm')
text(ax, 16, 42, 'dans la pièce', 'sujet', 'm')
t = math.radians(35); O = (47, 15); w, s2 = 22, 18
pts = [O, (O[0] + w, O[1]), (O[0] + w + s2 * math.cos(t), O[1] + s2 * math.sin(t)), (O[0] + s2 * math.cos(t), O[1] + s2 * math.sin(t))]
poly(ax, pts, 'autre')
arc = lambda c, a0, a1, r: [(c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a))) for a in range(a0, a1 + 1, 5)]
line(ax, arc(O, 0, 35, 6), 'limite', lw=0.9)
line(ax, arc(pts[1], 35, 180, 4.5), 'limite', lw=0.9)
text(ax, 59.5, 18.8, '35°', 'limite', 's')
text(ax, 65.8, 22.2, '145°', 'limite', 's')
text(ax, 66, 42, 'sur le dessin', 'autre', 'm')
arrow(ax, (29, 25), (42, 25), 'varie', lw=1.2)
text(ax, 35.5, 29.5, 'dessiner', 'varie', 's')
text(ax, 55, 6, "ni l'un ni l'autre n'est 90°", 'limite', 's')
save(fig, '27-008')
