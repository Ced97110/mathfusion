import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(62)
ox, oy, u = 12, 12, 9
P = lambda x, t: (ox + x * u, oy + t * u)
axes(ax, ox, oy, u, -0.3, 4.0, -0.3, 4.2)
text(ax, P(4.1, 0)[0], oy - 4, r'$x$', 'fixe', 's'); text(ax, ox - 4, P(0, 4.3)[1], r'$t$', 'fixe', 's')
line(ax, [P(3, 0), P(3, 3)], 'fixe', dash=True); line(ax, [P(0, 3), P(3, 3)], 'fixe', dash=True)
disc(ax, *P(3, 3), 1.6, 'sujet')
text(ax, P(3, 3)[0] - 2, P(3, 3)[1] + 4.5, r'événement (3, 3)', 'sujet', 's', ha='center')
box(ax, 46, 30, 40, 18, 'limite', fill=True)
text(ax, 66, 43, r'$x^2+t^2$ = 18', 'limite', 'm'); text(ax, 66, 34.5, 'pas invariante', 'limite', 's')
box(ax, 46, 8, 40, 18, 'resultat', fill=True)
text(ax, 66, 21, r'$x^2-t^2$ = 0', 'resultat', 'm'); text(ax, 66, 12.5, 'invariante', 'resultat', 's')
save(fig, '72-007')
