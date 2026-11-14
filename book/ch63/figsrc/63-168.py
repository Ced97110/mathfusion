import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# parabole y = x^2 + x - 1, x de -2 à 1,1 ; unités : 22 mm en x, 14 mm en y
X0, Y0, ux, uy = 56, 40, 21, 14
fx = lambda v: X0 + ux * v
fy = lambda v: Y0 + uy * v
arrow(ax, (fx(-2.2), Y0), (fx(1.25), Y0), 'fixe', lw=0.7)
line(ax, [(X0, fy(-1.4)), (X0, fy(1.4))], 'fixe', lw=0.7)
xs = [-2 + 0.03 * i for i in range(0, 104)]
line(ax, [(fx(v), fy(v * v + v - 1)) for v in xs], 'sujet', lw=1.2)
r = (-1 + math.sqrt(5)) / 2; t = (-1 - math.sqrt(5)) / 2
disc(ax, fx(r), Y0, 1.5, 'sujet'); disc(ax, fx(t), Y0, 1.5, 'autre')
text(ax, fx(r) + 1, Y0 + 5, r'$s$', 'sujet', 'l')
text(ax, fx(t) - 1, Y0 + 5, r'$t$', 'autre', 'l')
text(ax, fx(r), Y0 - 5, r'$(-1+\sqrt{5})/2$', 'sujet', 's')
text(ax, fx(t), Y0 - 5, r'$(-1-\sqrt{5})/2$', 'autre', 's')
# axe de symétrie : milieu = -1/2, somme = -1
line(ax, [(fx(-0.5), fy(-1.25)), (fx(-0.5), fy(1.1))], 'resultat', dash=True)
text(ax, fx(-0.5) - 1.5, fy(1.1) + 3, r'$s + t = -1$', 'resultat', 'm', ha='right')
# produit : ordonnée à l'origine
disc(ax, X0, fy(-1), 1.4, 'varie')
text(ax, X0 + 2.5, fy(-1) - 4, r'$s \times t = -1$', 'varie', 'm', ha='left')
text(ax, 44, 62, r'$s$ et $t$ sont les racines de $x^2 + x - 1$', 'encre', 'm')
save(fig, '63-168')
