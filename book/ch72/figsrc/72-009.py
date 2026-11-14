import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(74)
ox, oy, u = 10, 10, 9
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -0.2, 3.7, -0.2, 4.6)
arrow(ax, P(0, 0), P(1, 2), 'sujet', lw=1.3); arrow(ax, P(0, 0), P(3, 4), 'autre', lw=1.3)
text(ax, P(3, 4)[0], P(3, 4)[1] + 4, r'$y$ = (3, 4)', 'autre', 'm')
text(ax, P(1, 2)[0] - 2, P(1, 2)[1] + 3, r'$x$ = (1, 2)', 'sujet', 'm', ha='right')
text(ax, 66, 64, r'$B(x,y)$', 'encre', 'l', weight='bold')
text(ax, 66, 54, r'$1\times3+2\times4$', 'encre', 'm')
box(ax, 54, 35, 24, 10, 'resultat', label='= 11', size='l')
text(ax, 66, 27, r'11 $\neq$ 0', 'limite', 'm'); text(ax, 66, 20, 'pas orthogonaux', 'limite', 's')
save(fig, '72-009')
