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
fig, ax = canvas(52)
s = 4; V30 = (6, 14); V80 = (6 + 8 * s, 14); V70 = (6 + 7.261 * s, 14 + 4.193 * s); G = cen(V30, V80, V70)
poly(ax, [V30, V80, V70], 'fixe')
ang(ax, V30, V80, V70, 7, 'fixe'); text(ax, *pt(V30, 14, 12), '30°', 'fixe', 's')
t = ang(ax, V70, V30, V80, 5, 'fixe'); text(ax, *pt(V70, 8, t), '70°', 'fixe', 's')
t = ang(ax, V80, V30, V70, 5, 'sujet', 1.4); text(ax, *pt(V80, 9.5, t), '80°', 'sujet', 's')
sidelab(ax, V30, V80, G, 3.5, '8', 'fixe'); sidelab(ax, V80, V70, G, 5, '4,26', 'varie'); sidelab(ax, V30, V70, G, 5.5, '8,38', 'varie')
bx = [('180° − 30° − 70° = 80°', 'sujet'), ('8 ÷ sin 70° ≈ 8,51', 'fixe'), ('× sin 30° ≈ 4,26', 'varie'), ('× sin 80° ≈ 8,38', 'varie')]
for i, (l, r) in enumerate(bx):
    y = 40 - 10 * i; box(ax, 48, y, 38, 7, r, label=l, size='s')
    if i < 3: arrow(ax, (67, y), (67, y - 3), 'fixe', lw=0.8)
save(fig, '36-072')
