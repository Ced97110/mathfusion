import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(62)
c = (30, 8); R = 44
A = pt(c, R, 0); B = pt(c, R, 55)
line(ax, arcpts(c, R, -5, 70, 40), 'fixe', lw=0.8)
line(ax, arcpts(c, R, 0, 55, 40), 'resultat', lw=2.2)
line(ax, [c, A], 'sujet', lw=1.2); line(ax, [c, B], 'sujet', lw=1.2)
line(ax, arcpts(c, 11, 0, 55, 30), 'sujet', lw=1.2)
disc(ax, c[0], c[1], 1.2, 'sujet')
text(ax, c[0] - 3, c[1] - 3.5, 'O', 'sujet', 'l')
text(ax, A[0] + 3.5, A[1] - 3, 'A', 'sujet', 'l'); text(ax, B[0] + 3, B[1] + 3, 'B', 'sujet', 'l')
text(ax, 55, 52, 'angle au centre', 'sujet', 'm', ha='left')
arrow(ax, (54, 51), pt(c, 13, 28), 'sujet', curve=0.2)
text(ax, 62, 22, 'arc AB', 'resultat', 'm', ha='left')
text(ax, 17, 40, 'cercle', 'fixe', 'm')
save(fig, '29-018')
