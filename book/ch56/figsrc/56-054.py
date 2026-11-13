import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# Ligne du haut : les nombres
text(ax, 44, 80, 'on multiplie, puis on prend la norme', 'encre', 's')
box(ax, 1, 56, 28, 14, 'sujet', label=r'$z=1+\sqrt{3}\,i$', size='s')
text(ax, 31, 63, '×', 'encre', 'm')
box(ax, 33, 56, 28, 14, 'autre', label=r'$w=1-\sqrt{3}\,i$', size='s')
text(ax, 64, 63, '=', 'encre', 'm')
box(ax, 67, 56, 20, 14, 'resultat', label='zw = 4', size='s')
# flèches ν
for xc in (15, 47, 77):
    arrow(ax, (xc, 55), (xc, 41), 'varie')
text(ax, 22, 48, 'ν', 'varie', 'm')
# Ligne du bas : les normes
box(ax, 1, 26, 28, 14, 'sujet', label='ν(z) = 4', size='s')
text(ax, 31, 33, '×', 'encre', 'm')
box(ax, 33, 26, 28, 14, 'autre', label='ν(w) = 4', size='s')
text(ax, 64, 33, '=', 'encre', 'm')
box(ax, 67, 26, 20, 14, 'resultat', label='ν(4) = 16', size='s')
text(ax, 44, 14, '4 × 4 = 16 : même résultat', 'resultat', 'm')
save(fig, '56-054')
