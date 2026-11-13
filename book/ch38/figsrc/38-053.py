import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians

al, s = 51.33, 0.3
fig, ax = canvas(76)
A = (10, 16); B = (A[0] + 150*s, A[1])
P = (A[0] + 162.793*s*cos(radians(al)), A[1] + 162.793*s*sin(radians(al))); H = (P[0], A[1])
poly(ax, [A, B, P], 'sujet')
line(ax, [B, P], 'fixe', 1.0); line(ax, [A, B], 'fixe', 1.0)
line(ax, [P, H], 'fixe', 1.4, dash=True)
line(ax, [A, P], 'sujet', 2.2)
d = 2.4
line(ax, [(H[0] - d, A[1]), (H[0] - d, A[1] + d), (H[0], A[1] + d)], 'fixe', 0.7)
disc(ax, P[0], P[1], 1.1, 'sujet'); disc(ax, A[0], A[1], 1.1, 'fixe'); disc(ax, B[0], B[1], 1.1, 'fixe')
text(ax, A[0] - 3, A[1] - 3, 'A'); text(ax, B[0] + 3, B[1] - 3, 'B'); text(ax, P[0], P[1] + 3.5, 'P')
text(ax, H[0] - 3, H[1] - 3, 'H', 'fixe', 's')
text(ax, (A[0] + P[0]) / 2 - 3, (A[1] + P[1]) / 2 + 3, 'AP ≈ 162,8 m', 'sujet', 's', ha='right', weight='bold')
text(ax, H[0] - 2.5, A[1] + 12, 'w ≈ 127,1 m', 'fixe', 's', ha='right', weight='bold')
text(ax, (A[0] + B[0]) / 2, A[1] - 5.5, 'AB = 150 m', 'fixe', 's')
text(ax, 44, 70, 'AP est le résultat du triangle ABP seul', 'sujet', 's', weight='bold')
text(ax, 44, 4, 'AP (162,8) est plus grand que w (127,1)', 'encre', 's')
save(fig, '38-053')
