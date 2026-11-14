import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(60)
P = plane(ax, 14, 10, 30, 10, (-0.4, 1.9), (-0.3, 4.3))
poly(ax, [P(0, 1), P(1, 1), P(1, 3)], 'sujet')
line(ax, [P(-0.35, 0.3), P(1.5, 4)], 'sujet', lw=1.3)
line(ax, [P(0, 1), P(1, 1)], 'varie', lw=1.5); line(ax, [P(1, 1), P(1, 3)], 'varie', lw=1.5)
text(ax, 29, 15.5, 'avancée 1', 'varie', 's'); text(ax, 48, 30, 'montée 2', 'varie', 's', ha='left')
box(ax, 62, 12, 24, 12, 'resultat', label=r'$m=\frac{2}{1}=2$', size='m')
save(fig, '19-063')
