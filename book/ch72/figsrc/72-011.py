import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(80)
ox, oy, u = 24, 40, 17
P = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [P(-0.6, -0.3), P(2.3, 1.15)], 'fixe', lw=0.8, dash=True)
text(ax, P(2.3, 1.15)[0] + 2, P(2.3, 1.15)[1] - 4, r'droite de $x$', 'fixe', 's')
arrow(ax, P(0, 0), P(1.6, 0.8), 'resultat', lw=1.4)
arrow(ax, P(1.6, 0.8), P(1, 2), 'varie', lw=1.4)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.4)
text(ax, P(0.8, 0.4)[0] + 1, P(0.8, 0.4)[1] - 5, r'$p$', 'resultat', 'm')
text(ax, P(1.3, 1.4)[0] + 5, P(1.3, 1.4)[1], r'$q$', 'varie', 'm')
text(ax, P(0.5, 1.0)[0] - 4, P(0.5, 1.0)[1] + 2, r'$y$', 'autre', 'm')
box(ax, 4, 4, 24, 12, 'autre', label='(1, 2)', size='m')
text(ax, 31, 10, '=', 'encre', 'l')
box(ax, 34, 4, 26, 12, 'resultat', label='(1,6 ; 0,8)', size='m')
text(ax, 63, 10, '+', 'encre', 'l')
box(ax, 66, 4, 20, 12, 'varie', label=r'($-$0,6 ; 1,2)', size='s')
save(fig, '72-011')
