import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, ux, uv = 10, 12, 5.8, 9
P = lambda x, v: (ox + x * ux, oy + v * uv)
arrow(ax, (ox, oy), (ox + 12 * ux + 4, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, oy + 4 * uv + 4), 'fixe', lw=0.8)
text(ax, ox + 12 * ux + 4, oy - 3, r'$x$', 'fixe', 's'); text(ax, ox - 4, oy + 4 * uv + 4, r'$v$', 'fixe', 's')
for (x0, x1, v, tag) in [(3, 5, 1, 2), (3, 11, 4, 8)]:
    arrow(ax, (P(x0, v)[0] + 2, P(x0, v)[1]), (P(x1, v)[0] - 2, P(x1, v)[1]), 'varie')
    disc(ax, *P(x0, v), 1.8, 'sujet'); disc(ax, *P(x1, v), 1.8, 'resultat')
    text(ax, (P(x0, v)[0] + P(x1, v)[0]) / 2, P(x0, v)[1] + 4.5, rf'$+2v$ = {tag}', 'varie', 's')
text(ax, P(3, 0)[0], oy - 3, '3', 'sujet', 's'); text(ax, P(5, 0)[0], oy - 3, '5', 'resultat', 's'); text(ax, P(11, 0)[0], oy - 3, '11', 'resultat', 's')
text(ax, ox - 3, P(0, 1)[1], '1', 'fixe', 's'); text(ax, ox - 3, P(0, 4)[1], '4', 'fixe', 's')
text(ax, P(3, 0)[0], P(0, 4)[1] + 5, 'départ', 'sujet', 's'); text(ax, 74, P(0, 4)[1] + 5, 'après 2 s', 'resultat', 's')
text(ax, 44, 64, r'$(x,\ v) \to (x + 2v,\ v)$', 'encre', 'l')
save(fig, '75-004')
