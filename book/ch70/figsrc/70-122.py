import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy = 8, 10
X = lambda x: ox + 13 * x
Yv = lambda y: oy + 9 * y
arrow(ax, (ox - 2, oy), (X(3.2), oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 2), (ox, Yv(4.5)), 'fixe', lw=0.6)
xs = [0.5 + i * 0.025 for i in range(101)]
line(ax, [(X(x), Yv(1 / x)) for x in xs], 'sujet', lw=1.3)
line(ax, [(X(x), Yv(2 / x)) for x in xs], 'autre', lw=1.3)
text(ax, X(3.0) + 1.5, Yv(1 / 3.0) - 1.0, r'$f$', 'sujet', 's', ha='left')
text(ax, X(3.0) + 1.5, Yv(2 / 3.0) + 1.5, r'$g$', 'autre', 's', ha='left')
text(ax, X(3.2) + 1, oy - 3, r'$x$', 'fixe', 's')
text(ax, ox + 3, Yv(4.5), r'$y$', 'fixe', 's')
# 2 x 2 table of coefficients
cx = [58, 72]
text(ax, 54.5, 46.5, r'$f$', 'sujet', 's')
text(ax, 54.5, 33.5, r'$g$', 'autre', 's')
for j, (a, b) in enumerate([(r'$x$', r'$-1$'), (r'$x$', r'$-2$')]):
    yy = 42 - 13 * j
    box(ax, cx[0], yy, 13, 9, 'varie', label=a)
    box(ax, cx[1], yy, 13, 9, 'fixe', label=b)
text(ax, 71.5, 24, r'$-2x+x$', 'encre', 'm')
box(ax, 58, 8, 27, 10, 'resultat', label=r'$\mathrm{Res}=-x$', size='m')
arrow(ax, (71.5, 21.5), (71.5, 18.5), 'resultat', lw=0.9)
save(fig, '70-122')
