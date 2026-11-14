import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u = (1, 3)
o = (22, 8); s = 12
P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
fig, ax = canvas(56)
arrow(ax, P((-0.5, 0)), P((2.4, 0)), 'fixe', lw=0.8)
arrow(ax, P((0, -0.0)), P((0, 3.6)), 'fixe', lw=0.8)
arrow(ax, P((0, 0)), P((1, 0)), 'resultat', lw=1.8)
arrow(ax, P((0, 0)), P(u), 'sujet', lw=1.2)
arrow(ax, P((1, 0)), P(u), 'varie', lw=1.6)
line(ax, [P((0.9, 0)), P((0.9, 0.1)), P((1, 0.1))], 'fixe')
text(ax, P((2.4, 0))[0] + 2, P((2.4, 0))[1], r'axe $x$ : $v$', 'fixe', 's', ha='left')
text(ax, P((0, 3.6))[0] + 3, P((0, 3.6))[1], r'$y$', 'fixe')
text(ax, P(u)[0] - 3, P(u)[1] + 1, r'$u$', 'sujet')
text(ax, P((0.5, 0))[0], P((0.5, 0))[1] - 3.2, r'$a=1$ le long de $x$', 'resultat', 's', ha='left')
text(ax, P((1, 1.5))[0] + 2, P((1, 1.5))[1], r'$b=3$ le long de $y$', 'varie', 's', ha='left')
save(fig, '41-101')
