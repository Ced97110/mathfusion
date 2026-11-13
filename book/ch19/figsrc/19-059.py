import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(64)
ys = [46, 30, 14]
for y, role, s in zip(ys, ('varie', 'sujet', 'resultat'), (r'$x=0$', r'$y=2\times0+1$', r'$y=1$')):
    box(ax, 4, y, 36, 9, role, label=s, size='m')
for y in ys[:2]: arrow(ax, (22, y), (22, y - 7), 'varie')
P = plane(ax, 62, 14, 13, 9, (-1.2, 1.3), (-0.5, 4))
line(ax, [P(-0.5, 0), P(1.2, 3.4)], 'fixe', lw=1.2)
disc(ax, *P(0, 1), 1.9, 'sujet')
arrow(ax, (41, 18.5), (59.8, 22.4), 'varie')
text(ax, P(0, 1)[0] + 3, P(0, 1)[1] - 4.5, r'$(0,\,1)$', 'sujet', 's', ha='left')
text(ax, 66, 54, r'$y=2x+1$', 'fixe', 's')
save(fig, '19-059')
