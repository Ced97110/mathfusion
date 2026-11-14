import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 14, 36, 17
arrow(ax, (ox - 8, oy), (ox + 66, oy), 'fixe', lw=0.8)
ax.plot([ox, ox], [oy - 16, oy + 16], color=COL['fixe'], lw=0.9, ls='--', zorder=3)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.8)
arrow(ax, (ox + u, oy + 3), (ox + 2 * u, oy + 3), 'varie', lw=1.8)
text(ax, ox + u / 2, oy - 4.5, r'$z=(1,0)$', 'sujet', 's')
text(ax, ox + 1.5 * u, oy + 8, r'$\lambda z=2z=(2,0)$', 'varie', 's')
text(ax, ox + 4, oy + 14, 'cette direction : non atteinte', 'fixe', 's', ha='left')
box(ax, 14, 6, 60, 10, 'limite', label=r'$z$ et $\lambda z$ : une seule droite, pas une base', size='s')
save(fig, '60-162')
