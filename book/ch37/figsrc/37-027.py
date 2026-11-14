import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
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
s = 0.5
B = (16, 44); C = (16 + 110 * s, 44)
A = (B[0] + 103.01 * s * math.cos(math.radians(68.48)), 44 + 103.01 * s * math.sin(math.radians(68.48)))
poly(ax, [A, B, C], 'fixe')
line(ax, [B, C], 'sujet', 2.2)
arcl(B, 8, 0, 68.48, 'varie', 1.2); arcl(C, 8, 180 - 53, 180, 'varie', 1.2); vang(A, B, C, 8, 'resultat', 1.2)
text(ax, 43.5, 38.5, 'a = 110', 'sujet', 'm', weight='bold')
text(ax, 9, 38.5, 'B = 68,48°', 'varie', 's'); text(ax, 80, 38.5, 'C = 53°', 'varie', 's')
text(ax, A[0], A[1] + 5, 'A = 58,52°', 'resultat', 'm')
text(ax, 44, 28, 'A = 180 − 68,48 − 53 = 58,52°', 'resultat', 's')
text(ax, 44, 19, '½ × 110² × 0,9303 × 0,7986', 'encre', 's')
text(ax, 44, 11, '÷ 0,8528 ≈ 5 271', 'resultat', 'm', weight='bold')

save(fig, '37-027')
