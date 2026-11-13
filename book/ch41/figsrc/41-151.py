import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, s = 8, 12, 5.0
P = lambda x, y: (ox + x * s, oy + y * s)
# u = <3, 4> et v = <6, 8> sont sur la même droite
line(ax, [P(-0.8, -1.07), P(6.8, 9.07)], 'fixe', lw=0.6, dash=True)
arrow(ax, P(0, 0), P(6, 8), 'autre', lw=1.4)
arrow(ax, P(0, 0), P(3, 4), 'sujet', lw=1.6)
text(ax, P(3, 4)[0] + 4, P(3, 4)[1] - 2, r'$u=\langle 3,\ 4,\ 0\rangle$', 'sujet', 's', ha='left')
text(ax, P(6, 8)[0] + 7, P(6, 8)[1] + 3, r'$v=\langle 6,\ 8,\ 0\rangle$', 'autre', 's', ha='left')
text(ax, 63, 33, 'parallélogramme', 'fixe', 's')
text(ax, 63, 28, 'aplati : aire 0', 'fixe', 's')
box(ax, 44, 4, 42, 15, 'resultat')
text(ax, 65, 14.5, r'$3\times 8-4\times 6$', 'resultat', 's')
text(ax, 65, 8, r'$=24-24=0$', 'resultat', 's')
save(fig, '41-151')
