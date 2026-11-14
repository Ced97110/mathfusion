import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(80)
X = lambda x: 8 + (x + 3) * 9
Y = lambda v: 46 + v * 3
line(ax, [(4, 46), (78, 46)], 'fixe', lw=0.8)
a = np.linspace(-3, 1.5, 90); b = np.linspace(-1.8, 3.8, 90)
line(ax, [(X(x), Y(x * x + 2 * x + 2)) for x in a], 'sujet', lw=1.6)
line(ax, [(X(x), Y((x - 1) ** 2)) for x in b], 'autre', lw=1.6)
disc(ax, X(-1), Y(1), 1.3, 'sujet'); disc(ax, X(1), Y(0), 1.3, 'autre')
text(ax, 16, 72, r'$x^2+2x+2$', 'sujet', 's'); text(ax, 78, 60, r'$(x-1)^2$', 'autre', 's')
text(ax, 44, 40, 'jamais sous l’axe', 'resultat', 's')
box(ax, 4, 22, 26, 10, 'sujet', label=r'$(x+1)^2$', size='s'); text(ax, 35, 27, '+', 'encre', 'm')
box(ax, 40, 22, 16, 10, 'sujet', label=r'$1^2$', size='s'); text(ax, 72, 27, 'deux carrés', 'sujet', 's')
box(ax, 4, 6, 26, 10, 'autre', label=r'$(x-1)^2$', size='s'); text(ax, 35, 11, 'un seul carré', 'autre', 's', ha='left')
save(fig, '70-184')
