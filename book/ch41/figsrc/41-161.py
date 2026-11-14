import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 10.0
# gauche : deux vecteurs non colinéaires, <3, 1> = 2 e1 + e2
ox, oy = 6, 22
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(0, 0), P(1, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(1, -1), 'autre', lw=1.5)
arrow(ax, P(1, 1), P(2, 2), 'sujet', lw=1.5)
arrow(ax, P(2, 2), P(3, 1), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(3, 1), 'resultat', lw=1.6)
text(ax, P(0.2, 1.6)[0], P(0.2, 1.6)[1] + 1, r'$\langle 1,\ 1\rangle$', 'sujet', 's')
text(ax, P(0.7, -1.2)[0] + 3, P(0.7, -1.2)[1] - 1, r'$\langle 1,\ -1\rangle$', 'autre', 's')
text(ax, P(3, 1)[0] + 1, P(3, 1)[1] - 4, r'$\langle 3,\ 1\rangle$', 'resultat', 's')
text(ax, 24, 56, r'$2\times\langle 1,1\rangle+1\times\langle 1,-1\rangle$', 'resultat', 's')
# droite : i et 2i sont sur la même droite
ax.add_patch(Rectangle((56, 12), 30, 24, ec=COL['limite'], fc=FILL['limite'], lw=0.8, zorder=1))
arrow(ax, (60, 28), (68, 28), 'sujet', lw=1.5)
arrow(ax, (60, 19), (76, 19), 'autre', lw=1.5)
text(ax, 71, 32, r'$i$', 'sujet', 's')
text(ax, 80, 19, r'$2i$', 'autre', 's')
text(ax, 71, 7, 'pas une base', 'limite', 's')
save(fig, '41-161')
