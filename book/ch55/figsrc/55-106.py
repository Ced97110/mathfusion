import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ox, oy, ux, uy = 24, 16, 13.0, 7.5
X = lambda x: ox + x * ux
Y = lambda y: oy + y * uy
arrow(ax, (ox - 3, oy), (X(4.4), oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 4), (ox, Y(6) + 8), 'fixe', lw=0.9)
xs = [i * 4.2 / 60 for i in range(61)]
line(ax, [(X(x), Y(x * x - 5 * x + 6)) for x in xs], 'sujet', lw=1.3)
# produit = hauteur en x = 0 (vert, le long de l'axe vertical)
line(ax, [(ox, oy), (ox, Y(6))], 'resultat', lw=2.4)
disc(ax, X(0), Y(6), 1.8, 'resultat')
text(ax, ox - 2.5, Y(3), r'produit $=6$', 'resultat', 's', ha='right')
text(ax, X(0) + 3.5, Y(6) + 1, 'hauteur en $x=0$', 'resultat', 's', ha='left')
# somme = double de la position de l'axe de symétrie (orange)
line(ax, [(X(2.5), oy - 3), (X(2.5), Y(3.6))], 'varie', lw=1.0, dash=True)
text(ax, X(2.5), Y(3.6) + 6, 'axe de symétrie : 2,5\nsomme $=2\\times 2{,}5=5$', 'varie', 's')
# racines
for r in (2, 3):
    disc(ax, X(r), oy, 1.8, 'sujet')
    text(ax, X(r), oy - 5, rf'$r_{r - 1}={r}$', 'sujet', 's')
text(ax, X(4.2) - 2, Y(2.7) + 6, r'$x^2-5x+6$', 'sujet', 's')
save(fig, '55-106')
