import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
f = numberline(ax, 5, 39, 34, -2, 2, step=1, labels=False, arrow_right=False)
for v, l in [(-math.sqrt(2), r'$-\sqrt{2}$'), (math.sqrt(2), r'$\sqrt{2}$')]:
    disc(ax, f(v), 34, 2, 'resultat')
    text(ax, f(v), 41, l, 'resultat', 's')
text(ax, 22, 62, r'$x^2-2$', 'sujet', 'm')
text(ax, 22, 22, '2 racines distinctes', 'resultat', 's')
text(ax, 22, 14, r"PGCD$(f,f')=1$", 'resultat', 's')
g = numberline(ax, 49, 83, 34, -1, 3, step=1, labels=False, arrow_right=False)
disc(ax, g(1), 34, 3.2, 'limite', fill=False)
disc(ax, g(1), 34, 1.8, 'limite')
text(ax, g(1), 41, '1', 'limite', 's')
text(ax, 66, 62, r'$(x-1)^2$', 'sujet', 'm')
text(ax, 66, 22, '1 racine, comptée 2 fois', 'limite', 's')
text(ax, 66, 14, r'PGCD $=x-1$', 'limite', 's')
save(fig, '63-111')
