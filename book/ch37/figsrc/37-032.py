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
f = lambda v: 14 + 10 * v
line(ax, [(f(0), 84), (f(6), 84)], 'fixe', 1.0)
for v in range(7): line(ax, [(f(v), 83), (f(v), 85)], 'fixe', 0.7)
for v in (0, 2, 6):
    dot((f(v), 84), 'sujet', 1.3); text(ax, f(v), 90, str(v), 'sujet', 'm', weight='bold')
for v in (1, 3, 4):
    line(ax, [(f(v), 66), (f(v), 80)], 'varie', 1.6); text(ax, f(v), 62.5, str(v), 'varie', 'm')
text(ax, 44, 97, 'trois points alignés', 'encre', 'm')
text(ax, 44, 55.5, 'alignés : droites parallèles', 'limite', 's')
Cc = (0.4 * 0, 0); 
C0 = (14, 6); B0 = (14 + 44, 6); A0 = (14 + 120 * 0.4 * math.cos(math.radians(53)), 6 + 120 * 0.4 * math.sin(math.radians(53)))
ax_, ay_ = A0; bx, by = B0; cx, cy = C0
d = 2 * (ax_ * (by - cy) + bx * (cy - ay_) + cx * (ay_ - by))
ux = ((ax_**2 + ay_**2) * (by - cy) + (bx**2 + by**2) * (cy - ay_) + (cx**2 + cy**2) * (ay_ - by)) / d
uy = ((ax_**2 + ay_**2) * (cx - bx) + (bx**2 + by**2) * (ax_ - cx) + (cx**2 + cy**2) * (bx - ax_)) / d
O = (ux, uy)
poly(ax, [A0, B0, C0], 'fixe')
for p, q in ((A0, B0), (B0, C0), (C0, A0)):
    m = mid(p, q); line(ax, [m, O], 'varie', 1.6)
dot(O, 'resultat', 1.5)
for p, q in ((A0, B0), (B0, C0), (C0, A0)):
    m = mid(p, q); dot(m, 'fixe', 0.6)
text(ax, 72, 28, 'triangle : un point\ncommun O', 'resultat', 's')

save(fig, '37-032')
