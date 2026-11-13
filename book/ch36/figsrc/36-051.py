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
fig, ax = canvas(70)
s = 0.4; oy = 16; A = (34, oy); B = (34 + 90 * s, oy)
C = (34 + 120 * s * math.cos(math.radians(130)), oy + 120 * s * math.sin(math.radians(130))); D = (C[0], oy)
poly(ax, [A, B, C], 'fixe'); line(ax, [C, D], 'fixe', dash=True); line(ax, [D, A], 'varie', lw=2.0)
rt(ax, D, A, C)
ang(ax, A, B, C, 4, 'sujet'); text(ax, *pt(A, 8.5, 62), '130°', 'sujet', 's')
ang(ax, A, D, C, 7, 'varie'); text(ax, *pt(A, 11, 155), '50°', 'varie', 's')
for P, l, dy in ((D, 'D', -2.6), (A, 'A', -2.6), (B, 'B', -2.6), (C, 'C', 3.2)): text(ax, P[0], P[1] + dy, l, 'encre', 'm')
text(ax, D[0] + 3, 33, '$h$', 'fixe', 's')
brace(ax, D[0], A[0], oy - 4.8, 'varie', label='x ≈ 77,13')
brace(ax, A[0], B[0], oy - 4.8, 'fixe', label='90')
text(ax, 62, 46, '$\\cos(180^\\circ-A)=-\\cos A$', 'encre', 's')
text(ax, 44, 3, N('a² = 22_500 + 13_884,2 = 36_384,2'), 'resultat', 's')
save(fig, '36-051')
