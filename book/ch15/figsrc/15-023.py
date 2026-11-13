import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 5, 40, 22, 11, 'sujet', label=r'$5x$'); arrow(ax, (29, 45.5), (45, 45.5), 'varie')
box(ax, 47, 40, 36, 11, 'resultat', label=r'$5 \times x$')
text(ax, 44, 33, 'un nombre devant une lettre : fois', 'sujet', 's')
box(ax, 5, 8, 22, 11, 'fixe', label=r'$53$'); arrow(ax, (29, 13.5), (45, 13.5), 'fixe')
text(ax, 65, 13.5, 'cinquante-trois', 'fixe', 'm')
text(ax, 44, 24, 'deux chiffres : un seul nombre', 'fixe', 's')
save(fig, '15-023')
