import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
ox, oy, u = 14, 32, 10
Q = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [Q(-0.8, 0), Q(3.4, 0)], 'fixe', lw=0.7); line(ax, [Q(0, -2.8), Q(0, 3.4)], 'fixe', lw=0.7)
line(ax, [Q(-0.5, -0.5), Q(3, 3)], 'limite', lw=0.9, dash=True)
line(ax, [Q(-0.5, 0.5), Q(3, -3)], 'limite', lw=0.9, dash=True)
text(ax, Q(3, 3)[0] + 1, Q(3, 3)[1] + 3, 'carré 0', 'limite', 's', ha='left')
line(ax, [Q(math.cosh(t / 10), math.sinh(t / 10)) for t in range(-18, 19)], 'sujet', lw=1.3)
text(ax, Q(2.6, -1.4)[0], Q(2.6, -1.4)[1], 'carré 1', 'sujet', 's', ha='left')
arrow(ax, Q(0, 0), Q(1, 3), 'autre', lw=1.2)
text(ax, Q(1, 3)[0] + 2, Q(1, 3)[1] + 1, r'$d=(1,3)$', 'autre', 's', ha='left')
text(ax, Q(0.35, 1.7)[0] - 9, Q(0.35, 1.7)[1], 'carré −8', 'autre', 's', ha='right') if False else None
disc(ax, *Q(1, 0), 1.3, 'sujet'); disc(ax, *Q(1.25, 0.75), 1.3, 'resultat')
text(ax, Q(1, 0)[0] - 1, Q(1, 0)[1] - 4, '(1, 0)', 'sujet', 's', ha='right')
arrow(ax, (Q(1, 0)[0] + 1.2, Q(1, 0)[1] + 0.6), (Q(1.25, 0.75)[0] - 0.4, Q(1.25, 0.75)[1] - 1.2), 'varie', lw=1.2)
text(ax, Q(1.25, 0.75)[0] + 3, Q(1.25, 0.75)[1] + 2.5, r'$(5/4,\,3/4)$', 'resultat', 's', ha='left')
text(ax, 70, 62, r'$\eta = S_d\,S_{e_2}$', 'varie', 'm')
text(ax, 70, 55, r'$d$ a pour carré $-8$', 'autre', 's')
save(fig, '72-137')
