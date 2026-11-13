import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(80)
O, u = (26, 14), 5
text(ax, 44, 75, r'$5^{3}$ : « cinq au cube »', 'sujet', 'l')
text(ax, 44, 68, '5 × 5 × 5 : 3 facteurs', 'varie', 'm')
# cube de côté 5 : 125 petits cubes
cubes(ax, [(i, j, k) for i in range(5) for j in range(5) for k in range(5)], O, u, 'sujet')
# les trois arêtes : longueur, largeur, hauteur
A = iso(5, 0, 0, O, u); B = iso(0, 5, 0, O, u); H = iso(5, 0, 5, O, u)
line(ax, [iso(0, 0, 0, O, u), A], 'varie', lw=1.8)
line(ax, [iso(0, 0, 0, O, u), B], 'varie', lw=1.8)
line(ax, [A, H], 'varie', lw=1.8)
text(ax, 40, 9, 'longueur : 5', 'varie', 's')
text(ax, 12, 9, 'largeur : 5', 'varie', 's')
text(ax, 50, 39, 'hauteur : 5', 'varie', 's', ha='left')
text(ax, 76, 30, '= 125', 'resultat', 'l')
text(ax, 76, 24, 'petits cubes', 'resultat', 's')
save(fig, '04-024')
