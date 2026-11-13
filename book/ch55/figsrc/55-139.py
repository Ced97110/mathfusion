import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
r2 = math.sqrt(2)
assert abs(r2 * r2 - 2) < 1e-12
# roots of x^2 - 2 on a line, and the swap of the two roots
f = numberline(ax, 12, 76, 44, -2, 2, step=1, arrow_right=False)
disc(ax, f(-r2), 44, 1.6, 'sujet')
disc(ax, f(r2), 44, 1.6, 'sujet')
text(ax, f(-r2), 52.5, r'$-\sqrt{2}$', 'sujet', 'm')
text(ax, f(r2), 52.5, r'$\sqrt{2}$', 'sujet', 'm')
arrow(ax, (f(-r2) + 2, 47), (f(r2) - 2, 47), 'varie', curve=-0.45)
arrow(ax, (f(r2) - 2, 41), (f(-r2) + 2, 41), 'varie', curve=-0.45)
text(ax, 44, 64, r'échange des deux racines de $x^2-2$', 'varie', 's')
box(ax, 3, 10, 40, 14, 'resultat', label=None)
text(ax, 23, 20, 'somme : 0', 'resultat', 'm')
text(ax, 23, 14, 'fixée, dans ℚ', 'resultat', 's')
box(ax, 47, 10, 38, 14, 'fixe', label=None)
text(ax, 66, 20, r'$\sqrt{2}$ devient $-\sqrt{2}$', 'varie', 's')
text(ax, 66, 14, 'pas fixée, hors de ℚ', 'fixe', 's')
save(fig, '55-139')
