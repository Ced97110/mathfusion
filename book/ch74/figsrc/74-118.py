import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 9.4; ox = 6; oy = 34
P = lambda x, y: (ox + x * u, oy + (y - 1) * u)
line(ax, [P(0, 2), P(8.2, 2)], 'fixe', lw=0.9, dash=True)
text(ax, *P(1.0, 2.0 + 0.0), '', 'fixe', 's')
text(ax, *P(6.6, 2.0 + 0.4), r'axe $x_2=2$', 'fixe', 's')
pts = [(1, 1), (4, 3), (7, 1)]; rl = ['sujet', 'varie', 'resultat']
arrow(ax, P(1.1, 1.1), P(3.85, 2.9), 'varie', lw=1.1); arrow(ax, P(4.15, 2.9), P(6.9, 1.1), 'varie', lw=1.1)
arrow(ax, P(1.2, 1), P(6.8, 1), 'resultat', lw=1.4)
for (x, y), r, lb in zip(pts, rl, ['(1, 1)', '(4, 3)', '(7, 1)']):
    disc(ax, *P(x, y), 1.2, r)
    text(ax, *P(x, y + (0.5 if y == 3 else -0.5)), lb, r, 's')
text(ax, *P(4, 1.45), r'$f\circ f=(6,0)$', 'resultat', 's')
xs = [14, 30, 46, 62]
for i, (x, c) in enumerate(zip(xs, ['b', 'p', 'b', 'p'])):
    text(ax, x, 14, c, 'sujet' if c == 'b' else 'varie', 'xl', weight='bold')
arrow(ax, (xs[0], 20), (xs[2], 20), 'resultat', lw=1.2, curve=-0.4)
text(ax, 30, 29, 'glisse de 2 lettres', 'resultat', 's')
save(fig, '74-118')
