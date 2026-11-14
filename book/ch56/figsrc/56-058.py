import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# ligne 1 : racine de -5, normes différentes
text(ax, 44, 88, r'dans $\mathbb{Z}[\sqrt{-5}]$', 'encre', 'm')
box(ax, 4, 66, 28, 14, 'sujet', label='2 : norme 4', size='s')
text(ax, 44, 73, '≠', 'resultat', 'l')
box(ax, 56, 66, 28, 14, 'autre', label='norme 6', size='s')
text(ax, 44, 60, 'normes différentes : nombres différents', 'resultat', 's')
# ligne 2 : racine de 3 i, normes égales
text(ax, 44, 50, r'dans $\mathbb{Z}[\sqrt{3}\,i]$', 'encre', 'm')
box(ax, 4, 28, 28, 14, 'sujet', label='2 : norme 4', size='s')
text(ax, 44, 35, '=', 'varie', 'l')
box(ax, 56, 28, 28, 14, 'autre', label='1 + √3 i : norme 4', size='s')
text(ax, 44, 22, 'normes égales : on ne peut pas conclure', 'varie', 's')
box(ax, 4, 3, 80, 12, 'fixe', label='il faut lister les associés de 2 : 2 × 1 et 2 × (−1)', size='s')
save(fig, '56-058')
