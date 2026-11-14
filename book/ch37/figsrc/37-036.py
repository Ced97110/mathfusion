import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
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
B, C, A, O, R = fld(0.55, (10, 22))
circ(O, R, 'fixe', 1.0)
poly(ax, [A, B, C], 'fixe', fill=False)
line(ax, [O, B], 'autre', 1.4); line(ax, [O, C], 'autre', 1.4)
vang(A, B, C, 4.5, 'sujet', 1.3); vang(O, B, C, 7, 'autre', 1.3); dot(O, 'autre')
text(ax, A[0] + 2, A[1] + 3.2, 'A', 'sujet', 'm', weight='bold')
text(ax, B[0] - 2.5, B[1] - 2.5, 'B', 'encre', 'm', weight='bold'); text(ax, C[0] + 2.5, C[1] - 2.5, 'C', 'encre', 'm', weight='bold')
text(ax, O[0] + 3, O[1] + 3, 'O', 'autre', 'm', weight='bold') if False else text(ax, O[0] + 3.5, O[1] + 2.5, 'O', 'autre', 'm', weight='bold')
u = 0.45
box(ax, 46, 42, 41.41 * u, 7, 'sujet', label='41,41°', size='s'); text(ax, 46 + 41.41 * u / 2, 53, 'angle inscrit A', 'sujet', 's')
box(ax, 46, 20, 41.41 * u, 7, 'autre', label='41,41°', size='s'); box(ax, 46 + 41.41 * u, 20, 41.41 * u, 7, 'autre', label='41,41°', size='s')
text(ax, 65, 14, 'angle au centre = 82,82°', 'autre', 's')
arrow(ax, (50, 41), (50, 28.5), 'varie'); text(ax, 56, 34.5, '× 2', 'varie', 'm', weight='bold')

save(fig, '37-036')
