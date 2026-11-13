import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
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
O = (44, 66); R = 20
A = P(O, R, 90); D = P(O, R, 270); B = P(O, R, 255.64); C = P(O, R, 338.46)
circ(O, R, 'fixe', 1.0)
wedge(O, 11, 90, 255.64, 'fixe'); wedge(O, 15, 255.64, 270, 'varie'); wedge(O, 11, 270, 338.46, 'autre')
arcl(O, 18.5, 255.64, 338.46, 'resultat', 1.6); vang(B, A, O, 4.5, 'sujet', 1.3)
poly(ax, [A, B, C], 'fixe', fill=False)
line(ax, [A, D], 'encre', 1.2); line(ax, [O, B], 'sujet', 1.3); line(ax, [O, C], 'autre', 1.3)
arcl(A, 6, 262.82, 270, 'sujet', 1.3); arcl(A, 8, 270, 304.3, 'autre', 1.3)
dot(O, 'encre')
text(ax, 44, 89, 'A', 'encre', 'm', weight='bold'); text(ax, 44, 41, 'D', 'encre', 'm', weight='bold')
text(ax, *P(O, 23.5, 255.64), 'B', 'encre', 'm', weight='bold'); text(ax, *P(O, 23.5, 338.46), 'C', 'encre', 'm', weight='bold')
text(ax, 50, 66, 'O', 'encre', 'm', weight='bold')
text(ax, 40.5, 76, 'x', 'sujet', 'm', weight='bold'); text(ax, 52, 78, 'y', 'autre', 'm', weight='bold')
text(ax, *P(O, 8.5, 296), '2y', 'autre', 's', weight='bold')
text(ax, 39.5, 53, '2x', 'varie', 's', weight='bold', ha='right')
steps = [('1  OA = OB : angles de base x', 'sujet'), ('2  AOB = 180° − 2x', 'fixe'), ('3  BOD = 2x : A, O, D alignés', 'varie'), ('4  de même COD = 2y', 'autre'), ('5  BOC = 2x + 2y = 2A', 'resultat')]
for i, (l, r) in enumerate(steps):
    box(ax, 8, 31 - 7.2 * i, 72, 6.4, r, label=l, size='s')

save(fig, '37-038')
