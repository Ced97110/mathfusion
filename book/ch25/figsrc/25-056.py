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
fig, ax = canvas(72)
A, B, C = geo(14, 14, 54, 40)
poly(ax, [A, B, C], 'fixe'); sqmark(ax, C)
line(ax, [B, C], 'sujet', lw=2.4)
line(ax, [A, C], 'varie', lw=2.4)
line(ax, [A, B], 'resultat', lw=2.4)
vlabels(ax, A, B, C, 'sujet', 'varie', 'resultat')
text(ax, C[0] - 6, mid(B, C)[1], 'a', 'sujet', 'xl', weight='bold')
text(ax, mid(A, C)[0], C[1] + 6, 'b', 'varie', 'xl', weight='bold')
text(ax, mid(A, B)[0] - 5, mid(A, B)[1] + 5, 'c', 'resultat', 'xl', weight='bold')
text(ax, 4, 5, 'A et a', 'sujet', 's', ha='left')
text(ax, 34, 5, 'B et b', 'varie', 's', ha='left')
text(ax, 64, 5, 'C et c', 'resultat', 's', ha='left')
save(fig, '25-056')
