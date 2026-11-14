import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(62)
P = plane(ax, 22, 14, 10, 10, (-1.8, 1.8), (-0.5, 4.2))
line(ax, [P(-1.7, 3), P(1.7, 3)], 'sujet', lw=1.5)
text(ax, 22, 5, "aucun point sur l'axe", 'limite', 's')
text(ax, 36, 40, r'$y=3$', 'sujet', 's', ha='left')
text(ax, 38, 11, r'axe des $x$', 'fixe', 's', ha='left')
box(ax, 56, 44, 28, 9, 'sujet', label=r'$y=3$', size='m')
arrow(ax, (70, 44), (70, 35), 'varie'); text(ax, 72.5, 39.5, r'$y$ par 0', 'varie', 's', ha='left')
box(ax, 56, 26, 28, 9, 'limite', label=r'$0=3$', size='m')
text(ax, 70, 20, r'faux pour tout $x$', 'limite', 's')
save(fig, '19-058')
