import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(56)
def sq(cx, cy, place, role):
    poly(ax, pg(cx, cy, 7, 4, 45), 'fixe')
    x, y = pol(cx, cy, 7, 45 + 90 * (place - 1)); disc(ax, x, y, 2.1, role)
xs = (10, 31, 52, 73)
rowA = ((1, 'sujet'), (4, 'sujet'), (1, 'sujet'), (4, 'resultat'))
for i, (p, r) in enumerate(rowA): sq(xs[i], 40, p, r)
for i, l in enumerate((r'$s$', r'$r$', r'$s$')):
    arrow(ax, (xs[i] + 9.5, 40), (xs[i + 1] - 9.5, 40), 'varie'); text(ax, (xs[i] + xs[i + 1]) / 2, 45, l, 'varie', 'm')
text(ax, 10, 51, 'sommet 1', 'sujet', 's')
text(ax, 73, 30, 'place 4', 'resultat', 's'); text(ax, 31, 51, r'$srs$', 'varie', 'l')
sq(10, 14, 1, 'sujet'); sq(52, 14, 4, 'resultat')
arrow(ax, (19.5, 14), (42.5, 14), 'varie'); text(ax, 31, 19, r'$r^3$', 'varie', 'm')
text(ax, 73, 14, 'place 4', 'resultat', 's')
text(ax, 31, 4, r'$srs = r^{-1} = r^3$', 'resultat', 'm')
save(fig, '44-226')
