import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians
from matplotlib.patches import Arc

fig, ax = canvas(66)
c = (44, 14); r = 30
ax.add_patch(Arc(c, 2*r, 2*r, theta1=0, theta2=180, ec=COL['fixe'], lw=0.9, zorder=2))
line(ax, [(c[0] - r - 4, c[1]), (c[0] + r + 4, c[1])], 'fixe', 0.9)
a1, a2 = 59.47, 120.53
p1 = (c[0] + r*cos(radians(a1)), c[1] + r*sin(radians(a1)))
p2 = (c[0] + r*cos(radians(a2)), c[1] + r*sin(radians(a2)))
line(ax, [(c[0] - r - 2, p1[1]), (c[0] + r + 2, p1[1])], 'resultat', 0.9, dash=True)
line(ax, [c, p1], 'varie', 1.2); line(ax, [c, p2], 'sujet', 1.2)
for p, role in ((p1, 'varie'), (p2, 'sujet')):
    disc(ax, p[0], p[1], 1.2, role)
ax.add_patch(Arc(c, 18, 18, theta1=0, theta2=a1, ec=COL['varie'], lw=0.9, zorder=3))
ax.add_patch(Arc(c, 26, 26, theta1=0, theta2=a2, ec=COL['sujet'], lw=0.9, zorder=3))
text(ax, c[0] + 20, c[1] + 4.5, '59,47°', 'varie', 's', weight='bold')
text(ax, c[0] - 20, c[1] + 8, '120,53°', 'sujet', 's', weight='bold')
text(ax, c[0], c[1] + r + 3.5, 'même hauteur : sin = 0,86136', 'resultat', 's', weight='bold')
text(ax, 44, 4, 'w = 150 × 0,78076 × 0,93483 ÷ 0,86136 ≈ 127,1 m', 'resultat', 's', weight='bold')
text(ax, 44, 62, r'$\sin(180° - x) = \sin x$ avec $x = \alpha + \beta$', 'encre', 's')
text(ax, 44, 56, '180° − α − β = 59,47° et α + β = 120,53°', 'fixe', 's')
save(fig, '38-051')
