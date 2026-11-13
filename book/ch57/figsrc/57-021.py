import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 10; ox, oy = 40, 16
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-3.4, 0), P(3.6, 0), 'fixe', lw=1.0); arrow(ax, P(0, -1.2), P(0, 3.6), 'fixe', lw=1.0)
for i in range(-3, 4):
    if i: line(ax, [P(i, -0.12), P(i, 0.12)], 'fixe', lw=0.8)
for j in range(-1, 4):
    if j: line(ax, [P(-0.12, j), P(0.12, j)], 'fixe', lw=0.8)
line(ax, [P(0, 0), P(2, 0)], 'varie', lw=1.8); line(ax, [P(2, 0), P(2, 1)], 'varie', lw=1.8)
disc(ax, *P(2, 1), 1.1, 'varie')
disc(ax, *P(0, 0), 1.7, 'sujet')
text(ax, *P(-0.5, -0.5), 'O', 'sujet', 'l', weight='bold')
text(ax, *P(-0.45, 0.5), '(0 ; 0)', 'sujet', 's', ha='right')
text(ax, *P(1, -0.55), '2 pas', 'varie', 's')
text(ax, *P(1.85, 0.5), '1 pas', 'varie', 's', ha='right')
text(ax, *P(2, 1.5), '(2, 1)', 'varie', 'm')
text(ax, *P(3.5, -0.6), 'axe horizontal', 'fixe', 's', ha='right')
text(ax, *P(0.2, 3.4), 'axe vertical', 'fixe', 's', ha='left')
save(fig, '57-021')
