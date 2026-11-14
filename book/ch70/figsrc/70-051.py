import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, ux, uy = 20, 34, 7, 4.5
arrow(ax, (4, oy), (37, oy), 'fixe', lw=0.7)
arrow(ax, (ox, 22), (ox, 50), 'fixe', lw=0.7)
pts = [(ox + t * ux, oy + (t * t - 2) * uy) for t in [i / 10 for i in range(-20, 21)]]
line(ax, pts, 'autre', lw=1.4)
xs = ox + 1.8 * ux
line(ax, [(xs, oy), (xs, oy + (1.8 ** 2 - 2) * uy)], 'varie', lw=1.8)
text(ax, xs, oy - 4, r'$x$', 'fixe', 's')
text(ax, 27, 53, 'hauteur de l’allée\n$s=x^2-2$', 'autre', 's')
steps = [(50, 'sujet', r'$f(x,y)$ : cercle'), (36, 'varie', r'$y$ remplacé par $s$'),
         (22, 'fixe', r'$\times\ b_1^n=1$'), (8, 'resultat', r'$x^4-3x^2$')]
for k, (y, role, s) in enumerate(steps):
    box(ax, 46, y, 40, 8, role, label=s, size='s')
    if k < 3:
        arrow(ax, (66, y), (66, steps[k + 1][0] + 8), 'fixe')
save(fig, '70-051')
