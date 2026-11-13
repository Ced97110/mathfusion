import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 12; ox, oy = 50, 10
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(-3, 3): line(ax, [P(i, -0.5), P(i, 3)], 'fixe', lw=0.2)
for j in range(0, 4): line(ax, [P(-3, j), P(2, j)], 'fixe', lw=0.2)
arrow(ax, P(-3, 0), P(2.4, 0), 'fixe', lw=0.7); arrow(ax, P(0, -0.5), P(0, 3.4), 'fixe', lw=0.7)
line(ax, [P(0, 0), P(-1, 0)], 'varie', lw=1.5, dash=True); line(ax, [P(-1, 0), P(-1, 2)], 'varie', lw=1.5, dash=True)
arrow(ax, P(0, 0), P(-1, 2), 'autre', lw=2.0)
text(ax, *P(-0.85, 2.4), 'w = (−1, 2)', 'autre', 'm', ha='left', weight='bold')
text(ax, *P(-0.5, -0.4), '1 à gauche : −', 'varie', 's')
text(ax, *P(-1.15, 1), '2 en haut : +', 'varie', 's', ha='right')
save(fig, '57-024')
