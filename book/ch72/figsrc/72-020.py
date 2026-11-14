import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 44, 40, 14
P = lambda x, y: (ox + x*u, oy + y*u)
arrow(ax, P(-2.6, 0), P(2.6, 0), 'fixe', lw=0.6); arrow(ax, P(0, -2.4), P(0, 2.4), 'fixe', lw=0.6)
ts = [i/40*1.5 for i in range(-40, 41)]
for s in (1, -1): line(ax, [P(s*math.cosh(t), math.sinh(t)) for t in ts], 'sujet', lw=1.4)
line(ax, [P(0.5, -2.2), P(0.5, 2.2)], 'limite', lw=0.9, dash=True)
disc(ax, *P(1, 0), 1.1, 'sujet'); disc(ax, *P(-1, 0), 1.1, 'sujet')
text(ax, *P(1.55, -0.45), 'P = (1, 0)', 'sujet', 's')
text(ax, *P(-1.6, -0.45), '(−1, 0)', 'sujet', 's')
text(ax, *P(0.5, 2.5), r'$x=0{,}5$ : aucun point', 'limite', 's')
text(ax, *P(0, -2.55), r'$x^2-y^2=1$', 'sujet', 's')
save(fig, '72-020')
