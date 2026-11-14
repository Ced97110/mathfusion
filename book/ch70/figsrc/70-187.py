import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
u, oy = 9, 24
def panel(ox, c, b, xs, role, roots, rr):
    line(ax, [(ox + xs[0] * u - 2, oy), (ox + xs[1] * u + 2, oy)], 'fixe', lw=0.8)
    line(ax, [(ox, 14), (ox, 42)], 'fixe', lw=0.8)
    t = np.linspace(xs[0], xs[1], 80)
    line(ax, [(ox + u * a, oy + 6 * (a * a + b * a + c)) for a in t], role, lw=1.6)
    for r in roots:
        disc(ax, ox + u * r, oy, 1.3, rr); text(ax, ox + u * r, 19.8, str(r).replace('-', '−'), rr, 's')
panel(12, 2, -3, (-0.2, 3.2), 'sujet', (1, 2), 'resultat')
panel(80, 2, 3, (-3.2, 0.2), 'autre', (-1, -2), 'limite')
text(ax, 26, 55, r'$b=-3,\ c=2$', 'sujet', 's', weight='bold')
text(ax, 66, 55, r'$b=3,\ c=2$', 'autre', 's', weight='bold')
text(ax, 26, 48, 'une racine > 0 : oui', 'resultat', 's')
text(ax, 66, 48, 'une racine > 0 : non', 'limite', 's')
text(ax, 44, 8, r'$b^2-4c=1$ dans les deux cas', 'encre', 's')
save(fig, '70-187')
