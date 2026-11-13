import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(72)
ox, oy, u = 38, 34, 14
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -2.2, 2.8, -1.2, 2.5)
line(ax, [P(-0.85, -1.7), P(0.85, 1.7)], 'varie', lw=1.3, dash=True)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(-1, 2), 'resultat', lw=1.5)
text(ax, P(2, 1)[0] + 3, P(2, 1)[1] + 3, r'$x$ = (2, 1)', 'sujet', 's', ha='center')
text(ax, P(-1, 2)[0] - 2, P(-1, 2)[1] + 3, r'($-1$, 2)', 'resultat', 's', ha='right')
text(ax, P(1.0, 2.0)[0] + 8, P(1.0, 2.0)[1] - 1, r'$x^\perp$', 'varie', 'l')
text(ax, 44, 4, r'2$\times$($-1$) + 1$\times$2 = 0', 'resultat', 'm')
save(fig, '72-012')
