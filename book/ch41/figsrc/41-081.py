import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, s = 12, 14, 15
P = lambda x, y: (ox + s * x, oy + s * y)
O, U, V = P(0, 0), P(1, 3), P(4, 2)
arrow(ax, V, O, 'autre', lw=1.4)
arrow(ax, O, U, 'sujet', lw=1.6)
arrow(ax, V, U, 'varie', lw=1.8)
for p, c in ((O, 'encre'), (U, 'sujet'), (V, 'autre')):
    ax.plot([p[0]], [p[1]], marker='o', ms=3, color=COL[c], zorder=6)
text(ax, O[0] - 3, O[1] - 2.5, r'$O$', 'encre', 'm')
text(ax, U[0] - 3, U[1] + 2, r'$U$', 'sujet', 'm')
text(ax, V[0] + 3.5, V[1] + 1, r'$V$', 'autre', 'm')
text(ax, 18, 40, r'$u$', 'sujet', 'm')
text(ax, 46, 18, r'$-v$ (retour)', 'autre', 's')
text(ax, 57, 56, r'$u-v$', 'varie', 'm')
text(ax, 44, 4, r'$\langle1-4,\ 3-2\rangle=\langle-3,1\rangle$', 'varie', 's')
save(fig, '41-081')
