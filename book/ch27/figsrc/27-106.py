import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(64)
b = 10; A = (6, b); C = (56, b); V = (31, b + 42.4); O = (31, b)
fig, ax = canvas(58)
o = (40, 6); u = 11; I = lambda x, y, z: iso(x, y, z, o, u)
th, ph = math.radians(20), math.radians(50)
AE = 2.92; ex, ez = AE * math.cos(th), AE * math.sin(th); fy = AE * math.tan(ph)
A = (0, 0, 0); D = (ex, 0, 0); E = (ex, 0, ez); B = (ex, fy, 0); Fp = (0, fy, 0); C = (ex, fy, ez)
poly(ax, [I(*A), I(*D), I(*B), I(*Fp)], 'fixe')
poly(ax, [I(*A), I(*E), I(*C), I(*Fp)], 'varie')
ax.add_patch(Polygon([I(*A), I(*D), I(*E)], closed=True, ec='none', fc=COL['sujet'], alpha=0.30, zorder=2.6))
ax.add_patch(Polygon([I(*A), I(*B), I(*C)], closed=True, ec='none', fc=COL['resultat'], alpha=0.25, zorder=2.6))
for a, b, r in ((A, D, 'sujet'), (D, E, 'sujet'), (A, E, 'sujet'), (Fp, B, 'sujet'), (B, C, 'sujet'), (Fp, C, 'sujet'), (E, C, 'varie'), (A, C, 'resultat'), (B, C, 'resultat'), (A, B, 'resultat')):
    line(ax, [I(*a), I(*b)], r, lw=1.1)
line(ax, [I(*A), I(*Fp)], 'encre', lw=2.0)
def vec(a, b): return tuple(q - p for p, q in zip(a, b))
def nrm(v): l = math.sqrt(sum(c * c for c in v)); return tuple(c / l for c in v)
def arc3(a, b, c, r, role, lab):
    u1, v1 = nrm(vec(a, b)), nrm(vec(a, c)); om = math.acos(sum(p * q for p, q in zip(u1, v1)))
    pts = []
    for i in range(13):
        t = i / 12; w = [(math.sin((1 - t) * om) * p + math.sin(t * om) * q) / math.sin(om) for p, q in zip(u1, v1)]
        pts.append(I(*[a[j] + r * w[j] for j in range(3)]))
    line(ax, pts, role, lw=1.0)
    t = .5; w = [(math.sin((1 - t) * om) * p + math.sin(t * om) * q) / math.sin(om) for p, q in zip(u1, v1)]
    m = I(*[a[j] + (r + 0.45) * w[j] for j in range(3)])
    return m
mt = arc3(A, D, E, 0.9, 'sujet', ''); mp = arc3(A, E, C, 1.2, 'varie', ''); ma = arc3(A, C, B, 0.9, 'resultat', '')
text(ax, mt[0] + 0.5, mt[1] - 2.2, r'$\theta$', 'sujet', 's'); text(ax, mp[0] - 4, mp[1] + 1, r'$\varphi$', 'varie', 's'); text(ax, ma[0] + 4, ma[1] - 4.5, r'$\alpha$', 'resultat', 's')
for n, p, d in (('A', A, (-3, -2.5)), ('E', E, (3, 2)), ('C', C, (0, 3.5))):
    q = I(*p); text(ax, q[0] + d[0], q[1] + d[1], r'$' + n + r'$', 'encre', 'm')
text(ax, 16, 14, 'charnière', 'encre', 's')
text(ax, 24, 31, 'colline', 'varie', 's')
text(ax, 78, 12, 'plan de $\\theta$', 'sujet', 's'); arrow(ax, (72, 14.5), (60, 15), 'sujet', lw=0.7)
text(ax, 15, 47, 'plan de $\\alpha$', 'resultat', 's'); arrow(ax, (23, 44.5), (33.6, 33), 'resultat', lw=0.7)
save(fig, '27-106')
