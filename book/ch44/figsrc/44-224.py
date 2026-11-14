import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(52)
cx, cy, R = 26, 27, 11
poly(ax, pg(cx, cy, R, 4, 45), 'sujet')
for k in range(4):
    x, y = pol(cx, cy, 7, 45 + 90 * k); text(ax, x, y, str(k + 1), 'sujet', 's')
    arrow(ax, pol(cx, cy, R + 4.5, 45 + 90 * k + 17), pol(cx, cy, R + 4.5, 45 + 90 * k + 73), 'varie', curve=0.3)
    x, y = pol(cx, cy, R + 10, 90 * k + 90); text(ax, x, y, r'$r$', 'varie', 's')
text(ax, 66, 40, '4 × 90°', 'varie', 'l'); text(ax, 66, 32, '= 360°', 'resultat', 'l')
text(ax, 66, 24, 'un tour complet', 'resultat', 's')
box(ax, 52, 6, 28, 11, 'resultat', label=r'$r^4 = 1$', size='l')
arrow(ax, (66, 21), (66, 18), 'resultat')
save(fig, '44-224')
