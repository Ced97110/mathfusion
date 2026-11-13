import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
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
for k, (c, col) in enumerate(((22, 'sujet'), (66, 'autre'))):
    Cn = (c, 34); r = 18
    circ(Cn, r, 'fixe', 1.0)
    Bp = P(Cn, r, 228.59); Cp = P(Cn, r, 311.41)
    line(ax, arcp(Cn, r, 228.59, 311.41), 'fixe', 2.6)
    if k == 0:
        Ap = P(Cn, r, 100)
        line(ax, [Ap, Bp], col, 1.3); line(ax, [Ap, Cp], col, 1.3)
        m = vang(Ap, Bp, Cp, 6, col, 1.2)
        text(ax, *P(Ap, 11.5, m), '41,41°', col, 's')
        text(ax, *out(Ap, Cn, 3), 'A', col, 'm', weight='bold')
        text(ax, c, 9, 'sommet A sur le cercle', col, 's')
    else:
        line(ax, [Cn, Bp], col, 1.3); line(ax, [Cn, Cp], col, 1.3)
        vang(Cn, Bp, Cp, 6, col, 1.2); dot(Cn, col, 1.0)
        text(ax, c, 43, '82,82°', col, 's')
        text(ax, c, 38, 'O', col, 'm', weight='bold')
        text(ax, c, 9, 'sommet O au centre', col, 's')
    text(ax, *out(Bp, Cn, 3.3), 'B', 'encre', 'm', weight='bold'); text(ax, *out(Cp, Cn, 3.3), 'C', 'encre', 'm', weight='bold')

save(fig, '37-034')
