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
A, B, C = geo(12, 14, 56, 40)
poly(ax, [A, B, C], 'fixe'); sqmark(ax, C)
line(ax, [B, C], 'sujet', lw=2.4)
arc(ax, A, 11, 0, 40, 'autre', 1.6)
vlabels(ax, A, B, C, 'autre', 'fixe', 'fixe')
text(ax, C[0] - 5.5, mid(B, C)[1], 'a', 'sujet', 'xl', weight='bold')
text(ax, 77, 40, 'côté BC', 'sujet', 's')
text(ax, 46, 9, 'en face de A', 'autre', 's')
arrow(ax, (25, 19), (64, 33), 'autre', curve=-0.2)
save(fig, '25-052')
