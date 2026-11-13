import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, ux, uy = 24, 10, 8.5, 3.8
P = lambda x, y: (ox + x * ux, oy + y * uy)
arrow(ax, (ox, oy), (ox + 7.2 * ux, oy), 'fixe', lw=0.9); arrow(ax, (ox, oy), (ox, oy + 14 * uy), 'fixe', lw=0.9)
p1, p2 = P(2, 5), P(6, 13)
disc(ax, *p1, 1.8, 'fixe'); text(ax, p1[0] + 3, p1[1], r'$x_1,y_1$', 'fixe', 's', ha='left')
line(ax, [(ox, p2[1]), p2, (p2[0], oy)], 'autre', dash=True)
disc(ax, *p2, 2.2, 'autre')
text(ax, p2[0] - 3, p2[1] + 4, r'$(x_2,y_2)$', 'autre', 'm', ha='right')
text(ax, p2[0], oy - 4.5, r'$x_2=6$', 'autre', 'm')
text(ax, ox - 2, p2[1], r'$y_2=13$', 'autre', 'm', ha='right')
save(fig, '19-073')
