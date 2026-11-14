import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(64)
O = (44, 56); L = 44
A = pt(O, L, -120); B = pt(O, L, -60)
poly(ax, [O, A, B], 'fixe')
line(ax, [O, A], 'sujet', lw=1.5); line(ax, [O, B], 'sujet', lw=1.5)
line(ax, [A, B], 'resultat', lw=2.2)
text(ax, 44, 62.5, 'O', 'sujet', 'm'); text(ax, A[0] - 4, A[1], 'A', 'sujet', 'm'); text(ax, B[0] + 4, B[1], 'B′', 'sujet', 'm')
text(ax, 31, 40, 'r', 'sujet', 'm'); text(ax, 57, 40, 'r', 'sujet', 'm')
text(ax, 44, A[1] - 4, 'AB′ = r', 'resultat', 'm')
text(ax, 44, 46, '60°', 'sujet', 's')
text(ax, A[0] + 7, A[1] + 3, '60°', 'fixe', 's'); text(ax, B[0] - 7, B[1] + 3, '60°', 'fixe', 's')
save(fig, '29-020')
