import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
s, ox, oy = 7.0, 22, 20
for i in range(-3, 4):
    for j in range(0, 6):
        if (i, j) == (0, 0): continue
        ax.plot([ox + 3 * s + i * s], [oy + j * s], '.', color=COL['fixe'], ms=2.4, zorder=1)
disc(ax, ox + 3 * s, oy, 2.0, 'sujet')
text(ax, ox + 3 * s, oy - 6, r'$(0,\,0)$', 'sujet', 's')
text(ax, 44, 71, r'$K=\{0\}$ : un seul point', 'sujet', 'm')
text(ax, 44, 5, r'base vide : $m=0\leq n$', 'varie', 's')
save(fig, '59-030')
