import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 14, 24, 58, 'sujet')
text(ax, 14, 66, r'$A$', 'sujet', 'l')
box(ax, 5, 46, 18, 9, 'sujet', fill=False, label=r'$2+i$')
box(ax, 5, 24, 18, 9, 'sujet', fill=False, label=r'$i$')
text(ax, 38, 82, r'$\rho$ : élément $\to$ transformation', 'varie', 's', ha='left') if False else None
def plane(x0, y0, pts, head, imgs):
    box(ax, x0, y0, 52, 34, 'fixe')
    text(ax, x0 + 26, y0 + 30, head, 'varie', 's')
    o = (x0 + 18, y0 + 6); u = 6.5
    P = lambda a, b: (o[0] + a * u, o[1] + b * u)
    line(ax, [(o[0]-10, o[1]), (o[0]+22, o[1])], 'fixe', lw=0.5); line(ax, [(o[0], o[1]-3), (o[0], o[1]+22)], 'fixe', lw=0.5)
    for (a, b), s, dx, dy in pts:
        disc(ax, *P(a, b), 1.1, 'fixe'); text(ax, P(a, b)[0] + dx, P(a, b)[1] + dy, s, 'fixe', 's')
    for (p, q, s, dx, dy) in imgs:
        arrow(ax, (P(*p)[0] + (0.8 if q[0] >= p[0] else -0.8), P(*p)[1] + 0.8), (P(*q)[0] - (0.8 if q[0] >= p[0] else -0.8), P(*q)[1] - 0.8), 'varie', curve=0.0)
        if s: text(ax, P(*q)[0] + dx, P(*q)[1] + dy, s, 'varie', 's')
plane(34, 46, [((1, 0), '1', 0, -2.6), ((0, 1), r'$i$', 0, 2.6)], r'$\rho(2+i)$',
      [((1, 0), (2, 1), r'$2+i$', 2.5, -2.6), ((0, 1), (-1, 2), r'$-1+2i$', 0, 2.8)])
plane(34, 6, [((1, 0), '1', 0, -2.6), ((0, 1), r'$i$', 0, 2.6)], r'$\rho(i)$',
      [((1, 0), (0, 1), None, 0, 0), ((0, 1), (-1, 0), r'$-1$', 0, -2.6)])
arrow(ax, (27, 50), (33, 56), 'varie'); arrow(ax, (27, 28), (33, 22), 'varie')
text(ax, 14, 8, r'$\rho$ : règle', 'varie', 's')
save(fig, '77-030')
