import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
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
s = 0.22
C = (8, 16); B = (8 + 110 * s, 16); A = (8 + 120 * s * math.cos(math.radians(53)), 16 + 120 * s * math.sin(math.radians(53)))
line(ax, [A, B], 'fixe', 0.8); line(ax, [C, B], 'sujet', 1.8); line(ax, [C, A], 'sujet', 1.8)
arcl(C, 5, 0, 53, 'varie', 1.2)
text(ax, 20, 11.5, '110', 'sujet', 's'); text(ax, 9.5, 28, '120', 'sujet', 's'); text(ax, 17, 20, '53°', 'varie', 's')
labs = [('1. deux côtés : 110 et 120', 'sujet'), ('2. produit : 13 200', 'fixe'), ('3. × sin 53° ≈ 0,7986', 'varie'), ('4. moitié : ≈ 5 271', 'resultat')]
for i, (l, r) in enumerate(labs):
    y = 50 - 12 * i
    box(ax, 38, y, 48, 8, r, label=l, size='s')
    if i < 3: arrow(ax, (62, y), (62, y - 4), 'encre')
text(ax, 44, 5, 'autre paire : aussi ≈ 5 271', 'resultat', 's')

save(fig, '37-026')
