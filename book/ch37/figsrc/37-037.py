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
s = 6
# gauche : 5, 5, 6
P1 = (6, 20); P2 = (42, 20); Tt = (24, 44)
poly(ax, [P1, P2, Tt], 'sujet'); line(ax, [Tt, (24, 20)], 'fixe', 0.8, dash=True)
for a, b in ((P1, Tt), (P2, Tt)):
    m = mid(a, b); d = math.atan2(b[1] - a[1], b[0] - a[0]) + math.pi / 2
    for o in (-0.8, 0.8):
        q = (m[0] + o * math.cos(d - math.pi / 2), m[1] + o * math.sin(d - math.pi / 2))
        line(ax, [(q[0] - 1.2 * math.cos(d), q[1] - 1.2 * math.sin(d)), (q[0] + 1.2 * math.cos(d), q[1] + 1.2 * math.sin(d))], 'varie', 1.0)
arcl(P1, 5, 0, 53.13, 'varie', 1.3); arcl(P2, 5, 180 - 53.13, 180, 'varie', 1.3)
text(ax, 9.5, 35, '5', 'sujet', 'm'); text(ax, 38.5, 35, '5', 'sujet', 'm'); text(ax, 24, 15.5, '6', 'sujet', 'm')
text(ax, 9, 15.5, '53,13°', 'varie', 's'); text(ax, 39, 15.5, '53,13°', 'varie', 's')
text(ax, 24, 5, 'deux côtés égaux', 'sujet', 's')
# droite : 3, 4, 5
Q1 = (52, 20); Q2 = (82, 20); T2 = (52 + 1.8 * s, 20 + 2.4 * s)
poly(ax, [Q1, Q2, T2], 'limite')
rsq(T2, ((Q1[0] - T2[0]) / 18, (Q1[1] - T2[1]) / 18), ((Q2[0] - T2[0]) / 24, (Q2[1] - T2[1]) / 24), 2.2)
arcl(Q1, 5, 0, 53.13, 'limite', 1.3); arcl(Q2, 5, 180 - 36.87, 180, 'limite', 1.3)
text(ax, 54.5, 33, '3', 'limite', 'm'); text(ax, 76.5, 33, '4', 'limite', 'm'); text(ax, 67, 15.5, '5', 'limite', 'm')
text(ax, 57, 15.5, '53,13°', 'limite', 's'); text(ax, 78, 15.5, '36,87°', 'limite', 's')
text(ax, 67, 5, 'côtés inégaux', 'limite', 's')

save(fig, '37-037')
