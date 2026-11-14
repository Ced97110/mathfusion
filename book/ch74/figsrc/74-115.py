import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 7.5; ox = 8; oy = 24
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-0.2, 0), P(4.4, 0), 'fixe', lw=0.8)
line(ax, [P(0, -2.2), P(0, 3.4)], 'fixe', lw=0.8)
pairs = [((1, 1), (4, 3), 'sujet'), ((0, 2), (3, 2), 'sujet')]
for (p0, p1, _r) in pairs:
    mid = (p0[0], -p0[1])
    disc(ax, *P(*p0), 1.1, 'sujet'); disc(ax, *P(*mid), 0.9, 'fixe'); disc(ax, *P(*p1), 1.1, 'resultat')
    arrow(ax, P(p0[0], p0[1] - 0.2 * (1 if p0[1] > 0 else -1)), P(mid[0], mid[1] + 0.2), 'varie', lw=1.1)
    arrow(ax, P(*mid), P(p1[0] - 0.1, p1[1] - 0.1), 'resultat', lw=1.1)
text(ax, *P(1.15, 1.0), '(1, 1)', 'sujet', 's', ha='left'); text(ax, *P(4.2, 3.0), '(4, 3)', 'resultat', 's', ha='left')
text(ax, *P(0.2, 2.45), '(0, 2)', 'sujet', 's', ha='left'); text(ax, *P(2.7, 2.6), '(3, 2)', 'resultat', 's')
text(ax, *P(0.55, -0.45), 'A', 'varie', 's'); text(ax, *P(3.2, 0.1), '+ b', 'resultat', 's')
box(ax, 50, 40, 36, 10, 'varie', label='A : miroir de l’axe', size='s')
box(ax, 50, 24, 36, 10, 'resultat', label='b = (3, 4) : glissement', size='s')
text(ax, 68, 12, 'f(x) = A x + b', 'encre', 's')
save(fig, '74-115')
