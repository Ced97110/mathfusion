import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
S = '\u202f'
def N(s): return s.replace('_', S)
def pt(o, r, d): return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))
def field(o, s, A=50, b=120, c=90):
    a = math.radians(A); return o, (o[0] + c * s, o[1]), (o[0] + b * s * math.cos(a), o[1] + b * s * math.sin(a))
def cen(*P): return (sum(p[0] for p in P) / len(P), sum(p[1] for p in P) / len(P))
def out(P, G, off):
    dx, dy = P[0] - G[0], P[1] - G[1]; n = math.hypot(dx, dy) or 1; return (P[0] + off * dx / n, P[1] + off * dy / n)
def mid(P, Q): return ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
def sidelab(ax, P, Q, G, off, s, role='encre', size='s'):
    x, y = out(mid(P, Q), G, off); text(ax, x, y, s, role, size)
def vlab(ax, V, G, off, s, role='encre', size='m'):
    x, y = out(V, G, off); text(ax, x, y, s, role, size)
def ang(ax, V, P1, P2, r, role='varie', lw=1.0):
    t1 = math.degrees(math.atan2(P1[1] - V[1], P1[0] - V[0])); t2 = math.degrees(math.atan2(P2[1] - V[1], P2[0] - V[0]))
    d = (t2 - t1 + 180) % 360 - 180
    if d < 0: t1, d = t2, -d
    ax.add_patch(Arc(V, 2 * r, 2 * r, theta1=t1, theta2=t1 + d, color=COL[role], lw=lw, zorder=3)); return t1 + d / 2
def rt(ax, V, P1, P2, r=1.8, role='fixe'):
    u = [(P1[0] - V[0], P1[1] - V[1]), (P2[0] - V[0], P2[1] - V[1])]; n = [math.hypot(*v) for v in u]
    a = (V[0] + r * u[0][0] / n[0], V[1] + r * u[0][1] / n[0]); b = (V[0] + r * u[1][0] / n[1], V[1] + r * u[1][1] / n[1])
    line(ax, [a, (a[0] + b[0] - V[0], a[1] + b[1] - V[1]), b], role, lw=0.7)
fig, ax = canvas(57)
s = 0.3; Bv = (16, 12); a2 = math.radians(82.03)
Av = (Bv[0] + 90 * s, Bv[1]); Cv = (Bv[0] + 92.82 * s * math.cos(a2), Bv[1] + 92.82 * s * math.sin(a2)); G = cen(Av, Bv, Cv)
poly(ax, [Av, Bv, Cv], 'fixe'); line(ax, [Av, Cv], 'sujet', lw=1.9)
t = ang(ax, Bv, Av, Cv, 6, 'varie'); text(ax, *pt(Bv, 11, t), '82,03°', 'varie', 's')
sidelab(ax, Bv, Cv, G, 7, 'a = 92,82', 'fixe'); sidelab(ax, Bv, Av, G, 3.5, 'c = 90', 'fixe'); sidelab(ax, Av, Cv, G, 7, 'b = 120', 'sujet')
text(ax, 44, 52, '$b^2=a^2+c^2-2ac\\,\\cos B$', 'encre', 'm')
steps = [(N('a² + c² = 16_715,8'), 'fixe'), (N('2ac cos B ≈ 2_317'), 'fixe'), (N('b² ≈ 14_400'), 'sujet'), ('b ≈ 120', 'resultat')]
for i, (l, r) in enumerate(steps):
    y = 37.5 - 9.5 * i; box(ax, 56, y, 30, 6.5, r, label=l, size='s')
    if i < 3: arrow(ax, (71, y), (71, y - 3), 'varie', lw=0.8)
save(fig, '36-052')
