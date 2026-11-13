import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 15; ox, oy = 14, 10
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(0, 0), P(4.5, 0), 'fixe', lw=0.7); arrow(ax, P(0, 0), P(0, 2.9), 'fixe', lw=0.7)
for i in range(0, 5):
    for j in range(0, 3):
        disc(ax, *P(i, j), 0.7, 'fixe')
arrow(ax, P(2, 1), P(1, 0.5), 'varie', lw=1.3)
disc(ax, *P(2, 1), 1.3, 'sujet')
disc(ax, *P(1, 0.5), 1.3, 'limite')
text(ax, *P(2.15, 1.35), '(2, 1)', 'sujet', 'm', ha='left')
text(ax, *P(0.9, 0.12), '(1 ; ½) : pas entier', 'limite', 's', ha='left')
text(ax, *P(1.8, 0.45), '× ½', 'varie', 'm')
text(ax, *P(3.5, 2.4), 'points de ℤ²', 'fixe', 's')
save(fig, '57-007')
