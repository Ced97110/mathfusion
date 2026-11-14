import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, tan, radians, degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='fixe'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))
    return (a1 + a2) / 2

s = 0.0105
al, be, hh = 18.0, 21.25, 1975.55
fig, ax = canvas(92)
A = (12, 56); B = (A[0] + 1000*s, 56)
H = (A[0] + hh / tan(radians(al)) * s, 56); S = (H[0], 56 + hh*s)
poly(ax, [A, B, S], 'fixe')
line(ax, [A, H], 'fixe', 0.9); line(ax, [A, B, S, A], 'fixe', 1.0)
line(ax, [B, S], 'sujet', 2.2); line(ax, [S, H], 'resultat', 2.2)
d = 2.2
line(ax, [(H[0] - d, 56), (H[0] - d, 56 + d), (H[0], 56 + d)], 'fixe', 0.7)
wedge(A, B, S, 6, 'varie'); wedge(B, H, S, 5, 'varie'); m = wedge(S, A, B, 8, 'varie')
def leader(label, xy, to):
    line(ax, [xy, to], 'varie', 0.6)
    text(ax, label[0], label[1], label[2], 'varie', 's', weight='bold')
leader((A[0] + 8, 69, '18°'), (A[0] + 8, 67.4), (A[0] + 6*cos(radians(9)), 56 + 6*sin(radians(9))))
leader((B[0] + 10, 71, '21,25°'), (B[0] + 9, 69.4), (B[0] + 5*cos(radians(10.6)), 56 + 5*sin(radians(10.6))))
leader((S[0] - 13, S[1] + 6, '3,25°'), (S[0] - 11, S[1] + 4.3), (S[0] + 8*cos(radians(m)), S[1] + 8*sin(radians(m))))
text(ax, (A[0] + B[0]) / 2, 51.5, '1000 m', 'fixe', 's')
text(ax, (B[0] + S[0]) / 2 + 1.3, (B[1] + S[1]) / 2 - 3.6, 'BS ≈ 5451 m', 'sujet', 's', rot=21.25, weight='bold')
text(ax, H[0] - 2.5, 66, 'h ≈ 1976 m', 'resultat', 's', ha='right', weight='bold')
box(ax, 2, 28, 84, 9, 'fixe', label='angle au sommet : 21,25° − 18° = 3,25°', size='s')
box(ax, 2, 16, 84, 9, 'sujet', label='BS = 1000 × sin 18° ÷ sin 3,25° ≈ 5451 m', size='s')
box(ax, 2, 4, 84, 9, 'resultat', label='h = BS × sin 21,25° ≈ 1976 m', size='s')
arrow(ax, (44, 28), (44, 25.2), 'varie'); arrow(ax, (44, 16), (44, 13.2), 'varie')
save(fig, '38-065')
