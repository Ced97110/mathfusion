import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, u = 12, 10, 14
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-0.4, 0), P(4.2, 0), 'fixe'); arrow(ax, P(0, -0.4), P(0, 4.6), 'fixe')
for v in range(1, 5):
    ax.plot([P(v, 0)[0]] * 2, [oy - 1, oy + 1], color=COL['fixe'], lw=0.7)
    text(ax, P(v, 0)[0], oy - 3.2, str(v), 'fixe', 's')
for v in range(1, 5):
    ax.plot([ox - 1, ox + 1], [P(0, v)[1]] * 2, color=COL['fixe'], lw=0.7)
    text(ax, ox - 3.2, P(0, v)[1], str(v), 'fixe', 's')
line(ax, [P(0, 3), P(3, 0)], 'sujet', lw=1.3)
line(ax, [P(0, 1), P(3, 4)], 'autre', lw=1.3)
text(ax, P(3, 0)[0] + 2, P(3, 0)[1] + 4, r'$x+y=3$', 'sujet', 'm', ha='left')
text(ax, P(3, 4)[0] + 2, P(3, 4)[1], r'$y-x=1$', 'autre', 'm', ha='left')
disc(ax, *P(1, 2), 1.5, 'resultat')
text(ax, P(1, 2)[0] + 3, P(1, 2)[1] + 4, r'$c=(1\,;\,2)$', 'resultat', 'm', ha='left')
text(ax, 44, 74, r'$(I-A)\,c=b$ : 2 équations', 'encre', 'm')
save(fig, '74-049')
