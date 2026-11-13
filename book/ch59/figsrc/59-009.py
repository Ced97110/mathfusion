import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s, ox, oy = 8.0, 8, 8
P = lambda x, y: (ox + x * s, oy + y * s)
for i in range(8):
    for j in range(8):
        ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.4, zorder=1)
poly(ax, [P(0, 0), P(2, 4), P(6, 6), P(4, 2)], 'fixe')
arrow(ax, P(0, 0), P(2, 4), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(4, 2), 'autre', lw=1.5)
arrow(ax, P(0, 0), P(6, 6), 'varie', lw=1.2)
text(ax, P(2, 4)[0] - 10, P(2, 4)[1] + 2, r'$(2,\,4)$', 'sujet', 's')
text(ax, P(4, 2)[0] + 11, P(4, 2)[1] - 3, r'$(4,\,2)$', 'autre', 's')
text(ax, P(6, 6)[0] + 2, P(6, 6)[1] + 6, r'$(6,\,6)$', 'varie', 's')
text(ax, 70, 20, 'somme des deux', 'varie', 's')
text(ax, 70, 15, 'autres : inutile', 'varie', 's')
text(ax, 70, 9, '2 suffisent', 'encre', 's')
save(fig, '59-009')
