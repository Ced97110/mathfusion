import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
# chaîne de 6 triangles : sommets alternés en haut et en bas
xs = [6 + 12.5 * i for i in range(7)]
top = [(xs[i], 62) if i % 2 else (xs[i], 46) for i in range(7)]
for i in range(5):
    poly(ax, [top[i], top[i + 1], top[i + 2]], 'fixe')
line(ax, [top[0], top[1]], 'sujet', lw=2.0)
line(ax, [top[5], top[6]], 'resultat', lw=2.0)
text(ax, 12, 69, 'base mesurée', 'sujet', 's')
text(ax, 72, 69, 'segment de contrôle', 'resultat', 's')
# deux barres de même longueur : calculé et mesuré
Lg = 56.0
ax.add_patch(Rectangle((16, 28), Lg, 4, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((16, 18), Lg, 4, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, 14, 30, 'calculée', 'varie', 's', ha='right')
text(ax, 14, 20, 'mesurée', 'resultat', 's', ha='right')
text(ax, 44, 9, 'égales aux erreurs près : le réseau tient', 'resultat', 's')
text(ax, 44, 37, 'longueur du segment de contrôle', 'encre', 's')
save(fig, '38-088')
