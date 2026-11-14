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
fig, ax = canvas(58)
s = 5.5; P = (12, 16); Q = (12 + 6 * s, 16); R = (12 + 2.25 * s, 16 + 3.307 * s); G = cen(P, Q, R)
poly(ax, [P, Q, R], 'fixe')
for n, (V, a, b_, r, role, lab) in enumerate(((R, P, Q, 5, 'sujet', '1'), (P, Q, R, 6, 'varie', '2'), (Q, P, R, 5, 'resultat', '3'))):
    ang(ax, V, a, b_, r, role, 1.3); x, y = out(V, G, 6.0); disc(ax, x, y, 2.4, role, label=lab, size='s')
sidelab(ax, P, Q, G, 3.5, '6', 'fixe'); sidelab(ax, P, R, G, 3.5, '4', 'fixe'); sidelab(ax, Q, R, G, 3.5, '5', 'fixe')
bx = [('étape 1 : loi des\ncosinus\ncos = 5 ÷ 40 → 82,82°', 'sujet'), ('étape 2 : loi des\nsinus\nsin = 0,8268 → 55,77°', 'varie'), ('étape 3 : 180°\n180° − 82,82° − 55,77°\n= 41,41°', 'resultat')]
for i, (l, r) in enumerate(bx):
    y = 40 - 17 * i; box(ax, 56, y, 30, 14, r, label=l, size='s')
    if i < 2: arrow(ax, (71, y), (71, y - 3), 'fixe', lw=0.9)
save(fig, '36-069')
