import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
OX, OY, U = 33.0, 8.0, 7.0
A = (0, 4, 0); B = (0, 0, 0); C = (3, 0, 0); D = (3, 4, 0); G = (3, 0, 2)
E = (0, 4, 2); F = (0, 0, 2); Hh = (3, 4, 2)
def Q(p): return iso(p[0], p[1], p[2], (OX, OY), U)
def seg(a, b, role='fixe', lw=0.9, dash=False): line(ax, [Q(a), Q(b)], role, lw, dash)
def face(pts, role='fixe', fill=True, lw=0.8): poly(ax, [Q(p) for p in pts], role, fill, lw)
def add(o, *vs): return tuple(o[i] + sum(v[i] for v in vs) for i in range(3))
def sc(v, s): return tuple(s * c for c in v)
def unit(v):
    n = math.sqrt(sum(c * c for c in v)); return tuple(c / n for c in v)
def rmark(o, e1, e2, s=0.4, role='encre'):
    e1, e2 = unit(e1), unit(e2)
    line(ax, [Q(add(o, sc(e1, s))), Q(add(o, sc(e1, s), sc(e2, s))), Q(add(o, sc(e2, s)))], role, 0.8)
def arcv(o, v1, v2, r, role='varie', lw=1.0):
    v1, v2 = unit(v1), unit(v2)
    th = math.acos(sum(a * b for a, b in zip(v1, v2))); pts = []
    for k in range(17):
        t = k / 16
        w = tuple((math.sin((1 - t) * th) * a + math.sin(t * th) * b) / math.sin(th) for a, b in zip(v1, v2))
        pts.append(Q(add(o, sc(w, r))))
    line(ax, pts, role, lw)
def lab(p, s, dx=0, dy=0, role='encre', size='m', ha='center'):
    x, y = Q(p); text(ax, x + dx, y + dy, s, role, size, ha=ha)
def vec(a, b): return tuple(b[i] - a[i] for i in range(3))
fig, ax = canvas(52)
face([A, B, C, D], 'fixe')
Hp = (2, 2, 0); Gp = (2, 2, 3)
seg(Gp, Hp, 'varie', 1.4)
rmark(Hp, (1, 0, 0), (0, 0, 1), 0.5); rmark(Hp, (0, -1, 0), (0, 0, 1), 0.5)
gx, gy = Q(Gp); hx, hy = Q(Hp)
disc(ax, gx, gy, 1.1, 'sujet'); disc(ax, hx, hy, 1.1, 'resultat')
text(ax, gx + 4, gy, 'G', 'sujet'); text(ax, hx + 5, hy - 4, 'H', 'resultat')
text(ax, 10, 12, 'plan', 'fixe', 's')
text(ax, 62, 42, 'point G', 'sujet', 's', ha='left')
text(ax, 62, 30, r'perpendiculaire', 'varie', 's', ha='left')
text(ax, 62, 25, 'au plan par G', 'varie', 's', ha='left')
text(ax, 62, 13, 'projeté de G : H', 'resultat', 's', ha='left')
save(fig, '27-036')
