import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 23, 33, 15
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
P = lambda a: (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
disc(ax, *P(0), 2.0, 'fixe')
text(ax, P(0)[0] + 4, P(0)[1], r'$1$', 'fixe', 'm')
names = {72: (r'$\zeta$', 0, 5), 144: (r'$\zeta^2$', -5, 3.5), 216: (r'$\zeta^3$', -5, -3.5), 288: (r'$\zeta^4$', 0, -5)}
for a, (s, dx, dy) in names.items():
    disc(ax, *P(a), 2.0, 'sujet')
    text(ax, P(a)[0] + dx, P(a)[1] + dy, s, 'sujet', 'm')
def sh(p, q, d=3.0):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
    return (p[0] + ux * d, p[1] + uy * d), (q[0] - ux * d, q[1] - uy * d)
for a, b, lab, sg, dist, t in [(72, 144, 'carré', -1, 4.0, .5), (144, 288, 'carré', -1, 3.6, .78), (72, 216, 'cube', 1, 3.6, .28)]:
    p, q = sh(P(a), P(b)); arrow(ax, p, q, 'varie', lw=0.9)
    mx, my = p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])
    L = math.hypot(q[0] - p[0], q[1] - p[1]); nx, ny = -(q[1] - p[1]) / L, (q[0] - p[0]) / L
    text(ax, mx + sg * nx * dist, my + sg * ny * dist, lab, 'varie', 's')
box(ax, 48, 50, 38, 11, 'sujet', label=r'$z$ racine de $h$')
box(ax, 48, 30, 38, 11, 'varie', label=r'$z^p$ racine de $h$')
box(ax, 48, 10, 38, 11, 'resultat', label='toutes les primitives')
arrow(ax, (60, 50), (60, 41.5), 'varie')
text(ax, 62, 45.5, r'élever à $p$', 'varie', 's', ha='left')
arrow(ax, (60, 30), (60, 21.5), 'varie')
text(ax, 62, 25.5, 'on répète', 'varie', 's', ha='left')
save(fig, '66-055')
