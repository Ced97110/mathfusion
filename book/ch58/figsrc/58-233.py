import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
U = 10
P1 = lambda x, y: (8 + U * x, 8 + U * y)
P2 = lambda x, y: (50 + U * x, 8 + U * y)
poly(ax, [P1(0, 0), P1(2, 1), P1(3, 2), P1(1, 1)], 'varie')
poly(ax, [P2(0, 0), P2(1, 2), P2(3, 3), P2(2, 1)], 'autre')
for i in range(4):
    for j in range(4):
        disc(ax, *P1(i, j), 0.5, 'fixe') if j < 3 else None
        disc(ax, *P2(i, j), 0.5, 'fixe')
arrow(ax, P1(0, 0), P1(2, 1), 'varie', lw=1.2)
arrow(ax, P1(0, 0), P1(1, 1), 'varie', lw=1.2)
arrow(ax, P2(0, 0), P2(1, 2), 'autre', lw=1.2)
arrow(ax, P2(0, 0), P2(2, 1), 'autre', lw=1.2)
text(ax, 33, 14, '$(2,1)$', 'varie', 's', ha='left')
text(ax, 17, 22, '$(1,1)$', 'varie', 's', ha='right')
text(ax, 58, 30, '$(1,2)$', 'autre', 's', ha='right')
text(ax, 76, 13, '$(2,1)$', 'autre', 's', ha='left')
text(ax, 23, 50, r'$2\times1-1\times1=1$', 'varie', 's')
text(ax, 23, 44, r'aire $|1|=1$', 'varie', 'm', weight='bold')
text(ax, 65, 50, r'$1\times1-2\times2=-3$', 'autre', 's')
text(ax, 65, 44, r'aire $|-3|=3$', 'autre', 'm', weight='bold')
save(fig, '58-233')
