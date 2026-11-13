import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# left: parabola y = x^2 + 1 above the real axis
ox, oy, sx, sy = 22, 30, 7.0, 3.6
line(ax, [(4, oy), (40, oy)], 'fixe')
pts = [(ox + sx * t / 10, oy + sy * ((t / 10) ** 2 + 1)) for t in range(-20, 21)]
line(ax, pts, 'sujet', lw=1.2)
text(ax, 22, 70, r'$x^2+1$ sur ℝ', 'sujet', 'm')
text(ax, 22, 19, 'aucune racine réelle', 'limite', 's')
text(ax, 22, 24, 'ne touche pas l’axe', 'fixe', 's')
# right: the field built from it
arrow(ax, (42, 45), (50, 45), 'varie')
text(ax, 46, 50, 'on construit', 'varie', 's')
box(ax, 50, 52, 34, 12, 'sujet', label=r'ℝ[$x$]/($x^2+1$)', size='s')
box(ax, 50, 28, 34, 12, 'resultat', label=r'$[x]^2=-1$', size='m')
arrow(ax, (67, 51), (67, 41), 'resultat')
text(ax, 67, 20, r'$[x]$ est racine', 'resultat', 's')
save(fig, '54-273')
