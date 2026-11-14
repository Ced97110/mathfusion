import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, s = 12, 22, 12.0
P = lambda x, y: (ox + x * s, oy + y * s)
for a in range(0, 6):
    for b in range(0, 3):
        x, y = P(a, b)
        if (a, b) == (1, 0):
            disc(ax, x, y, 1.5, 'limite')
        elif a % 2 == 0:
            disc(ax, x, y, 1.3, 'sujet')
        else:
            disc(ax, x, y, 1.1, 'fixe', fill=False)
arrow(ax, P(0, 0), P(2, 0), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(0, 1), 'autre', lw=1.5)
text(ax, P(1, 0)[0] + 12, P(1, 0)[1] + 4, '$f_1$ = (2, 0)', 'autre', 's', ha='left')
text(ax, P(0, 1)[0] - 3, P(0, 1)[1] + 3.5, '$f_2$ = (0, 1)', 'autre', 's', ha='left')
text(ax, P(1, 0)[0], P(1, 0)[1] - 4, '(1, 0)', 'limite', 's')
disc(ax, 6, 11, 1.3, 'sujet')
text(ax, 10, 11, 'atteint : $a f_1 + b f_2$', 'sujet', 's', ha='left')
disc(ax, 6, 6, 1.1, 'fixe', fill=False)
text(ax, 10, 6, 'non atteint', 'fixe', 's', ha='left')
disc(ax, 46, 6, 1.5, 'limite')
text(ax, 50, 6, '(1, 0) : non atteint', 'limite', 's', ha='left')
save(fig, '58-292')
