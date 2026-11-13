import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(70)
ox, oy, u = 34, 34, 11
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -2.2, 3.4, -2.2, 3.0)
line(ax, [P(-2.1, 0), P(3.0, 0)], 'varie', lw=1.1)
line(ax, [P(-2.0, -2.0), P(2.8, 2.8)], 'autre', lw=1.1)
text(ax, P(3.0, 0)[0] + 1, oy + 3, 'pli 1', 'varie', 's', ha='right')
text(ax, P(2.9, 2.9)[0] + 1, P(2.9, 2.9)[1] + 1, 'pli 2', 'autre', 's', ha='right')
disc(ax, *P(2, 1), 1.5, 'sujet'); text(ax, P(2, 1)[0] + 2, P(2, 1)[1] + 3.5, '(2, 1)', 'sujet', 's', ha='left')
disc(ax, *P(2, -1), 1.5, 'varie'); text(ax, P(2, -1)[0] + 2, P(2, -1)[1] - 3.5, r'(2, $-1$)', 'varie', 's', ha='left')
disc(ax, *P(-1, 2), 1.5, 'resultat'); text(ax, P(-1, 2)[0] - 2, P(-1, 2)[1] + 3.5, r'($-1$, 2)', 'resultat', 's', ha='right')
arrow(ax, P(2, 0.8), P(2, -0.8), 'varie', lw=1.0)
arrow(ax, P(1.7, -1.1), P(-0.9, 1.9), 'autre', lw=1.0, curve=-0.25)
text(ax, 44, 8, 'deux plis suffisent', 'encre', 'm')
save(fig, '72-004')
