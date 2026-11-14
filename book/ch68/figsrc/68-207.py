import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
text(ax, 44, 103, 'départ : 2 coefficients ≠ 0', 'sujet', 'm')
w = '0?00?00'
cw, x0 = 7, 19.5
for i, c in enumerate(w):
    box(ax, x0 + i * cw, 90, cw, 7, 'varie' if c == '?' else 'fixe', label=c, r=0.5)
text(ax, 44, 84, 'les ? sont les 2 inconnues', 'varie', 's')
box(ax, 4, 66, 38, 11, 'sujet', label='annulation en α', size='s')
box(ax, 46, 66, 38, 11, 'sujet', label='annulation en α²', size='s')
text(ax, 44, 60, 'α : élément du corps à 8 éléments', 'fixe', 's')
arrow(ax, (23, 59), (36, 51.5), 'varie')
arrow(ax, (65, 59), (52, 51.5), 'varie')
box(ax, 14, 39, 60, 12, 'varie', label='déterminant ≠ 0 (Vandermonde)', size='s')
text(ax, 44, 33.5, 'donc la seule solution est 0', 'varie', 's')
arrow(ax, (44, 31), (44, 26), 'resultat')
box(ax, 14, 13, 60, 12, 'resultat', label='les 2 inconnues valent 0', size='s')
text(ax, 44, 7, 'aucun mot non nul n’a si peu de', 'resultat', 's')
text(ax, 44, 2.5, 'coefficients non nuls', 'resultat', 's')
save(fig, '68-207')
