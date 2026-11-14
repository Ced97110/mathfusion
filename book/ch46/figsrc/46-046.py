import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
text(ax, 44, 53, r'$g\,h^{-1}$ : le produit de $g$ par l’inverse de $h$', 'encre', 's')
for x, role, lab, sub in [(14, 'sujet', '$g$', '$g = 8$'), (44, 'varie', r'$h^{-1}$', r'$h = 4$, donc $h^{-1} = 8$'), (74, 'resultat', r'$g\,h^{-1}$', '8 + 8 = 16, soit 4')]:
    box(ax, x - 11, 28, 22, 13, role, label=lab, size='l')
    text(ax, x, 20, sub, role, 's')
arrow(ax, (25, 34.5), (33, 34.5), 'fixe'); arrow(ax, (55, 34.5), (63, 34.5), 'fixe')
text(ax, 29, 38, '+', 'fixe', 'm'); text(ax, 59, 38, '=', 'fixe', 'm')
text(ax, 44, 8, 'sur l’horloge, le produit est une somme', 'fixe', 's')
save(fig, '46-046')
