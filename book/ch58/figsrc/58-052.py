import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
assert 2 * 1 - 1 * 1 == 1
text(ax, 44, 50, r'$(u_1,\,\ldots,\,u_n)$ : une liste de $M$', 'encre', 'm')
k = 9.0
def grid(ox, oy):
    P = lambda a, b: (ox + a * k, oy + b * k)
    for i in range(0, 4): line(ax, [P(i, 0), P(i, 3.2)], 'fixe', lw=0.2)
    for j in range(0, 4): line(ax, [P(0, j), P(3.4, j)], 'fixe', lw=0.2)
    return P
P = grid(5, 16)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(1, 1), 'autre', lw=1.5)
text(ax, P(2, 1)[0] + 1, P(2, 1)[1] - 3, r'$u_1=(2,1)$', 'sujet', 's', ha='left')
text(ax, P(1, 1)[0] - 1, P(1, 1)[1] + 3, r'$u_2=(1,1)$', 'autre', 's', ha='center')
text(ax, 22, 8, 'une base', 'resultat', 'm', weight='bold')
Q = grid(50, 16)
arrow(ax, Q(0, 0), Q(2, 1), 'sujet', lw=1.5)
text(ax, Q(2, 1)[0] + 1, Q(2, 1)[1] - 3, r'$u_1=(2,1)$', 'sujet', 's', ha='left')
text(ax, 66, 8, 'pas une base', 'limite', 'm', weight='bold')
save(fig, '58-052')
