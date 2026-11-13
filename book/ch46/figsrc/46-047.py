import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
text(ax, 44, 55, '$g = 9$ et $h = 5$ sur l’horloge', 'encre', 's')
box(ax, 3, 30, 22, 12, 'sujet', label=r'$g\,h^{-1}$', size='l'); box(ax, 3, 8, 22, 12, 'varie', label=r'$g - h$', size='l')
text(ax, 45, 39, '9 + 7 = 16, soit 4', 'sujet', 'm'); text(ax, 45, 33, '7 est l’inverse de 5', 'sujet', 's')
text(ax, 45, 14, '9 − 5 = 4', 'varie', 'm')
arrow(ax, (26, 36), (33, 36), 'sujet', lw=0.8); arrow(ax, (26, 14), (33, 14), 'varie', lw=0.8)
box(ax, 66, 17, 18, 17, 'resultat', label='4', size='xl')
arrow(ax, (62, 36), (66, 29), 'sujet'); arrow(ax, (62, 14), (66, 22), 'varie')
text(ax, 75, 11, 'même résultat', 'resultat', 's')
save(fig, '46-047')
