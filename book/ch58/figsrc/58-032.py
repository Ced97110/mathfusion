import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
k = 6.0
def panel(ox, oy):
    P = lambda a, b: (ox + a * k, oy + b * k)
    for i in range(0, 7): line(ax, [P(i, 0), P(i, 5.2)], 'fixe', lw=0.2)
    for j in range(0, 6): line(ax, [P(0, j), P(6.2, j)], 'fixe', lw=0.2)
    return P
# gauche : axes
P = panel(5, 8)
line(ax, [P(0, 0), P(5, 0), P(5, 4)], 'fixe', lw=1.4, dash=True)
disc(ax, *P(5, 4), 1.5, 'sujet')
text(ax, P(5, 4)[0] - 3.5, P(5, 4)[1] + 3, r'$w$', 'sujet', 'l', weight='bold')
text(ax, P(2.5, 0)[0], P(0, 0)[1] - 3.2, '5', 'fixe')
text(ax, P(5, 2)[0] + 1.5, P(5, 2)[1], '4', 'fixe', ha='left')
text(ax, 22, 47, 'axes : 5 et 4', 'fixe', 'm')
# droite : flèches
Q = panel(50, 8)
arrow(ax, Q(0, 0), Q(4, 2), 'autre', lw=1.4)
arrow(ax, Q(4, 2), Q(5, 4), 'autre', lw=1.4)
disc(ax, *Q(5, 4), 1.5, 'sujet')
text(ax, Q(5, 4)[0] - 3.5, Q(5, 4)[1] + 3, r'$w$', 'sujet', 'l', weight='bold')
text(ax, Q(2, 1)[0] + 0.5, Q(2, 1)[1] + 4, '2', 'autre')
text(ax, Q(4.5, 3)[0] - 3, Q(4.5, 3)[1], '1', 'autre')
text(ax, 66, 47, 'flèches : 2 et 1', 'autre', 'm')
text(ax, 44, 2.5, 'le point w est au même endroit', 'encre', 's')
save(fig, '58-032')
