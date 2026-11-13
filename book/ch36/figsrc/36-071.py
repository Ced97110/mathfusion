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
fig, ax = canvas(50)
s = 3.2; y0 = 16
P = (6, y0); Q = (6 + 10 * s, y0); R = (6 + 6.736 * s, y0 + 5.653 * s)
poly(ax, [P, Q, R], 'sujet')
ang(ax, P, Q, R, 6, 'varie'); text(ax, *pt(P, 10.5, 20), '40°', 'varie', 's')
ang(ax, Q, P, R, 5, 'varie'); text(ax, *pt(Q, 9.5, 150), '60°', 'varie', 's')
t = ang(ax, R, P, Q, 5, 'resultat'); text(ax, *pt(R, 9, t), '80°', 'resultat', 's')
text(ax, (P[0] + Q[0]) / 2, y0 - 3.5, '10', 'fixe', 's')
P2 = (52, y0); Q2 = (52 + 10 * s, y0)
line(ax, [P2, Q2], 'fixe', lw=1.4)
E1 = pt(P2, 24, 100); E2 = pt(Q2, 24, 100); line(ax, [P2, E1], 'limite', lw=1.4); line(ax, [Q2, E2], 'limite', lw=1.4)
ang(ax, P2, Q2, E1, 6, 'limite'); text(ax, *pt(P2, 11, 50), '100°', 'limite', 's')
ang(ax, Q2, P2, E2, 6, 'limite'); text(ax, *pt(Q2, 10, 140), '80°', 'limite', 's')
text(ax, (P2[0] + Q2[0]) / 2, y0 - 3.5, '10', 'fixe', 's')
text(ax, 68, 46, 'impossible : parallèles,\nils ne se rejoignent pas', 'limite', 's', weight='bold')
text(ax, 22, 42, 'possible', 'sujet', 's', weight='bold')
text(ax, 22, 7, '40° + 60° = 100° < 180°', 'sujet', 's'); text(ax, 68, 7, '100° + 80° = 180°', 'limite', 's')
save(fig, '36-071')
