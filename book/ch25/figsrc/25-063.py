import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def geo(x, y, w, deg):
    h = w * math.tan(math.radians(deg)); return (x, y), (x + w, y + h), (x + w, y)
def arc(ax, P, r, a0, a1, role, lw=1.2):
    ax.add_patch(Arc(P, 2 * r, 2 * r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def sqmark(ax, P, s=3.0, role='fixe'):
    line(ax, [(P[0] - s, P[1]), (P[0] - s, P[1] + s), (P[0], P[1] + s)], role, lw=0.9)
def tri(ax, A, B, C, role='fixe'):
    poly(ax, [A, B, C], role); sqmark(ax, C)
def mid(P, Q): return ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
def vlabels(ax, A, B, C, ra='fixe', rb='fixe', rc='fixe'):
    text(ax, A[0] - 3, A[1] - 2.5, 'A', ra, 'l', weight='bold')
    text(ax, B[0] + 3, B[1] + 2, 'B', rb, 'l', weight='bold')
    text(ax, C[0] + 3, C[1] - 2.5, 'C', rc, 'l', weight='bold')
fig, ax = canvas(66)
u = 8.0
A = (8, 14); C = (8 + 4 * u, 14); B = (C[0], 14 + 3 * u)
poly(ax, [A, B, C], 'fixe'); sqmark(ax, C)
line(ax, [B, C], 'varie', lw=2.4); line(ax, [A, C], 'sujet', lw=2.4)
arc(ax, A, 9, 0, 36.87, 'fixe', 1.4)
text(ax, A[0] - 3, A[1] - 2.5, 'A', 'fixe', 'l', weight='bold')
text(ax, C[0] + 6, mid(B, C)[1], 'a = 3', 'varie', 'm', weight='bold')
text(ax, mid(A, C)[0], 8, 'b = 4', 'sujet', 'm', weight='bold')
text(ax, 62, 56, r'tan A = $a/b$', 'encre', 'l', weight='bold')
text(ax, 62, 46, 'a : opposé', 'varie', 's')
text(ax, 62, 40, 'b : adjacent', 'sujet', 's')
arrow(ax, (62, 36), (62, 30), 'fixe')
text(ax, 62, 25, '3 ÷ 4 = 0,75', 'resultat', 'm', weight='bold')
text(ax, 62, 15, '6 ÷ 8 = 0,75', 'resultat', 's')
save(fig, '25-063')
