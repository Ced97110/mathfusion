import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(92)
box(ax, 1, 6, 86, 74, 'fixe', fill=False, dash=True)
text(ax, 44, 88, 'G : de 0 à 11, addition modulo 12', 'fixe', 's')
ax.add_patch(Circle((30, 44), 24, fc=FILL['sujet'], ec=COL['sujet'], lw=0.9, alpha=0.7, zorder=1))
ax.add_patch(Circle((58, 44), 24, fc=FILL['autre'], ec=COL['autre'], lw=0.9, alpha=0.7, zorder=1))
for s, p in [('3', (15, 50)), ('9', (15, 38))]: text(ax, *p, s, 'sujet', 'm')
for s, p in [('2', (65, 54)), ('4', (74, 46)), ('8', (65, 34)), ('10', (74, 38))]: text(ax, *p, s, 'autre', 'm')
for s, p in [('0', (44, 52)), ('6', (44, 36))]: text(ax, *p, s, 'resultat', 'l', weight='bold')
text(ax, 22, 74, 'multiples de 3', 'sujet', 's'); text(ax, 66, 74, 'nombres pairs', 'autre', 's')
text(ax, 44, 12, 'inf = intersection = {0, 6}', 'resultat', 's')
save(fig, '79-074')
