import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 30, 40, 12
P = lambda a, b: (ox + u * a, oy + u * b)
arrow(ax, P(-2.2, 0), P(2.6, 0), 'fixe', lw=0.5)
arrow(ax, P(0, -2.8), P(0, 3.2), 'fixe', lw=0.5)
line(ax, [P(-1.3, 2.6), P(1.3, -2.6)], 'sujet', lw=1.5)
text(ax, *P(-1.3, 2.6 + 0.4), r'$2X+Y=0$', 'sujet', 's', ha='left')
arrow(ax, P(0, 0), P(2, 1), 'autre', lw=1.5)
text(ax, P(2, 1)[0] + 1.5, P(2, 1)[1] + 3, r'$(\alpha,\ \beta)=(2,\ 1)$', 'autre', 's', ha='left')
arrow(ax, P(0, 0), P(1, -2), 'varie', lw=1.5)
text(ax, P(1, -2)[0] + 2, P(1, -2)[1] - 1, r'$(X,\ Y)=(1,\ -2)$', 'varie', 's', ha='left')
a = (2 / math.sqrt(5), 1 / math.sqrt(5)); b = (1 / math.sqrt(5), -2 / math.sqrt(5))
s = 3.0
line(ax, [(ox + s * a[0], oy + s * a[1]), (ox + s * (a[0] + b[0]), oy + s * (a[1] + b[1])), (ox + s * b[0], oy + s * b[1])], 'fixe', lw=0.7)
text(ax, 66, 70, 'pentes $-2$ et $1/2$ :\nproduit $-1$', 'fixe', 's')
save(fig, '70-146')
