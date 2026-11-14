import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, u = 44, 42, 14
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, P(-2.6, 0), P(2.6, 0), 'fixe', lw=0.6); arrow(ax, P(0, -2.6), P(0, 2.6), 'fixe', lw=0.6)
line(ax, [P(-2.3, -2.3), P(2.3, 2.3)], 'limite', lw=1.1); line(ax, [P(-2.3, 2.3), P(2.3, -2.3)], 'limite', lw=1.1)
ts = [i/40*1.5 for i in range(-40, 41)]
for s in (1, -1):
    line(ax, [P(s*math.cosh(t), math.sinh(t)) for t in ts], 'sujet', lw=1.3)
    line(ax, [P(math.sinh(t), s*math.cosh(t)) for t in ts], 'resultat', lw=1.3)
disc(ax, *P(1, 0), 1.1, 'sujet'); disc(ax, *P(1.25, 0.75), 1.1, 'varie')
arrow(ax, P(1.04, 0.2), P(1.2, 0.62), 'varie', lw=0.9)
text(ax, *P(1.0, -0.5), 'P', 'sujet', 'm')
text(ax, *P(1.75, 0.95), r'$\eta P$', 'varie', 'm')
text(ax, *P(2.0, -0.15), r'$x^2-y^2=1$', 'sujet', 's')
text(ax, *P(0, 2.0), r'$x^2-y^2=-1$', 'resultat', 's')
text(ax, *P(2.0, 2.7), r'$x^2-y^2=0$', 'limite', 's')
save(fig, '72-018')
