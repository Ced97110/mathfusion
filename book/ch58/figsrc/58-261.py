import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 23, 34, 6.2
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, P(-3, 0), P(3, 0), 'sujet', lw=1.2)
arrow(ax, P(0, -3), P(0, 3), 'autre', lw=1.2)
arrow(ax, P(-3, -3), P(3, 3), 'varie', lw=1.2)
text(ax, P(3, 0)[0] - 1, P(3, 0)[1] - 3.5, 'X', 'sujet', 's', weight='bold')
text(ax, P(0, 3)[0] + 3.5, P(0, 3)[1], 'Y', 'autre', 's', weight='bold')
text(ax, P(3, 3)[0] - 3, P(3, 3)[1] + 2, 'Z', 'varie', 's', weight='bold')
disc(ax, ox, oy, 1.5, 'resultat')
for i, s in enumerate([r'$\checkmark\ X\cap Y=\{O\}$', r'$\checkmark\ X\cap Z=\{O\}$', r'$\checkmark\ Y\cap Z=\{O\}$']):
    text(ax, 50, 54 - i * 8, s, 'resultat', 's', ha='left')
box(ax, 48, 12, 38, 12, 'limite', label='pourtant pas indépendantes', size='s')
arrow(ax, (67, 31), (67, 25.5), 'limite', lw=1.2)
text(ax, 23, 6, 'deux à deux : seulement O', 'fixe', 's')
save(fig, '58-261')
