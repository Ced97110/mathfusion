import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 20, 65, r'$\mathbb{R}[x]/(x^2+1)$', 'sujet', 'm')
text(ax, 68, 65, r'$\mathbb{C}$', 'autre', 'm')
text(ax, 20, 60, r'ici $x^2=-1$', 'sujet', 's')
text(ax, 68, 60, r'ici $i^2=-1$', 'autre', 's')
rows = [(46, r'$2+x$', r'$2+i$'),
        (33, r'$3+x$', r'$3+i$'),
        (14, r'$x^2+5x+6\equiv 5+5x$', r'$5+5i$')]
for i, (y, a, b) in enumerate(rows):
    w = 38 if i == 2 else 20
    box(ax, 2, y, w, 9, 'sujet', label=a, size='s')
    box(ax, 56 if i < 2 else 56, y, 28 if i < 2 else 28, 9, 'autre', label=b, size='s')
    text(ax, 49 if i == 2 else 44, y + 4.5, '↔', 'encre', 'l')
text(ax, 44, 7, 'les deux produits : même résultat', 'resultat', 's')
text(ax, 44, 27, 'produit des deux lignes :', 'fixe', 's')
save(fig, '57-197')
