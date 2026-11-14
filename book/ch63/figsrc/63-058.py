import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ox, oy, s = 36, 40, 22
text(ax, 44, 72, r'$\tau$ = conjugaison complexe', 'encre', 'm')
arrow(ax, (6, oy), (84, oy), 'fixe', lw=0.8)
line(ax, [(ox, 12), (ox, 68)], 'fixe', lw=0.5)
ax.add_patch(Circle((ox, oy), s, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
text(ax, 76, 44, 'axe réel', 'fixe', 's')
rr = 2 ** (1 / 3)
disc(ax, ox + rr * s, oy, 2.2, 'fixe')
text(ax, ox + rr * s, 46, r'$r$ reste', 'fixe', 'm')
jx, jy = ox - 0.5 * s, oy + math.sqrt(3) / 2 * s
disc(ax, jx, jy, 2.2, 'varie')
disc(ax, jx, 2 * oy - jy, 2.2, 'varie')
text(ax, jx - 6, jy + 2, r'$j$', 'varie', 'm')
text(ax, jx - 10, 2 * oy - jy - 2, r'$j^2=\bar{j}$', 'varie', 'm')
arrow(ax, (jx, jy - 3.5), (jx, 2 * oy - jy + 3.5), 'varie', both=True)
text(ax, jx + 4, oy + 8, r'$\tau$', 'varie', 'm')
save(fig, '63-058')
