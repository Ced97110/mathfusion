import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcp(c, r, a0, a1, n=36): return [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
def ang(p, q): return math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
def arcl(c, r, a0, a1, role, lw=0.9): line(ax, arcp(c, r, a0, a1), role, lw)
def wedge(c, r, a0, a1, role): poly(ax, [c] + arcp(c, r, a0, a1), role, lw=0.4)
def circ(c, r, role, lw=0.9, dash=False): ax.add_patch(Circle(c, r, ec=COL[role], fc='none', lw=lw, ls='--' if dash else '-', zorder=2))
def dot(p, role='encre', r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
def vang(v, p, q, r, role, lw=0.9):
    a = ang(v, p); d = (ang(v, q) - a + 180) % 360 - 180
    arcl(v, r, a, a + d, role, lw); return a + d / 2
def rsq(p, u, w, s=2.0): line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + w[0]) * s, p[1] + (u[1] + w[1]) * s), (p[0] + w[0] * s, p[1] + w[1] * s)], 'fixe', 0.7)
def out(p, c, d):
    L = math.hypot(p[0] - c[0], p[1] - c[1]); return (p[0] + (p[0] - c[0]) / L * d, p[1] + (p[1] - c[1]) / L * d)
def mid(p, q): return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
RR = 120000 / (4 * math.sqrt(75 * 35 * 25 * 15))
def fld(s, o):
    f = lambda p: (o[0] + s * p[0], o[1] + s * p[1])
    return f((0, 0)), f((40, 0)), f((33.75, math.sqrt(3600 - 33.75 ** 2))), f((20, math.sqrt(RR ** 2 - 400))), RR * s
B, C, A, O, R = fld(0.9, (26, 12))
poly(ax, [A, B, C], 'fixe')
for X, nm, off in ((A, 'A', (3, 3)), (B, 'B', (-3, -2)), (C, 'C', (3, -2))):
    line(ax, [O, X], 'varie', 1.6)
    m = mid(O, X); d = math.atan2(X[1] - O[1], X[0] - O[0]) + math.pi / 2
    for o in (-0.8, 0.8):
        q = (m[0] + o * math.cos(d - math.pi / 2), m[1] + o * math.sin(d - math.pi / 2))
        line(ax, [(q[0] - 1.3 * math.cos(d), q[1] - 1.3 * math.sin(d)), (q[0] + 1.3 * math.cos(d), q[1] + 1.3 * math.sin(d))], 'encre', 0.9)
    text(ax, X[0] + off[0], X[1] + off[1], nm, 'encre', 'm', weight='bold')
text(ax, 55.5, 38, '30,24 m', 'varie', 's'); text(ax, 21, 25, '30,24 m', 'varie', 's'); text(ax, 70, 25, '30,24 m', 'varie', 's')
dot(O, 'sujet', 1.6); text(ax, O[0] + 4, O[1] - 3.5, 'O', 'sujet', 'l', weight='bold')
text(ax, 44, 4, 'O : le puits', 'sujet', 'm')

save(fig, '37-044')
