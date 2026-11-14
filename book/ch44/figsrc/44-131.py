import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for k, v in enumerate(['5', r'$\frac{1}{2}$', r'$v$']):
    y = 38 - k * 13
    box(ax, 4, y, 24, 9, 'sujet', label=r'0 × ' + v)
    arrow(ax, (30, y + 4.5), (47, 30), 'fixe')
box(ax, 48, 24, 12, 12, 'fixe', label='0', size='l')
text(ax, 54, 41, 'toujours', 'fixe', 's')
box(ax, 72, 24, 12, 12, 'limite', label='1', size='l', dash=True)
arrow(ax, (61, 30), (70.5, 30), 'limite', lw=1.2)
ax.plot([64.5, 67.5], [27.5, 32.5], color=COL['limite'], lw=1.3, zorder=6); ax.plot([64.5, 67.5], [32.5, 27.5], color=COL['limite'], lw=1.3, zorder=6)
text(ax, 78, 41, 'jamais', 'limite', 's')
text(ax, 66, 12, '0 × v = 1 : aucun v', 'limite', 'm')
save(fig, '44-131')
