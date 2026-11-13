import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, c = 12, 26, 12
P = lambda i, j: (ox + i * c, oy + j * c)
arrow(ax, (ox, oy), (ox + 4.4 * c, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + 4.4 * c), 'fixe', lw=0.8)
for i in range(4):
    for j in range(4):
        ax.plot(*P(i, j), 'o', ms=1.2, color=COL['fixe'], zorder=1.5)
line(ax, [P(0, 0), (ox + 4.2 * c, oy + 4.2 * c)], 'varie', lw=1.0, dash=True)
text(ax, 62, 72, 'échange', 'varie', 's', ha='left')
text(ax, 62, 68, r'$x\leftrightarrow y$', 'varie', 's', ha='left')
for (i, j), lab, role in [((2, 1), r'$x^2y$', 'sujet'), ((3, 2), r'$x^3y^2$', 'sujet')]:
    disc(ax, *P(i, j), 1.6, role)
for (i, j), lab, role in [((1, 2), r'$xy^2$', 'autre'), ((2, 3), r'$x^2y^3$', 'autre')]:
    disc(ax, *P(i, j), 1.6, role)
disc(ax, *P(1, 1), 1.6, 'fixe')
text(ax, P(2, 1)[0], P(2, 1)[1] - 4.2, r'$x^2y$', 'sujet', 's')
text(ax, P(3, 2)[0] + 3, P(3, 2)[1], r'$x^3y^2$', 'sujet', 's', ha='left')
text(ax, P(1, 2)[0] - 3, P(1, 2)[1], r'$xy^2$', 'autre', 's', ha='right')
text(ax, P(2, 3)[0] + 3, P(2, 3)[1], r'$x^2y^3$', 'autre', 's', ha='left')
text(ax, P(1, 1)[0] - 1, P(1, 1)[1] - 4.2, r'$xy$', 'fixe', 's')
arrow(ax, (P(2, 1)[0] - 1, P(2, 1)[1] + 1.4), (P(1, 2)[0] + 1, P(1, 2)[1] - 1.4), 'varie')
arrow(ax, (P(3, 2)[0] - 1, P(3, 2)[1] + 1.4), (P(2, 3)[0] + 1, P(2, 3)[1] - 1.4), 'varie')
text(ax, ox + 2 * c, 17.5, r'exposant de $x$', 'fixe', 's')
text(ax, 5, oy + 2 * c, r'exposant de $y$', 'fixe', 's', rot=90)
text(ax, 22, 8, r'$x^2y\cdot xy=x^3y^2$', 'sujet', 's')
text(ax, 64, 8, r'$xy^2\cdot xy=x^2y^3$', 'autre', 's')
save(fig, '54-120')
