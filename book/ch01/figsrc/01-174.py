import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
line(ax, [(31,62),(16,62),(24,52),(16,42),(31,42)], 'sujet', lw=1.8)
# sous le signe
text(ax, 23, 37, r'$k = 0$', 'varie', 'l')
line(ax, [(28,37),(33,37)], 'fixe', lw=0.6)
text(ax, 34, 37, 'lettre qui varie, départ', 'fixe', 's', ha='left')
# au-dessus
text(ax, 23, 67, '3', 'varie', 'l')
line(ax, [(26,67),(43,67)], 'fixe', lw=0.6)
text(ax, 44, 67, 'dernière valeur', 'fixe', 's', ha='left')
# à droite
text(ax, 36, 52, r'$k$', 'sujet', 'l')
line(ax, [(38,52),(43,52)], 'fixe', lw=0.6)
text(ax, 44, 52, "ce qu'on additionne", 'fixe', 's', ha='left')
# dépliage
arrow(ax, (23,33), (27,16), 'varie')
text(ax, 46, 25, r'$k$ prend 0, 1, 2, 3', 'varie', 'm')
text(ax, 38, 11, '0 + 1 + 2 + 3', 'encre', 'l')
text(ax, 57, 11, '= 6', 'resultat', 'l', weight='bold')
save(fig, '01-174')
