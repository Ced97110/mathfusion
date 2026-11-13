import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(56)
o = (30, 8); u = 6.5; I = lambda x, y, z: iso(x, y, z, o, u)
pts = [(0,0,0),(4,0,0),(4,3,0),(0,3,0),(0,0,2),(4,0,2),(4,3,2),(0,3,2)]
Q = [I(*p) for p in pts]
for a, b in ((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)): line(ax, [Q[a], Q[b]], 'fixe', lw=0.6, dash=True)
poly(ax, [I(0,0,0), I(4,0,0), I(4,0,2)], 'sujet')
poly(ax, [I(0,0,0), I(0,3,0), I(4,3,2), I(4,0,2)], 'varie')
line(ax, [I(0,0,0), I(4,0,0), I(4,0,2), I(0,0,0)], 'sujet', lw=1.0)
line(ax, [I(0,0,0), I(0,3,0)], 'encre', lw=2.0)
text(ax, 70, 48, 'boîte 4 × 3 × 2', 'fixe', 's'); line(ax, [(58, 46), (46, 38)], 'fixe', lw=0.6)
text(ax, 70, 32, 'face inclinée', 'varie', 's'); line(ax, [(59, 31), (40, 28)], 'varie', lw=0.6)
text(ax, 70, 17, 'charnière', 'encre', 's'); line(ax, [(62, 16), (20, 17)], 'encre', lw=0.6)
text(ax, 22, 6, 'coin', 'sujet', 'm')
save(fig, '27-104')
