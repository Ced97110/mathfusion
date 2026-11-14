import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(66)
ox, oy, u = 12, 12, 8.5
P = lambda x, t: (ox + x * u, oy + t * u)
axes(ax, ox, oy, u, -0.3, 5.6, -0.3, 5.8)
text(ax, P(5.7, 0)[0], oy - 4, r'$x$', 'fixe', 's'); text(ax, ox - 4, P(0, 5.9)[1], r'$t$', 'fixe', 's')
arrow(ax, P(0, 0), P(5.3, 5.3), 'varie', lw=1.3)
text(ax, P(2.6, 3.8)[0] - 8, P(2.6, 3.8)[1] + 2, 'signal', 'varie', 's')
disc(ax, *P(3, 3), 1.5, 'sujet'); disc(ax, *P(5, 5), 1.5, 'sujet')
disc(ax, *P(0, 0), 1.2, 'fixe')
text(ax, 66, 52, r'(3, 3) :', 'sujet', 'm'); text(ax, 66, 45, r'$9-9=0$', 'resultat', 'm')
text(ax, 66, 32, r'(5, 5) :', 'sujet', 'm'); text(ax, 66, 25, r'$25-25=0$', 'resultat', 'm')
text(ax, 66, 3, 'vecteur non nul, carré nul', 'encre', 's')
save(fig, '72-008')
