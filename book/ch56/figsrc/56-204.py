import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'matrice réduite sur $\mathbb{Z}$ (anneau principal)', 'sujet', 's')
x0, y0, c = 22, 14, 16
vals = {0: '2', 1: '12', 2: '60'}
for i in range(3):
    for j in range(3):
        if i == j:
            box(ax, x0 + j * c, y0 + (2 - i) * c, c - 2, c - 2, 'sujet', label=vals[i], size='m')
        else:
            box(ax, x0 + j * c, y0 + (2 - i) * c, c - 2, c - 2, 'fixe', fill=False, dash=True)
text(ax, x0 + 1.5 * c - 1, y0 + 3 * c + 1, 'cases hors diagonale : 0', 'fixe', 's')
text(ax, 79, 46, r'$2\mid12$', 'resultat', 'm')
text(ax, 79, 28, r'$12\mid60$', 'resultat', 'm')
text(ax, 44, 6, 'chaque nombre divise le suivant', 'resultat', 's')
save(fig, '56-204')
