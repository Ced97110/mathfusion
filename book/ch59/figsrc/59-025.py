import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s, ox, oy = 6.0, 8, 10
P = lambda x, y: (ox + x * s, oy + y * s)
for i in range(13):
    for j in range(5):
        if i % 4 == 0: ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['sujet'], ms=3.4, zorder=3)
        else: ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.4, zorder=2)
arrow(ax, P(0, 0), P(4, 0), 'varie', lw=1.6)
arrow(ax, P(0, 0), P(0, 1), 'varie', lw=1.6)
text(ax, P(2, 0)[0], P(2, 0)[1] + 3.2, r'$(4,\,0)$', 'varie', 's')
text(ax, P(0, 1)[0] + 9, P(0, 1)[1] + 2.5, r'$(0,\,1)$', 'varie', 's')
text(ax, 44, 54, 'première case multiple de 4 : K', 'sujet', 's')
text(ax, 44, 4, r'base de $K$ : 2 éléments, $m=2\leq n=2$', 'encre', 's')
save(fig, '59-025')
