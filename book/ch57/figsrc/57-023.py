import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 14; ox, oy = 30, 14
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(-1, 4): line(ax, [P(i, -0.5), P(i, 2.3)], 'fixe', lw=0.2)
for j in range(0, 3): line(ax, [P(-1, j), P(3, j)], 'fixe', lw=0.2)
arrow(ax, P(-1, 0), P(3.4, 0), 'fixe', lw=0.7); arrow(ax, P(0, -0.5), P(0, 2.5), 'fixe', lw=0.7)
line(ax, [P(0, 0), P(2, 0)], 'varie', lw=1.5, dash=True); line(ax, [P(2, 0), P(2, 1)], 'varie', lw=1.5, dash=True)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=2.0)
text(ax, *P(0.75, 0.95), 'v = (2, 1)', 'sujet', 'm', weight='bold')
text(ax, *P(1, -0.3), '2 à droite', 'varie', 's')
text(ax, *P(2.1, 0.5), '1 en haut', 'varie', 's', ha='left')
save(fig, '57-023')
