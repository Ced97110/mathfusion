import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(62)
ox, oy, u = 24, 31, 14
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -1.2, 3.8, -1.8, 1.8)
line(ax, [P(-1.3, 0), P(3.4, 0)], 'varie', lw=1.3)
text(ax, P(3.2, 0)[0] - 2, oy + 3.5, 'axe du pli', 'varie', 's')
line(ax, [P(2, 1), P(2, -1)], 'fixe', dash=True)
for s in (1, -1):
    line(ax, [(P(2, 0)[0] - 1.2, P(2, s*0.5)[1]), (P(2, 0)[0] + 1.2, P(2, s*0.5)[1])], 'fixe', lw=0.9)
disc(ax, *P(2, 1), 1.6, 'sujet'); text(ax, P(2, 1)[0] + 12, P(2, 1)[1], r'$P$ = (2, 1)', 'sujet', 'm')
disc(ax, *P(2, -1), 1.6, 'resultat'); text(ax, P(2, -1)[0] + 14, P(2, -1)[1], r'(2, $-1$)', 'resultat', 'm')
text(ax, P(2, 0)[0] + 15, oy - 3.5, 'même distance', 'fixe', 's')
arrow(ax, P(-0.5, 0.6), P(-0.5, -0.6), 'varie', lw=0.9, curve=-0.3)
text(ax, P(-0.5, 0)[0] - 1, P(-0.5, 0)[1] + 8, 'pli', 'varie', 's')
save(fig, '72-002')
