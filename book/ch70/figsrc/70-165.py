import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(72)
O, u = (26, 38), 10
X = lambda a, b: (O[0] + a * u, O[1] + b * u)
line(ax, [X(-2, 0), X(5, 0)], 'fixe', lw=0.5)
t = np.linspace(-2.19, 2.19, 100)
line(ax, [X(a * a, a) for a in t], 'sujet', lw=1.6)
text(ax, 76, 55, r'$y^2=x$', 'sujet', 'm')
for xv, lab, yl in ((-1, '0 point', 58), (0, '1 point', 64), (4, '2 points', 66)):
    px = X(xv, 0)[0]
    line(ax, [(px, 8), (px, yl - 3)], 'fixe', dash=True)
    text(ax, px, yl, lab, 'encre', 's')
disc(ax, *X(4, 2), 1.3, 'sujet'); disc(ax, *X(4, -2), 1.3, 'sujet'); disc(ax, *X(0, 0), 1.3, 'sujet')
# projection line below
line(ax, [(4, 8), (X(0, 0)[0], 8)], 'limite', lw=2.6)
line(ax, [(X(0, 0)[0], 8), (79, 8)], 'resultat', lw=2.6)
arrow(ax, (79, 8), (84, 8), 'resultat', lw=1.2)
for xv, lab in ((-1, '−1'), (0, '0'), (4, '4')):
    text(ax, X(xv, 0)[0], 4.2, lab, 'fixe', 's')
text(ax, 52, 12.8, 'x ≥ 0 : un y existe', 'resultat', 's')
text(ax, 15, 12.8, 'x < 0 : aucun y', 'limite', 's')
save(fig, '70-165')
