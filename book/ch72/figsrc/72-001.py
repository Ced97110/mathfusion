import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(72)
ox, oy, u = 34, 30, 12
P = lambda x, y: (ox + x * u, oy + y * u)
box(ax, 4, 8, 72, 58, 'fixe', dash=True)
axes(ax, ox, oy, u, -2.2, 3.2, -1.2, 2.5)
line(ax, [P(-2.2, -1.1), P(2.2, 1.1)], 'varie', lw=1.2, dash=True)
text(ax, 60, 55, 'droite du pli', 'varie', 's')
arrow(ax, (58, 51), (P(1.8, 0.9)[0]+1, P(1.8, 0.9)[1]+2), 'varie', lw=0.7)
disc(ax, *P(0, 0), 1.3, 'fixe')
text(ax, ox - 7, oy - 4, 'croix', 'fixe', 's')
disc(ax, *P(2, 1), 1.5, 'sujet')
text(ax, P(2, 1)[0] + 3, P(2, 1)[1] - 4.5, 'point', 'sujet', 's')
disc(ax, *P(-1, 2), 1.5, 'resultat', fill=False)
text(ax, P(-1, 2)[0] - 8, P(-1, 2)[1] + 3, 'à atteindre', 'resultat', 's')
arrow(ax, P(1.7, 1.45), P(-0.7, 2.0), 'resultat', lw=1.0, curve=0.35)
text(ax, 45, 15, 'quart de tour voulu, avec des plis', 'encre', 's')
save(fig, '72-001')
