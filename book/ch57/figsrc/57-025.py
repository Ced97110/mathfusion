import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 15; ox, oy = 12, 10
P = lambda x, y: (ox + x * u, oy + y * u)
for i in range(0, 5): line(ax, [P(i, 0), P(i, 2.4)], 'fixe', lw=0.2)
for j in range(0, 3): line(ax, [P(0, j), P(4.4, j)], 'fixe', lw=0.2)
arrow(ax, P(0, 0), P(4.7, 0), 'fixe', lw=0.7); arrow(ax, P(0, 0), P(0, 2.8), 'fixe', lw=0.7)
for (x, y) in [(2, 1), (4, 2)]:
    line(ax, [P(x, y), P(x, 0)], 'fixe', lw=0.8, dash=True); line(ax, [P(x, y), P(0, y)], 'fixe', lw=0.8, dash=True)
arrow(ax, P(0, 0), P(4, 2), 'varie', lw=1.6)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=2.0)
disc(ax, *P(4, 2), 1.1, 'varie')
for v, y in [(2, 1), (4, 2)]:
    text(ax, *P(v, -0.3), str(v), 'fixe', 's')
    text(ax, *P(-0.3, y), str(y), 'fixe', 's')
text(ax, *P(2.45, 0.6), 'v', 'sujet', 'm', weight='bold')
text(ax, *P(4.15, 2.3), '2v', 'varie', 'm', ha='left', weight='bold')
text(ax, 52, 51, '2 × (2, 1) = (4, 2)', 'varie', 'm')
save(fig, '57-025')
