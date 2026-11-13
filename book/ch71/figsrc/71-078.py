import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
o = (44, 38); s = 6
P = lambda a, b: (o[0] + a * s, o[1] + b * s)
arrow(ax, P(-7, 0), P(7, 0), 'fixe', lw=0.5); arrow(ax, P(0, -4.4), P(0, 5.4), 'fixe', lw=0.5)
for cc, role, lab in [(5, 'fixe', r'$Q=25$'), (-5, 'fixe', r'$Q=25$'), (0, 'sujet', r'$Q=0$')]:
    xs = (-6.5, 6.5) if cc == 0 else (-5.8, 5.8)
    line(ax, [P(xs[0], (cc - xs[0]) / 2), P(xs[1], (cc - xs[1]) / 2)], role, lw=1.6 if cc == 0 else 0.9, dash=(cc != 0))
    q = P(xs[1], (cc - xs[1]) / 2); text(ax, q[0] - 3, q[1] + 4, lab, role, 's')
disc(ax, *P(3, 1), 1.5, 'varie'); disc(ax, *P(2, -1), 1.5, 'sujet')
text(ax, P(3, 1)[0] - 2, P(3, 1)[1] + 4, r'$(3,\,1)$', 'varie', 's')
text(ax, P(2, -1)[0] - 3, P(2, -1)[1] - 5, r'$(2,\,-1)$', 'sujet', 's')
text(ax, 44, 77, r'$Q=(x+2y)^2$ : un seul carré', 'sujet', 's')
text(ax, 44, 6, r'$Q=0$ sur toute la droite $x+2y=0$', 'sujet', 's')
save(fig, '71-078')
