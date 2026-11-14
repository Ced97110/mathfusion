import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
oy = 34
line(ax, [(4, oy), (42, oy)], 'fixe', lw=0.8); line(ax, [(46, oy), (84, oy)], 'fixe', lw=0.8)
t = np.linspace(-1, 1, 80)
line(ax, [(23 + 18 * a, oy + 5 * (4 * a * a - 1)) for a in t], 'sujet', lw=1.6)
line(ax, [(65 + 18 * a, oy + 5 * (-4 * a * a - 1)) for a in t], 'autre', lw=1.6)
disc(ax, 23 - 9, oy, 1.4, 'resultat'); disc(ax, 23 + 9, oy, 1.4, 'resultat')
text(ax, 23, 58, 'H = 4', 'sujet', 's', weight='bold')
text(ax, 65, 58, 'H = −4', 'autre', 's', weight='bold')
text(ax, 23, 44, r'$4z^2-1$', 'sujet', 's')
text(ax, 65, 17, r'$-4z^2-1$', 'autre', 's')
text(ax, 23, 20, 'z = 1/2 ou z = −1/2', 'resultat', 's')
text(ax, 65, 41, 'jamais égale à 0', 'limite', 's')
text(ax, 44, 36.5, 'z', 'fixe', 's')
save(fig, '70-174')
