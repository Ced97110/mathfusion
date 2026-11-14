import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
s, ox, oy = 6.0, 8, 8
P = lambda x, y: (ox + x * s, oy + y * s)
inK = lambda x, y: any(4 * a + 6 * b == x and 6 * a + 4 * b == y for a in range(-12, 13) for b in range(-12, 13))
nk = ng = 0
for i in range(13):
    for j in range(13):
        if inK(i, j):
            nk += 1; ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['sujet'], ms=4.6, zorder=4)
        else:
            ng += 1; ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.6, zorder=3)
assert (nk, nk + ng) == (10, 169), (nk, ng)
disc(ax, *P(8, 12), 2.4, 'varie', fill=False, lw=1.0)
disc(ax, *P(12, 8), 2.4, 'varie', fill=False, lw=1.0)
text(ax, P(8, 12)[0] - 6, P(8, 12)[1] + 5, r'$2f_1$', 'varie', 's')
text(ax, P(12, 8)[0] - 6, P(12, 8)[1] - 6, r'$2f_2$', 'varie', 's')
text(ax, 84, 84, '10 points de K', 'sujet', 'm', ha='right')
text(ax, 84, 78, 'sur 169 croisements', 'fixe', 's', ha='right')
save(fig, '59-016')
