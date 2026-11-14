import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(66)
P = plane(ax, 40, 26, 14, 11, (-2.3, 1.6), (-1.5, 3.3))
line(ax, [P(-1.2, -1.4), P(1.1, 3.2)], 'fixe', lw=1.2)
line(ax, [P(-2.2, 0), P(1.5, 0)], 'sujet', lw=1.8)
disc(ax, *P(-0.5, 0), 1.9, 'sujet'); disc(ax, *P(0, 1), 1.9, 'autre')
text(ax, 30, 15, "abscisse à l'origine\n" + r'$(-\frac{1}{2},\,0)$', 'sujet', 's')
text(ax, 44.5, 37, "ordonnée\nà l'origine", 'autre', 's', ha='left')
text(ax, 18, 30, r'$y=0$', 'sujet', 's')
save(fig, '19-057')
