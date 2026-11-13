import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(68)
ys = [56, 40, 24, 8]
for y, role, s in zip(ys, ('sujet', 'varie', 'resultat', 'resultat'), (r'$y=2x+1$', r'$y=2\times0+1$', r'$y=1$', r'$(0,\,1)$')):
    box(ax, 10, y, 40, 9, role, label=s, size='m')
for y, s in zip(ys[:3], (r'remplacer $x$ par 0', r'calculer $y$', 'le point cherché')):
    arrow(ax, (30, y), (30, y - 7), 'varie'); text(ax, 54, y - 3.5, s, 'varie', 's', ha='left')
save(fig, '19-056')
