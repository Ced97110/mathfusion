import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, u = 44, 33, 10
arrow(ax, (6, oy), (82, oy), 'sujet'); arrow(ax, (ox, 6), (ox, 64), 'autre')
text(ax, 83, oy + 4, r'$x$', 'sujet', 'l'); text(ax, ox + 4, 64, r'$y$', 'autre', 'l')
# right angle square, clear
ax.add_patch(Rectangle((ox, oy), 4.5, 4.5, ec=COL['fixe'], fc=FILL['fixe'], lw=1.0, zorder=3))
text(ax, ox + 14, oy + 11, 'angle droit', 'fixe', 's')
arrow(ax, (ox + 8, oy + 9.5), (ox + 4, oy + 5.2), 'fixe', lw=0.9)
# the shared origin
disc(ax, ox, oy, 1.7, 'encre')
text(ax, ox - 4, oy - 4, r'$O$', 'encre', 'l', weight='bold')
text(ax, ox - 4, oy + 3.5, r'$0$ sur $x$', 'sujet', 's', ha='right')
text(ax, ox + 11, oy - 8, r'$0$ sur $y$', 'autre', 's')
# climb along y
arrow(ax, (ox, oy + 2.2), (ox, oy + u - 1.6), 'varie', lw=1.4)
disc(ax, ox, oy + u, 1.6, 'varie')
text(ax, ox - 3, oy + u + 1, 'monter de 1', 'varie', 's', ha='right')
text(ax, ox - 8, oy - 9, r'$x$ vaut encore 0', 'sujet', 's', ha='right')
save(fig, '19-015')
