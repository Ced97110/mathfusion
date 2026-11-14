import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 9, 33, 22
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, P(-0.2, 0), P(2.0, 0), 'fixe', lw=0.6); arrow(ax, P(0, -1.3), P(0, 1.4), 'fixe', lw=0.6)
ts = [i/40*1.2 for i in range(-40, 41)]
line(ax, [P(math.cosh(t), math.sinh(t)) for t in ts], 'sujet', lw=1.4)
line(ax, [P(1.25, 0), P(1.25, 0.75)], 'fixe', lw=0.8, dash=True); line(ax, [P(0, 0.75), P(1.25, 0.75)], 'fixe', lw=0.8, dash=True)
disc(ax, *P(1, 0), 1.1, 'sujet'); disc(ax, *P(1.25, 0.75), 1.2, 'varie')
text(ax, *P(0.82, -0.22), 'P', 'sujet', 's')
text(ax, *P(1.55, 0.95), r'$\eta P$', 'varie', 'm')
text(ax, *P(1.25, -0.22), r'$5/4$', 'fixe', 's')
text(ax, *P(-0.22, 0.75), r'$3/4$', 'fixe', 's')
text(ax, 72, 54, r'$(5/4)^2=25/16$', 'varie', 's')
text(ax, 72, 44, r'$(3/4)^2=9/16$', 'varie', 's')
text(ax, 72, 33, r'$25/16-9/16$', 'sujet', 's')
text(ax, 72, 25, r'$=16/16=1$', 'resultat', 'm')
save(fig, '72-022')
