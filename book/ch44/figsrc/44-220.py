import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
P = {'1': (1, 2, 3), 's': (2, 3, 1), 'q': (3, 1, 2), 'a': (1, 3, 2), 'b': (3, 2, 1), 'c': (2, 1, 3)}
NM = {'1': '1', 's': r'$\sigma$', 'q': r'$\sigma^2$', 'a': r'$\tau_1$', 'b': r'$\tau_2$', 'c': r'$\tau_3$'}
ORDER = ['1', 's', 'q', 'a', 'b', 'c']
INV = {v: k for k, v in P.items()}
def comp(x, y): return INV[tuple(P[x][P[y][i] - 1] for i in range(3))]
import math
fig, ax = canvas(88)
def reg(cx, cy, R, n, rot=90):
    return [(cx + R * math.cos(math.radians(rot + 360 * i / n)), cy + R * math.sin(math.radians(rot + 360 * i / n))) for i in range(n)]
def ticks(p, q, n, role='encre'):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    L = math.dist(p, q); ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L; nx, ny = -uy, ux
    for t in range(n):
        o = (t - (n - 1) / 2) * 1.2
        line(ax, [(mx + ux * o - nx * 1.2, my + uy * o - ny * 1.2), (mx + ux * o + nx * 1.2, my + uy * o + ny * 1.2)], role, lw=0.8)
def arc(v, a, b, r, role='encre'):
    a1 = math.atan2(a[1] - v[1], a[0] - v[0]); a2 = math.atan2(b[1] - v[1], b[0] - v[0])
    d = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
    line(ax, [(v[0] + r * math.cos(a1 + d * t / 12), v[1] + r * math.sin(a1 + d * t / 12)) for t in range(13)], role, lw=0.8)
def shape(pts, role, sides, angs):
    poly(ax, pts, role); n = len(pts)
    for i in range(n):
        ticks(pts[i], pts[(i + 1) % n], sides[i])
        for t in range(angs[i]): arc(pts[i], pts[i - 1], pts[(i + 1) % n], 2.4 + 1.1 * t)
text(ax, 44, 84, 'côtés égaux et angles égaux', 'sujet', 's', weight='bold')
for cx, n in [(16, 3), (44, 4), (72, 5)]:
    R = 10.5 if n != 4 else 11
    shape(reg(cx, 66, R, n, 90 if n != 4 else 45), 'sujet', [1] * n, [1] * n)
    text(ax, cx, 49, f'$n={n}$', 'sujet', 'm')
rect = [(10, 36), (34, 36), (34, 22), (10, 22)]
shape(rect, 'limite', [1, 2, 1, 2], [1, 1, 1, 1])
text(ax, 22, 12, 'angles égaux, côtés non', 'limite', 's')
lo = [(66, 40), (77, 29), (66, 18), (55, 29)]
shape(lo, 'limite', [1, 1, 1, 1], [1, 2, 1, 2])
text(ax, 66, 12, 'côtés égaux, angles non', 'limite', 's')
save(fig, '44-220')
