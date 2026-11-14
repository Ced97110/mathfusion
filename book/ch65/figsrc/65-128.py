import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(74)
y0 = 38
sx, sy = 8.0, 4.0
def panel(cx, f, xr, role, ymin, ymax):
    arrow(ax, (cx - 18.5, y0), (cx + 18.5, y0), 'fixe', lw=0.7)
    xs = np.linspace(-xr, xr, 120)
    pts = [(cx + x * sx, y0 + f(x) * sy) for x in xs if ymin <= f(x) <= ymax]
    line(ax, pts, role, lw=1.4)
# gauche : x^2 + 1
panel(22, lambda x: x * x + 1, 2.1, 'sujet', -3, 5)
text(ax, 22, 66, r'$x^2+1=0$', 'sujet', 'm')
text(ax, 22, 20, 'aucune racine réelle', 'limite', 's')
text(ax, 22, 12, 'on dit : pas de solution', 'encre', 's')
# droite : x^3 - 3x + 1
panel(66, lambda x: x ** 3 - 3 * x + 1, 2.1, 'sujet', -3, 5)
roots = sorted(r.real for r in np.roots([1, 0, -3, 1]))
for r in roots:
    disc(ax, 66 + r * sx, y0, 1.4, 'resultat')
text(ax, 66, 66, r'$x^3-3x+1=0$', 'sujet', 'm')
text(ax, 66, 20, 'trois racines réelles', 'resultat', 's')
text(ax, 66, 12, r'formule : passe par $\sqrt{-1}$', 'varie', 's')
line(ax, [(44, 8), (44, 62)], 'fixe', lw=0.5, dash=True)
save(fig, '65-128')
