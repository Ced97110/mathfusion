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
A = (8, 14); u = 5.0
for k, (a, b) in enumerate(((3, 4), (6, 8))):
    C = (A[0] + b * u, A[1]); B = (C[0], A[1] + a * u)
    line(ax, [B, C], 'varie', lw=2.0); line(ax, [A, C], 'sujet', lw=2.0)
    if k == 1: line(ax, [(C[0] - 3, C[1]), (C[0] - 3, C[1] + 3), (C[0], C[1] + 3)], 'fixe', lw=0.9)
line(ax, [A, (A[0] + 8 * u, A[1] + 6 * u)], 'fixe', dash=True, lw=1.2)
text(ax, A[0] + 4 * u / 2, A[1] + 3.2, '4', 'sujet', 's')
text(ax, A[0] + 8 * u / 2, 9, '8', 'sujet', 's')
text(ax, A[0] + 4 * u - 2.5, A[1] + 3 * u / 2, '3', 'varie', 's')
text(ax, A[0] + 8 * u + 3, A[1] + 3 * u, '6', 'varie', 's')
text(ax, A[0] + 4 * u / 2 - 7, A[1] + 3 * u / 2 + 4, 'c = 5', 'fixe', 's')
text(ax, A[0] + 8 * u / 2 - 8, A[1] + 3 * u + 4, 'c = 10', 'fixe', 's')
text(ax, 56, 47, 'tan A = 3 ÷ 4 = 0,75', 'resultat', 's', ha='left')
text(ax, 56, 39, 'tan A = 6 ÷ 8 = 0,75', 'resultat', 's', ha='left')
text(ax, 56, 28, 'c = 5, puis 10 :', 'fixe', 's', ha='left')
text(ax, 56, 21, 'c ne sert pas', 'fixe', 's', ha='left')
text(ax, 56, 14.5, 'dans tan A', 'fixe', 's', ha='left')
line(ax, [(55.5, 28), (75.5, 28)], 'fixe', lw=0.0) if False else None
save(fig, '25-064')
