import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
O, u = (24, 22), 10
X = lambda a, b: (O[0] + a * u, O[1] + b * u)
line(ax, [X(-2.3, 0), X(2.3, 0)], 'fixe', lw=0.6); line(ax, [X(0, -2.2), X(0, 3.7)], 'fixe', lw=0.6)
for r, role in ((0.5, 'fixe'), (1, 'resultat'), (2, 'varie')):
    ax.add_patch(Circle(O, r * u, fill=False, ec=COL[role], lw=1.2, zorder=3))
t = np.linspace(-1.6, 1.6, 80)
line(ax, [X(a, a * a + 1) for a in t], 'sujet', lw=1.5)
disc(ax, *X(0, 1), 1.2, 'resultat')
text(ax, 20.5, 19.5, 'O', 'encre', 's')
# legend
rows = [(56, 'sujet', 'courbe : y = x² + 1'), (42, 'fixe', 'rayon 0,5 : aucun contact'),
        (32, 'resultat', 'rayon 1 : touche en (0 ; 1)'), (22, 'varie', 'rayon 2 : coupe la courbe')]
for y, role, s in rows:
    line(ax, [(47, y), (50, y)], role, lw=1.6)
    text(ax, 51.5, y, s, role, 's', ha='left')
text(ax, 66, 9, 'plus petit rayon : 1', 'resultat', 's', weight='bold')
save(fig, '70-153')
