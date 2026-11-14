import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# trois colonnes : u, v, w ; scalaires -1, 2, -1 ; produits ; somme
cols = [('sujet', '(3, 1)', r'$\times\,(-1)$', '(−3, −1)'),
        ('varie', '(1, 2)', r'$\times\,2$', '(2, 4)'),
        ('autre', '(−1, 3)', r'$\times\,(-1)$', '(1, −3)')]
xs = [6, 32, 58]
for x, (role, vec, sc, prod) in zip(xs, cols):
    box(ax, x, 62, 24, 9, role, label=vec)
    arrow(ax, (x + 12, 61), (x + 12, 55), role)
    text(ax, x + 12, 51.5, sc, role, 'm')
    arrow(ax, (x + 12, 47), (x + 12, 41), role)
    box(ax, x, 31, 24, 9, role, label=prod)
text(ax, 44, 75, 'trois vecteurs', 'fixe', 's')
text(ax, 44, 21.5, r'$-3+2+1=0$  et  $-1+4-3=0$', 'resultat', 's')
# somme
line(ax, [(6, 27), (82, 27)], 'fixe')
box(ax, 26, 6, 36, 10, 'resultat', label='somme : (0, 0)', weight='bold')
save(fig, '58-153')
