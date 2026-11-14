import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
u, oy = 4.5, 26
line(ax, [(5, oy), (43, oy)], 'fixe', lw=0.8); line(ax, [(48, oy), (86, oy)], 'fixe', lw=0.8)
t = np.linspace(-2.2, 2.2, 80)
line(ax, [(24 + u * a, oy + u * (a * a + 1)) for a in t], 'resultat', lw=1.6)
t = np.linspace(-3.6, 1.6, 80)
line(ax, [(66 + u * a, oy + u * (a * a + 2 * a - 3)) for a in t], 'limite', lw=1.6)
disc(ax, 66, oy - 3 * u, 1.4, 'limite')
text(ax, 85, 4.5, 'x = 0 : valeur −3', 'limite', 's', ha='right'); arrow(ax, (72, 6.5), (67.2, 11.2), 'limite')
text(ax, 24, 64, 'b = 0 et c = 1', 'resultat', 's', weight='bold')
text(ax, 24, 58, r'$b^2-4c=-4<0$', 'resultat', 's')
text(ax, 24, 19, 'toutes les valeurs > 0', 'resultat', 's')
text(ax, 66, 64, 'b = 2 et c = −3', 'limite', 's', weight='bold')
text(ax, 66, 58, r'$b^2-4c=16\geq 0$', 'limite', 's')
save(fig, '70-169')
