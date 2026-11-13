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
B = (6, 14); N = (26, 14); O = (26, 14 + h)
poly(ax, [B, N, O], 'sujet'); rsq(N, (-1, 0), (0, 1))
line(ax, [O, B], 'varie', 1.6)
vang(O, B, N, 6, 'varie', 1.2)
text(ax, 22.9, 28.2, 'A', 'varie', 's')
text(ax, 3, 10, 'B', 'encre', 'm', weight='bold'); text(ax, 29, 10, 'N', 'encre', 'm', weight='bold'); text(ax, 26, 41, 'O', 'encre', 'm', weight='bold')
text(ax, 16, 10, 'a/2 = 20', 'sujet', 's'); text(ax, 9.5, 30, 'R = 30,24', 'varie', 's')
steps = [('sin A = 20 ÷ 30,24 ≈ 0,6614', 'sujet'), ('a ÷ 2R : 40 ÷ 60,47 ≈ 0,6614', 'fixe'), ('40 ÷ 0,6614 ≈ 60,47 = 2R', 'resultat')]
for i, (l, r) in enumerate(steps):
    y = 42 - 14 * i
    box(ax, 38, y, 49, 9, r, label=l, size='s')
    if i < 2: arrow(ax, (62.5, y), (62.5, y - 5), 'encre')

save(fig, '37-040')
