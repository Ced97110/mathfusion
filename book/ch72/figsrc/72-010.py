import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(72)
ox, oy, u = 26, 20, 17
P = lambda x, y: (ox + x * u, oy + y * u)
import math
axes(ax, ox, oy, u, -1.2, 3.0, -0.2, 3.0, 'fixe')
n = math.sqrt(5)
line(ax, [P(-1.1, -0.55), P(2.9, 1.45)], 'fixe', lw=0.8, dash=True)
line(ax, [P(0.6, -1.2), P(-1.0, 2.0)], 'fixe', lw=0.8, dash=True)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.4)
arrow(ax, P(0, 0), P(1.6, 0.8), 'resultat', lw=1.2)
arrow(ax, P(0, 0), P(-0.6, 1.2), 'varie', lw=1.2)
line(ax, [P(1, 2), P(1.6, 0.8)], 'fixe', dash=True); line(ax, [P(1, 2), P(-0.6, 1.2)], 'fixe', dash=True)
sdx, sdy = 2/n, 1/n; qx, qy = -1/n, 2/n; a = 3.0
line(ax, [(ox + a*sdx, oy + a*sdy), (ox + a*(sdx+qx), oy + a*(sdy+qy)), (ox + a*qx, oy + a*qy)], 'limite', lw=0.9)
text(ax, P(2, 1)[0] + 7, P(2, 1)[1] - 3, r'$x$', 'sujet', 'm')
text(ax, P(1, 2)[0] + 3, P(1, 2)[1] + 3, r'$y$', 'autre', 'm')
text(ax, P(1.6, 0.8)[0] + 1, P(1.6, 0.8)[1] - 5, r'$p$', 'resultat', 'm')
text(ax, P(-0.6, 1.2)[0] - 5, P(-0.6, 1.2)[1] + 1, r'$q$', 'varie', 'm')
text(ax, 74, 62, r'$y=p+q$', 'encre', 'm')
text(ax, 72, 8, r'droite de $x$', 'fixe', 's'); text(ax, 22, 66, r'droite $x^\perp$', 'fixe', 's')
save(fig, '72-010')
