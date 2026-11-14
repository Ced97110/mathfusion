import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(60)
ox, oy, u = 20, 28, 9
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -1.8, 2.8, -1.2, 2.8)
disc(ax, *P(2, 1), 1.4, 'sujet'); text(ax, P(2, 1)[0] + 3, P(2, 1)[1] - 4, r'$P$', 'sujet', 's')
disc(ax, *P(-1, 2), 1.4, 'resultat'); text(ax, P(-1, 2)[0] - 5, P(-1, 2)[1] + 1, 'but', 'resultat', 's')
arrow(ax, P(1.8, 1.4), P(-0.6, 2.0), 'resultat', lw=1.0, curve=0.35)
text(ax, 20, 10, 'quart de tour', 'resultat', 'm')
text(ax, 62, 52, 'Deux questions', 'encre', 'm', weight='bold')
box(ax, 44, 36, 40, 11, 'varie', label='1. Est-ce possible ?', size='s')
box(ax, 44, 22, 40, 11, 'varie', label='2. Combien de plis ?', size='s')
for i, xx in enumerate((46, 58, 70)):
    box(ax, xx, 6, 10, 9, 'varie', fill=False, dash=True, label='pli' if i < 2 else '…', size='s')
save(fig, '72-003')
