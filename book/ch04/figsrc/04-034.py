import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(100)

# titres de colonne
text(ax, 25, 95, 'Sans le signe', 'encre', 's')
text(ax, 72, 95, 'Avec le signe', 'encre', 's')

# sans le signe : la phrase entière, pour 16 puis pour 25
box(ax, 3, 78, 44, 13, 'fixe')
text(ax, 25, 87.5, 'le nombre qui, multiplié', 'encre', 's')
text(ax, 25, 82, 'par lui-même, donne 16', 'encre', 's')
box(ax, 3, 60, 44, 13, 'fixe')
text(ax, 25, 69.5, 'le nombre qui, multiplié', 'encre', 's')
text(ax, 25, 64, 'par lui-même, donne 25', 'encre', 's')

# passage de la phrase au signe
arrow(ax, (48, 84.5), (58, 84.5), 'varie', lw=1.0)
arrow(ax, (48, 66.5), (58, 66.5), 'varie', lw=1.0)
text(ax, 72, 84.5, '√16', 'sujet', 'l')
text(ax, 72, 66.5, '√25', 'sujet', 'l')

# le signe en morceaux
text(ax, 44, 52, 'Le signe en morceaux', 'encre', 's')
line(ax, [(22, 32), (24, 33.5), (27, 24), (30, 38), (44, 38)], 'sujet', lw=1.6)
text(ax, 37, 31, '16', 'encre', 'l')
text(ax, 18, 44, 'racine carrée de', 'sujet', 's')
line(ax, [(20, 42.5), (25.4, 30)], 'sujet', lw=0.6)
text(ax, 37, 18, 'le nombre écrit après', 'encre', 's')
line(ax, [(37, 20), (37, 29.6)], 'fixe', lw=0.6)
text(ax, 51, 31, '= 4', 'resultat', 'l')
text(ax, 70, 31, 'se lit d’un coup', 'resultat', 's')

save(fig, '04-034')
