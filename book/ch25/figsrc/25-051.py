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
A, B, C = geo(10, 14, 56, 40)
poly(ax, [A, B, C], 'fixe')
line(ax, [(C[0] - 4, C[1]), (C[0] - 4, C[1] + 4), (C[0], C[1] + 4)], 'sujet', lw=1.4)
disc(ax, *C, 1.6, 'sujet')
vlabels(ax, A, B, C, 'fixe', 'fixe', 'sujet')
text(ax, 52, 8, '90° : angle droit en C', 'sujet', 's')
arrow(ax, (C[0] - 12, 8), (C[0] - 5, 12), 'sujet')
arc(ax, A, 10, 0, 40, 'fixe'); arc(ax, B, 10, 220, 270, 'fixe')
text(ax, 38, 26, 'angles aigus : A et B', 'fixe', 's')
save(fig, '25-051')
