import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ox, oy, u = 14, 34, 22
X = lambda x: ox + u * x
Yv = lambda y: oy + u * y
line(ax, [(ox - 4, oy), (X(2.3), oy)], 'fixe', lw=0.5)
line(ax, [(X((t / 20) ** 2), Yv(t / 20)) for t in range(-29, 30)], 'sujet', lw=1.4)
line(ax, [(X(0), Yv(0.5)), (X(1.8), Yv(1.4))], 'fixe', lw=1.0, dash=True)
arrow(ax, (X(1), Yv(1)), (X(0.55), Yv(1.9)), 'autre', lw=1.7)
disc(ax, X(1), Yv(1), 1.3, 'varie')
r5 = math.sqrt(5)
t = (2 / r5, 1 / r5); g = (-1 / r5, 2 / r5); s = 2.6
px, py = X(1), Yv(1)
line(ax, [(px + s * t[0], py + s * t[1]), (px + s * (t[0] + g[0]), py + s * (t[1] + g[1])), (px + s * g[0], py + s * g[1])], 'fixe', lw=0.7)
text(ax, X(0.55) - 3, Yv(1.9) + 4, r'$(-1,\ 2)$', 'autre', 's')
text(ax, X(1.8) - 8, Yv(1.4) + 6.5, r'direction $(2,\ 1)$', 'fixe', 's', ha='left')
text(ax, px + 3, py - 4.5, r'$(1,\ 1)$', 'varie', 's', ha='left')
text(ax, X(2.0), Yv(-0.8), r'$y^2-x=0$', 'sujet', 's', ha='left')
text(ax, 62, 8, r'$-1\times2+2\times1=0$', 'resultat', 's')
save(fig, '70-147')
