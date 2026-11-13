import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
Hl = 74
a = math.radians(15)
A = (6, 14); C = (A[0] + Hl * math.cos(a), 14); B = (C[0], 14 + Hl * math.sin(a))
poly(ax, [A, C, B], 'sujet')
line(ax, [A, C], 'resultat', lw=2.0)
s = 3.0
line(ax, [(C[0] - s, 14), (C[0] - s, 14 + s), (C[0], 14 + s)], 'fixe', lw=0.7)
def arc(P, a0, a1, r, role):
    pts = [(P[0] + r * math.cos(math.radians(t)), P[1] + r * math.sin(math.radians(t))) for t in range(int(a0), int(a1) + 1, 2)]
    line(ax, pts, role, lw=0.9)
arc(A, 0, 15, 14, 'sujet')
text(ax, 26, 17.8, '15°', 'sujet', 'm')
arc(B, 180 + 15, 270, 7, 'autre')
text(ax, B[0] - 5.5, B[1] - 12, '75°', 'autre', 'm')
text(ax, (A[0] + B[0]) / 2 - 1, (A[1] + B[1]) / 2 + 4, 'hypoténuse = 1', 'fixe', 's', rot=15)
text(ax, (A[0] + C[0]) / 2, 8, '0,9659', 'resultat', 'm', weight='bold')
text(ax, (A[0] + C[0]) / 2, 3, 'opposé à 75° = adjacent à 15°', 'resultat', 's')
text(ax, 44, 57, r'15° + 75° = 90° : complémentaires', 'encre', 's')
save(fig, '34-117')
