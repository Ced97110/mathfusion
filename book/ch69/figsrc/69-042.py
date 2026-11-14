import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(64)
sx, sy, y0 = 7.5, 2.4, 30
def panel(cx, fn, role):
    arrow(ax, (cx - 19, y0), (cx + 19, y0), 'fixe', lw=0.7)
    xs = np.linspace(-2.3, 2.3, 80)
    pts = [(cx + sx * x, y0 + sy * fn(x)) for x in xs if -9.6 < sy * fn(x) < 22]
    line(ax, pts, role, lw=1.3)
cub = lambda x: x ** 3 - 3 * x + 1
panel(22, cub, 'sujet')
panel(66, lambda x: x ** 2 + 1, 'autre')
for r in np.roots([1, 0, -3, 1]):
    disc(ax, 22 + sx * r.real, y0, 1.5, 'resultat')
text(ax, 22, 58, r'degré 3 (impair) : $x^3-3x+1$', 'sujet', 's')
text(ax, 66, 58, r'degré 2 (pair) : $x^2+1$', 'autre', 's')
text(ax, 22, 8, 'impair : au moins une racine', 'resultat', 's')
text(ax, 66, 8, 'pair : peut n’en avoir aucune', 'limite', 's')
save(fig, '69-042')
