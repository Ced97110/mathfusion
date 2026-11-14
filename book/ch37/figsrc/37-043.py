import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
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
s = 7.5; Cn = (24, 26); r = 2.5 * s
Pp = (Cn[0] - r, 26); Q = (Cn[0] + r, 26); T = (Cn[0] - 0.7 * s, 26 + 2.4 * s)
circ(Cn, r, 'fixe', 1.0); poly(ax, [Pp, Q, T], 'sujet')
line(ax, [Pp, Q], 'resultat', 2.4)
rsq(T, ((Pp[0] - T[0]) / 22.5, (Pp[1] - T[1]) / 22.5), ((Q[0] - T[0]) / 30, (Q[1] - T[1]) / 30), 2.2) if False else rsq(T, ((Pp[0] - T[0]) / 22.5, (Pp[1] - T[1]) / 22.5), ((Q[0] - T[0]) / 30, (Q[1] - T[1]) / 30), 2.2)
dot(Cn, 'resultat', 1.0)
text(ax, 8.5, 37.5, '3', 'sujet', 'm', weight='bold'); text(ax, 35, 37.5, '4', 'sujet', 'm', weight='bold')
text(ax, 24, 21.5, '5 = 2R', 'resultat', 'm', weight='bold')
text(ax, 66, 53, 'côté ÷ sinus en face', 'fixe', 's')
for i, l in enumerate(['3 ÷ 0,6 = 5', '4 ÷ 0,8 = 5', '5 ÷ 1 = 5']):
    box(ax, 50, 38 - 11 * i, 32, 8, 'resultat', label=l, size='m')

save(fig, '37-043')
