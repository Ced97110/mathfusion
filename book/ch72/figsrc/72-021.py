import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 44, 40, 14
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, P(-2.6, 0), P(2.6, 0), 'fixe', lw=0.6); arrow(ax, P(0, -2.6), P(0, 2.6), 'fixe', lw=0.6)
ts = [i/40*1.5 for i in range(-40, 41)]
for s in (1, -1): line(ax, [P(math.sinh(t), s*math.cosh(t)) for t in ts], 'resultat', lw=1.4)
disc(ax, *P(0, 1), 1.2, 'resultat')
text(ax, *P(0.75, 0.62), '(0, 1)', 'resultat', 'm')
text(ax, *P(-1.55, 0.45), r'$x^2-y^2=-1$', 'resultat', 's')
text(ax, *P(1.0, -0.5), r'$0-1=-1$', 'resultat', 's')
save(fig, '72-021')
