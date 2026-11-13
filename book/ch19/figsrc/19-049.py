import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(62)
for ox, role, title, cap in ((15, 'sujet', r'$y=2x+1$', 'graphe : une droite'), (60, 'autre', r'$y=x\times x$', 'graphe : une courbe')):
    P = plane(ax, ox, 14, 10, 6.5, (-1.2, 2.8), (-0.5, 5.5))
    text(ax, ox + 10, 57, title, role, 'm'); text(ax, ox + 10, 5, cap, role, 's')
    if role == 'sujet':
        line(ax, [P(-0.4, 0.2), P(2.2, 5.4)], role)
        pts = [(0, 1), (1, 3), (2, 5)]
    else:
        xs = [-1.2 + i * 0.05 for i in range(0, 69)]
        line(ax, [P(x, x * x) for x in xs if x * x <= 5.3], role)
        pts = [(-1, 1), (0, 0), (1, 1), (2, 4)]
    for p in pts: disc(ax, *P(*p), 1.5, role)
save(fig, '19-049')
