import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# plane of complex numbers: roots i and -i of x^2 + 1 (not real); sum 0 and product 1 are real
ox, oy, s = 22, 34, 12
arrow(ax, (ox - 18, oy), (ox + 19, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 20), (ox, oy + 21), 'fixe', lw=0.8)
text(ax, ox + 17, oy - 3.5, r'réels', 'fixe', 's')
disc(ax, ox, oy + s, 1.6, 'sujet'); text(ax, ox + 4, oy + s + 0.5, r'$i$', 'sujet', 'm')
disc(ax, ox, oy - s, 1.6, 'sujet'); text(ax, ox + 5, oy - s - 0.5, r'$-i$', 'sujet', 'm')
disc(ax, ox, oy, 1.6, 'resultat'); text(ax, ox - 3.5, oy - 3, '0', 'resultat', 's')
disc(ax, ox + s, oy, 1.6, 'resultat'); text(ax, ox + s, oy - 3, '1', 'resultat', 's')
text(ax, 22, 63, r'$x^2+1$ : racines hors de $\mathbb{R}$', 'sujet', 's')
# right: the coefficients are symmetric expressions of the roots
box(ax, 48, 42, 38, 10, 'resultat', label=r'somme : $i+(-i)=0$', size='s')
box(ax, 48, 22, 38, 10, 'resultat', label=r'produit : $i\times(-i)=1$', size='s')
arrow(ax, (ox + 4, oy + s - 2), (48, 47), 'varie', curve=-0.2)
arrow(ax, (ox + 5, oy - s + 2), (48, 27), 'varie', curve=0.2)
text(ax, 67, 10, 'ce sont des réels : 0 et 1', 'resultat', 's')
save(fig, '55-138')
