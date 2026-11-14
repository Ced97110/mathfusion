import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(62)
P = plane(ax, 14, 12, 34, 10, (-0.4, 1.7), (-0.3, 4))
line(ax, [P(0, 1), P(1, 3)], 'sujet', lw=1.5); line(ax, [P(0, 1), P(1, 2)], 'autre', lw=1.5)
line(ax, [P(0, 1), P(1, 1)], 'varie', lw=1.2, dash=True)
line(ax, [P(1, 1), P(1, 3)], 'sujet', lw=1.2, dash=True); line(ax, [P(1, 1), P(1, 2)], 'autre', lw=1.2, dash=True)
disc(ax, *P(0, 1), 1.7, 'fixe')
text(ax, 31, 17.5, 'avance 1', 'varie', 's')
text(ax, 51, 33, 'monte 2', 'sujet', 's', ha='left'); text(ax, 51, 26.5, 'monte 1', 'autre', 's', ha='left')
text(ax, 11, 26, r'$(0,\,1)$', 'fixe', 's', ha='right')
save(fig, '19-061')
