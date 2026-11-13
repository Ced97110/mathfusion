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
k = 40 / 154
F = (12, 14); T = (12 + 154 * k, 14); H = (12, 14 + 168 * k)
poly(ax, [F, H, T], 'fixe')
line(ax, [(F[0], F[1] + 3), (F[0] + 3, F[1] + 3), (F[0] + 3, F[1])], 'fixe', lw=0.9)
line(ax, [F, H], 'sujet', lw=2.4); line(ax, [F, T], 'fixe', lw=2.4)
arc(ax, T, 11, 180 - 47.49, 180, 'varie', 1.8)
text(ax, T[0] - 16, T[1] + 3.5, r'$\theta$ = ?', 'varie', 'l', weight='bold')
text(ax, 20, 36, '168 cm', 'sujet', 'm', ha='left')
text(ax, mid(F, T)[0], 9, '154 cm', 'fixe', 'm')
text(ax, 20, 65, 'la personne', 'sujet', 's', ha='left')
text(ax, 60, 55, 'angle cherché :', 'varie', 's', ha='left')
text(ax, 60, 49, r'$\theta$ (thêta)', 'varie', 'm', ha='left')
save(fig, '25-061')
