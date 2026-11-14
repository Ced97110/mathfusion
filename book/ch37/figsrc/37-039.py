import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
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
h = math.sqrt(RR ** 2 - 400)
B = (10, 14); C = (50, 14); N = (30, 14); O = (30, 14 + h)
poly(ax, [B, C, O], 'sujet'); line(ax, [O, N], 'fixe', 1.2, dash=True)
for a in (B, C):
    m = mid(a, O); d = math.atan2(O[1] - a[1], O[0] - a[0]) + math.pi / 2
    line(ax, [(m[0] - 1.2 * math.cos(d), m[1] - 1.2 * math.sin(d)), (m[0] + 1.2 * math.cos(d), m[1] + 1.2 * math.sin(d))], 'encre', 1.0)
rsq(N, (-1, 0), (0, 1)); rsq(N, (1, 0), (0, 1))
vang(O, B, N, 6, 'varie', 1.4); vang(O, N, C, 6, 'varie', 1.4)
text(ax, 6.5, 14, 'B', 'encre', 'm', weight='bold'); text(ax, 53.5, 14, 'C', 'encre', 'm', weight='bold'); text(ax, 30, 10, 'N', 'encre', 'm', weight='bold')
text(ax, 30, 40.5, 'O', 'encre', 'm', weight='bold'); text(ax, 30, 48, 'BOC = 82,82°', 'sujet', 's')
text(ax, 25.5, 29, 'BON', 'varie', 's'); text(ax, 34.5, 29, 'NOC', 'varie', 's')
text(ax, 30, 5, 'BON = NOC = 41,41°', 'varie', 's')
V = (60, 26)
line(ax, [V, (V[0] + 22 * math.cos(math.radians(20.7)), V[1] + 22 * math.sin(math.radians(20.7)))], 'autre', 1.4)
line(ax, [V, (V[0] + 22 * math.cos(math.radians(-20.7)), V[1] + 22 * math.sin(math.radians(-20.7)))], 'autre', 1.4)
arcl(V, 9, -20.7, 20.7, 'varie', 1.4)
text(ax, 57, 26, 'A', 'autre', 'm', weight='bold') if False else text(ax, 56.5, 26, 'A', 'autre', 'm', weight='bold')
text(ax, 72, 14, 'A = 41,41°', 'varie', 's'); text(ax, 72, 41, 'BON = A', 'resultat', 'm', weight='bold')

save(fig, '37-039')
