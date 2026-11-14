import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
c = (44, 60)
s = 6
P = (c[0] - 4 * s, c[1] + 4 * s)
Q = (c[0] + 4 * s, c[1] - 4 * s)
line(ax, [(6, 60), (82, 60)], 'fixe', lw=0.6)
line(ax, [(44, 32), (44, 90)], 'fixe', lw=0.6)
line(ax, [c, Q], 'limite', lw=1.0, dash=True)
line(ax, [c, P], 'resultat', lw=1.6)
r = 12
pts = [(c[0] + r * math.cos(math.radians(-45 + 180 * j / 40)), c[1] + r * math.sin(math.radians(-45 + 180 * j / 40))) for j in range(41)]
line(ax, pts, 'varie', lw=1.2)
arrow(ax, pts[-3], pts[-1], 'varie', lw=1.2)
disc(ax, *P, 1.6, 'resultat')
text(ax, P[0], P[1] + 4.5, r'$P\,(-4,\ 4)$', 'resultat', 's')
text(ax, 58, 73, '+ 180°', 'varie', 's')
text(ax, 29, 66, 'θ = 135°', 'resultat', 's')
text(ax, 62, 28, 'arctan(−1) = −45°', 'limite', 's')
text(ax, 4, 20, 'x > 0 : arctan(y/x)', 'encre', 's', ha='left')
text(ax, 4, 12, 'x < 0 : arctan(y/x) + 180°', 'resultat', 's', ha='left')
text(ax, 4, 4, 'x = 0 : 90° ou 270°', 'encre', 's', ha='left')
save(fig, '39-035')
