import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 3, 4, 42, 48, 'sujet', fill=False, dash=True)
import math
for k, ang in enumerate([20, 55, 95, 140, 200, 250, 310]):
    r = 12 + (k % 3) * 3
    a = math.radians(ang)
    arrow(ax, (24, 28), (24 + r*math.cos(a), 28 + r*math.sin(a)), 'sujet', lw=1.0)
text(ax, 10, 46, r'$V$', 'sujet', 'xl', weight='bold')
text(ax, 24, 8, 'toutes les flèches', 'sujet', 's')
arrow(ax, (52, 36), (64, 36), 'sujet'); arrow(ax, (52, 36), (56, 48), 'autre'); arrow(ax, (52, 36), (68, 48), 'resultat')
line(ax, [(64, 36), (68, 48)], 'fixe', dash=True); line(ax, [(56, 48), (68, 48)], 'fixe', dash=True)
text(ax, 65, 32, r'$x$', 'sujet', 's'); text(ax, 52, 48, r'$y$', 'autre', 's'); text(ax, 76, 50, r'$x+y$', 'resultat', 's')
arrow(ax, (52, 14), (62, 14), 'sujet'); arrow(ax, (52, 8), (72, 8), 'varie')
text(ax, 62, 17.5, r'$x$', 'sujet', 's'); text(ax, 80, 8, r'$2x$', 'varie', 's')
save(fig, '75-047')
