import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
sx, sy, y0 = 1.6, 14 / 971, 34
def panel(cx, fn, role):
    arrow(ax, (cx - 20, y0), (cx + 20, y0), 'fixe', lw=0.7)
    xs = np.linspace(-10, 10, 120)
    line(ax, [(cx + sx * x, y0 + sy * fn(x)) for x in xs], role, lw=1.3)
cub = lambda x: x ** 3 - 3 * x + 1
panel(22, cub, 'sujet')
panel(66, lambda x: x ** 2 + 1, 'autre')
text(ax, 22, 60, r'$x^3-3x+1$', 'sujet', 's')
text(ax, 66, 60, r'$x^2+1$', 'autre', 's')
text(ax, 11, y0 - 17, r'$-969$', 'varie', 's')
text(ax, 31, y0 + 17, r'$971$', 'varie', 's')
text(ax, 54, y0 + 4.4, r'$101$', 'varie', 's')
text(ax, 78, y0 + 4.4, r'$101$', 'varie', 's')
disc(ax, 22, y0, 1.4, 'resultat')
text(ax, 22, 8, 'signes opposés', 'resultat', 's')
text(ax, 66, 8, 'même signe', 'limite', 's')
save(fig, '69-043')
