import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(52)
text(ax, 44, 49, 'remplacer, puis résoudre', 'varie', 's')
xs = [2.5, 24.5, 46.5, 68.5]
for x, role, s in zip(xs, ('varie', 'sujet', 'sujet', 'resultat'), (r'$y=0$', r'$0=2x+1$', r'$2x=-1$', r'$x=-\frac{1}{2}$')):
    box(ax, x, 33, 17, 10, role, label=s, size='s')
for x in xs[:3]: arrow(ax, (x + 17.4, 38), (x + 21.6, 38), 'varie')
f = numberline(ax, 10, 70, 14, -2, 1, step=0.5, every=2)
disc(ax, f(-0.5), 14, 2.0, 'resultat')
text(ax, f(-0.5), 22, r'$-\frac{1}{2}$', 'resultat', 'm')
save(fig, '19-060')
