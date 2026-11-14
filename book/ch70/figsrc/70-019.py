import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
ux, uy, ox, oy = 7.0, 2.6, 46.0, 30.0
P = lambda y, v: (ox + ux * y, oy + uy * v)
arrow(ax, P(-5.4, 0), P(1.6, 0), 'fixe', lw=0.6)
arrow(ax, P(0, -6.8), P(0, 13.0), 'fixe', lw=0.6)
text(ax, P(1.6, 0)[0] + 2.5, oy - 1.5, r'$y$', 'fixe', 's')
f = lambda y: 2 * y + 6
g = lambda y: 3 * y + 9
line(ax, [P(-5, f(-5)), P(1, f(1))], 'sujet', lw=1.4)
line(ax, [P(-5, g(-5)), P(1, g(1))], 'autre', lw=1.4)
disc(ax, *P(-3, 0), 1.3, 'resultat')
text(ax, P(-3, 0)[0], oy + 4, '$-3$', 'resultat', 's')
text(ax, 72, 60, r'$f=2y+6$', 'sujet', 'm')
text(ax, 72, 54, r'$a_1=2$, $a_0=6$', 'sujet', 's')
text(ax, 72, 40, r'$g=3y+9$', 'autre', 'm')
text(ax, 72, 34, r'$b_1=3$, $b_0=9$', 'autre', 's')
text(ax, 72, 18, 'même racine : $-3$', 'resultat', 's')
save(fig, '70-019')
