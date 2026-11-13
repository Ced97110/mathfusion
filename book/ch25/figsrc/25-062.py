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
fig, ax = canvas(60)
A = (10, 12); R = 56
ends = {}
for deg, role in ((0, 'fixe'), (28, 'autre'), (55, 'sujet')):
    P = (A[0] + R * math.cos(math.radians(deg)), A[1] + R * math.sin(math.radians(deg)))
    arrow(ax, A, P, role, lw=1.4); ends[deg] = P
arc(ax, A, 14, 0, 28, 'autre', 1.6); arc(ax, A, 24, 0, 55, 'sujet', 1.6)
text(ax, 31, 16.5, r'$\theta$', 'autre', 'l', weight='bold')
text(ax, 27, 33, r'$\varphi$', 'sujet', 'l', weight='bold')
text(ax, 60, 52, r'$\varphi$ : 2e angle', 'sujet', 'm', ha='left')
text(ax, 60, 44, 'lu « fi »', 'sujet', 's', ha='left')
text(ax, 48, 5, r'$\theta$ : 1er angle', 'autre', 'm', ha='left')
save(fig, '25-062')
