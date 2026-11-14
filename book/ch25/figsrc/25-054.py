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
fig, ax = canvas(62)
u = 8.0
A = (10, 14); C = (10 + 4 * u, 14); B = (C[0], 14 + 3 * u)
poly(ax, [A, B, C], 'fixe'); sqmark(ax, C)
line(ax, [A, B], 'sujet', lw=2.4)
text(ax, mid(A, C)[0], 9, 'b = 4', 'fixe')
text(ax, C[0] + 6, mid(B, C)[1], 'a = 3', 'fixe')
text(ax, mid(A, B)[0] - 5.5, mid(A, B)[1] + 4.5, 'c = 5', 'sujet', 'l', weight='bold')
text(ax, 5, 52, 'hypoténuse AB', 'sujet', 's', ha='left')
text(ax, 62, 38, r'$a^2 + b^2 = c^2$', 'sujet', 'l')
text(ax, 62, 27, '9 + 16 = 25', 'resultat', 'm')
text(ax, 62, 18, 'c est le plus long', 'sujet', 's')
save(fig, '25-054')
