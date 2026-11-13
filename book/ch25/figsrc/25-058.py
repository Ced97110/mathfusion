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
# angle BAC : A au sommet, B en haut, C a droite
A, B, C = geo(8, 12, 36, 40)
poly(ax, [A, B, C], 'fixe'); sqmark(ax, C)
arc(ax, A, 9, 0, 40, 'sujet', 1.6)
text(ax, A[0] - 3, A[1] - 2.5, 'A', 'sujet', 'l', weight='bold')
text(ax, B[0] + 3, B[1] + 2, 'B', 'fixe', 'l', weight='bold')
text(ax, C[0] + 3, C[1] - 2.5, 'C', 'fixe', 'l', weight='bold')
box(ax, 56, 38, 28, 10, 'fixe', label='tan BAC', size='l')
text(ax, 70, 31, '3 lettres', 'fixe', 's')
arrow(ax, (70, 28), (70, 22), 'varie')
box(ax, 60, 8, 20, 10, 'resultat', label='tan A', size='l')
save(fig, '25-058')
