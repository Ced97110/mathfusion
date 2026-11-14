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
fig, ax = canvas(48)
x0, y0 = 6, 22
line(ax, [(x0 + 20, y0), (x0, y0)], 'fixe')
line(ax, [(x0, y0), (x0 + 20 * math.cos(math.radians(40)), y0 + 20 * math.sin(math.radians(40)))], 'fixe')
arc(ax, (x0, y0), 9, 0, 40, 'sujet', 1.6)
text(ax, 25, 27, '40°', 'sujet', 'm')
text(ax, 14, 11, 'un angle', 'fixe', 's')
arrow(ax, (29, 22), (36, 22), 'varie')
box(ax, 37, 15, 18, 14, 'sujet', label='tan', size='l', weight='bold')
arrow(ax, (57, 22), (62, 22), 'varie')
box(ax, 63, 16, 22, 12, 'resultat', label='0,8391')
text(ax, 74, 11, 'un nombre', 'resultat', 's')
text(ax, 46, 40, '« tangente de »', 'sujet', 'm')
save(fig, '25-055')
