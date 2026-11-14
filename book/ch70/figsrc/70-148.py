import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
Ox, Oy, u = 28, 40, 24
X = lambda x: Ox + u * x
Yv = lambda y: Oy + u * y
p = lambda x: (x - 2) * (x - 1) * (x - 3)
disc(ax, Ox, Oy, u, 'autre', fill=False, lw=1.3)
n = 160
up = [(1.5 + 0.5 * math.cos(math.pi * i / n), math.sqrt(max(p(1.5 + 0.5 * math.cos(math.pi * i / n)), 0))) for i in range(n + 1)]
line(ax, [(X(x), Yv(y)) for x, y in up] + [(X(x), Yv(-y)) for x, y in reversed(up)], 'sujet', lw=1.4)
line(ax, [(X(1), Oy - 24), (X(1), Oy + 24)], 'fixe', lw=1.1, dash=True)
line(ax, [(X(1), Oy), (X(1) - 20, Oy + 11)], 'limite', lw=1.1, dash=True)
disc(ax, Ox, Oy, 1.0, 'fixe')
text(ax, Ox - 3, Oy + 3, r'$O$', 'fixe', 's')
disc(ax, X(1), Oy, 1.4, 'resultat')
text(ax, X(1) - 3, Oy - 3.5, r'$P$', 'resultat', 's')
text(ax, 70, 62, r'courbe $f=0$', 'sujet', 's')
text(ax, 18, 10, 'cercle de centre $O$\npassant par $P$', 'autre', 's')
text(ax, 72, 18, 'tangente commune', 'fixe', 's')
text(ax, 22, 71, 'oblique en $P$ :\nentre dans le cercle', 'limite', 's')
save(fig, '70-148')
