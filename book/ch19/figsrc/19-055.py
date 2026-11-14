import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(66)
P = plane(ax, 30, 12, 14, 12, (-1.5, 1.5), (-0.5, 3.5))
line(ax, [P(-0.5, 0), P(1.2, 3.4)], 'fixe', lw=1.2)
line(ax, [P(0, -0.4), P(0, 3.4)], 'sujet', lw=1.8)
disc(ax, *P(0, 1), 1.9, 'sujet')
text(ax, 30, 61, r'axe des $y$ : $x=0$', 'sujet', 's')
text(ax, 70, 34, "ordonnée\nà l'origine", 'sujet', 'm')
arrow(ax, (60, 31), (32.3, 24.4), 'sujet')
text(ax, 42, 19, r'$(0,\,1)$', 'sujet', 's')
text(ax, 50, 15, r'$x$', 'fixe', 's')
save(fig, '19-055')
