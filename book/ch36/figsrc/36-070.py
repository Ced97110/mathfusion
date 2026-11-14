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
A, Bp, C = field((8, 12), 0.3); G = cen(A, Bp, C)
poly(ax, [A, Bp, C], 'fixe'); line(ax, [Bp, C], 'sujet', lw=2.2)
ang(ax, A, Bp, C, 7, 'fixe', 1.2); text(ax, *pt(A, 12, 22), '50°', 'fixe', 's')
ang(ax, C, A, Bp, 4.5, 'varie', 1.3); vlab(ax, C, G, 6, '47,97°', 'varie', 's')
ang(ax, Bp, A, C, 4.5, 'resultat', 1.3); vlab(ax, Bp, G, 7, '82,03°', 'resultat', 's')
sidelab(ax, A, C, G, 6, '120', 'fixe'); sidelab(ax, A, Bp, G, 3.5, '90', 'fixe'); sidelab(ax, Bp, C, G, 6, '92,82', 'sujet')
bx = [('loi des cosinus\na = 92,82 m', 'sujet'), ('loi des sinus\nangle = 47,97°', 'varie'), ('180° − 50° − 47,97°\n= 82,03°', 'resultat')]
for i, (l, r) in enumerate(bx):
    y = 40 - 16 * i; box(ax, 50, y + 0, 36, 12, r, label=l, size='s')
    if i < 2: arrow(ax, (68, y), (68, y - 4), 'fixe', lw=0.9)
text(ax, 44, 3, 'six mesures connues : fin', 'encre', 's')
save(fig, '36-070')
