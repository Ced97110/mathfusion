import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(78)
ox, oy, u = 34, 32, 11
P = lambda x, y: (ox + x * u, oy + y * u)
sq(ax, P(0, 0), (2*u, 0), (0, -2*u), 'varie')
sq(ax, P(2, 0), (0, 1*u), (1*u, 0), 'varie')
sq(ax, P(0, 0), (2*u, 1*u), (-1*u, 2*u), 'sujet')
poly(ax, [P(0, 0), P(2, 0), P(2, 1)], 'fixe')
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.3)
text(ax, P(1, -1)[0], P(1, -1)[1], '2×2 = 4', 'varie', 's')
text(ax, 66, P(1, 0)[1] + 16, '1×1 = 1', 'varie', 's')
text(ax, P(0.5, 1.5)[0] - 1, P(0.5, 1.5)[1], r'$B(x,x)$ = 5', 'sujet', 'm', weight='bold')
text(ax, 68, 60, r'$x$ = (2, 1)', 'sujet', 'm')
text(ax, 44, 4, '4 + 1 = 5', 'resultat', 'm')
save(fig, '72-015')
