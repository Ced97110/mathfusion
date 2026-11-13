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
cols = [15, 44, 73]; roles = ['fixe', 'sujet', 'autre']
forms = ['$b^2+c^2$', '$b^2+c^2-2bc\\,\\cos A$', '$a/\\sin A$']
titles = ['Pythagore', 'loi des cosinus', 'loi des sinus']
conds = ['angle droit\nseulement', '2 côtés +\nangle compris', '1 côté +\nangle en face']
for x, r, f, t, c in zip(cols, roles, forms, titles, conds):
    text(ax, x, 41, f, r, 's'); text(ax, x, 14, t, r, 's', weight='bold'); text(ax, x, 8, c, r, 's')
y0 = 20
P = [(8, y0), (22, y0), (8, y0 + 11)]; poly(ax, P, 'fixe'); rt(ax, P[0], P[1], P[2], 2.0, 'fixe')
line(ax, [P[0], P[1]], 'fixe', lw=1.8); line(ax, [P[0], P[2]], 'fixe', lw=1.8)
Q = [(35, y0), (53, y0), (48, y0 + 12)]; poly(ax, Q, 'sujet'); line(ax, [Q[0], Q[1]], 'sujet', lw=1.8); line(ax, [Q[0], Q[2]], 'sujet', lw=1.8)
ang(ax, Q[0], Q[1], Q[2], 5, 'varie')
R = [(64, y0), (82, y0), (70, y0 + 12)]; poly(ax, R, 'autre'); line(ax, [R[0], R[1]], 'autre', lw=1.8)
ang(ax, R[2], R[0], R[1], 4, 'varie')
arrow(ax, (23, 41), (31, 41), 'varie'); text(ax, 26.5, 46.5, '+ correction', 'varie', 's')
save(fig, '36-062')
