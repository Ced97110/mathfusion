import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(52)
line(ax, [(50, 4), (50, 48)], 'fixe', lw=0.6, dash=True)
gy = 14
A = (6, gy)
c, s = math.cos(math.radians(18)), math.sin(math.radians(18))
P = lambda t: (A[0] + t * c, gy + t * s)
line(ax, [(2, gy), (46, gy)], 'fixe')
line(ax, [A, P(40)], 'sujet', lw=1.4)
ax.add_patch(Arc(A, 22, 22, theta1=0, theta2=18, ec=COL['varie'], lw=1.2, zorder=3))
disc(ax, A[0], A[1], 1.3, 'sujet')
text(ax, A[0], gy - 5, '$A$', 'sujet', 's')
for t in (20, 38):
    p = P(t)
    disc(ax, p[0], p[1], 1.3, 'autre')
text(ax, P(20)[0], P(20)[1] + 6.5, 'bas, proche', 'autre', 's')
text(ax, P(38)[0] - 1, P(38)[1] + 6.5, 'haut, lointain', 'autre', 's')
text(ax, 26, gy - 6, '18° dans les deux cas', 'varie', 's')
text(ax, 25, 46, 'une seule visée', 'sujet', 'm')
# deux visées
A2, B2, S = (56, gy), (66, gy), (80, 36)
line(ax, [(52, gy), (86, gy)], 'fixe')
line(ax, [A2, S], 'sujet', lw=1.4)
line(ax, [B2, S], 'varie', lw=1.4)
for p, r in ((A2, 'sujet'), (B2, 'varie'), (S, 'resultat')):
    disc(ax, p[0], p[1], 1.3, r)
text(ax, A2[0], gy - 5, '$A$', 'sujet', 's')
text(ax, B2[0], gy - 5, '$B$', 'varie', 's')
text(ax, S[0], S[1] + 4.5, '$S$', 'resultat', 'm')
text(ax, 69, 46, 'deux visées', 'resultat', 'm')
text(ax, 69, 6, 'un seul point', 'resultat', 's')
save(fig, '38-019')
