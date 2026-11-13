import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
X = lambda x: 10 + x * 6
Y = lambda y: 8 + y * 6
for i in range(0, 6):
    for j in range(0, 8):
        disc(ax, X(i), Y(j), 0.5, 'fixe')
p, q = (X(1), Y(2)), (X(4), Y(6))
line(ax, [p, q], 'sujet', lw=1.6)
disc(ax, *p, 1.5, 'fixe'); disc(ax, *q, 1.5, 'autre')
text(ax, p[0] + 3, p[1] - 3.5, r'$P\ (1\ ;\ 2)$', 'fixe', 's', ha='left')
text(ax, q[0] - 3, q[1] + 3.5, r'$Q\ (4\ ;\ 6)$', 'autre', 's', ha='right')
text(ax, 21, 35, '5', 'sujet', 'l')
text(ax, 62, 48, r'$d(P,\ Q)=5$', 'sujet', 'l', ha='left')
text(ax, 62, 38, 'd : la distance', 'sujet', 's', ha='left')
text(ax, 62, 34.5, 'entre deux points', 'sujet', 's', ha='left')
text(ax, 62, 25, 'P, Q : les deux', 'fixe', 's', ha='left')
text(ax, 62, 21.5, 'points', 'fixe', 's', ha='left')
text(ax, 62, 12, '5 : un nombre', 'sujet', 's', ha='left')
save(fig, '74-087')
