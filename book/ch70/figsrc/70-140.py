import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
oy, uy = 42, 40
X = lambda x: 8 + 50 * (x - 0.8)
Yv = lambda y: oy + uy * y
p = lambda x: (x - 2) * (x - 1) * (x - 3)
line(ax, [(X(0.8), oy), (X(2.2), oy)], 'fixe', lw=0.6)
n = 160
up = [(1.5 + 0.5 * math.cos(math.pi * i / n), math.sqrt(max(p(1.5 + 0.5 * math.cos(math.pi * i / n)), 0))) for i in range(n + 1)]
line(ax, [(X(x), Yv(y)) for x, y in up] + [(X(x), Yv(-y)) for x, y in reversed(up)], 'sujet', lw=1.3)
for xv in (1.2, 1.5):
    r = math.sqrt(p(xv))
    line(ax, [(X(xv), Yv(-0.72)), (X(xv), Yv(0.72))], 'fixe', lw=0.8, dash=True)
    for s in (-1, 1):
        disc(ax, X(xv), Yv(s * r), 1.1, 'sujet')
    text(ax, X(xv), Yv(0.72) + 3, ('$x=%s$' % str(xv).replace('.', '{,}')), 'fixe', 's')
for xv in (1, 2):
    disc(ax, X(xv), oy, 1.5, 'resultat')
    text(ax, X(xv), oy - 5, '$x=%d$' % xv, 'resultat', 's')
text(ax, 44, 7, 'les deux points deviennent un\nseul en $x=1$, $2$, $3$', 'resultat', 's')
save(fig, '70-140')
