import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, '$5x^2+6x+5=0$', 'sujet', 's'); text(ax, 66, 59, '$x^2+4x+1=0$', 'autre', 's')
text(ax, 22, 53, '$y=1$ fixé', 'varie', 's'); text(ax, 66, 53, '$y=1$ fixé', 'varie', 's')
y0 = 28
def curve(xc, f, xs, xk, yk, role):
    pts = [(xc + x * xk, y0 + f(x) * yk) for x in xs]
    line(ax, pts, role, lw=1.3)
curve(30, lambda x: 5*x*x + 6*x + 5, [-1.5 + 0.03 * i for i in range(61)], 8, 2.0, 'sujet')
line(ax, [(4, y0), (40, y0)], 'fixe', lw=0.8)
text(ax, 22, 8, 'aucune solution', 'limite', 's')
text(ax, 22, 3, '$\\Delta=-64$', 'limite', 's')
curve(77, lambda x: x*x + 4*x + 1, [-4.2 + 0.04 * i for i in range(111)], 6, 2.6, 'autre')
line(ax, [(46, y0), (84, y0)], 'fixe', lw=0.8)
import math
for r in (-2 - math.sqrt(3), -2 + math.sqrt(3)):
    disc(ax, 77 + r * 6, y0, 1.0, 'resultat')
text(ax, 66, 8, 'deux solutions', 'resultat', 's')
text(ax, 66, 3, '$\\Delta=12$', 'resultat', 's')
save(fig, '71-182')
