import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(76)
u, oy = 5, 26
def panel(ox, c, xs, role):
    line(ax, [(ox - 20, oy), (ox + 18, oy)], 'fixe', lw=0.8)
    t = np.linspace(xs[0], xs[1], 80)
    line(ax, [(ox + u * a, oy + u * (a * a + 2 * a + c)) for a in t], role, lw=1.5)
panel(26, -3, (-3.6, 1.6), 'sujet')
panel(68, 5, (-2.6, 0.6), 'autre')
disc(ax, 26 + 5, oy, 1.3, 'resultat'); disc(ax, 26 - 15, oy, 1.3, 'resultat')
text(ax, 33.5, 22, '1', 'resultat', 's'); text(ax, 8.5, 22, '−3', 'resultat', 's')
text(ax, 26, 72, 'b = 2 et c = −3', 'sujet', 's', weight='bold')
text(ax, 26, 66, r'$b^2-4c=16\geq 0$', 'sujet', 's')
text(ax, 26, 60, 'racines : 1 et −3', 'resultat', 's')
text(ax, 68, 72, 'b = 2 et c = 5', 'autre', 's', weight='bold')
text(ax, 68, 66, r'$b^2-4c=-16<0$', 'autre', 's')
text(ax, 68, 35, 'aucune racine réelle', 'limite', 's')
save(fig, '70-168')
