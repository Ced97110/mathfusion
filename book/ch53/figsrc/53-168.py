import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# côté utilisateur : quelques millisecondes (barre minuscule)
text(ax, 4, 54, 'Alice et Bob', 'sujet', 'm', ha='left', weight='bold')
box(ax, 4, 43, 2.2, 7, 'sujet')
text(ax, 9, 46.5, 'quelques millisecondes', 'sujet', 'm', ha='left')
# côté attaquant : barre très longue, coupée
text(ax, 4, 35, 'L’attaquant', 'varie', 'm', ha='left', weight='bold')
box(ax, 4, 23, 80, 8, 'varie')
ax.add_patch(Polygon([(44, 22.6), (50, 22.6), (52, 31.4), (46, 31.4)], closed=True, ec='white', fc='white', lw=0.5, zorder=2.5))
line(ax, [(44, 23), (46, 31)], 'varie')
line(ax, [(50, 23), (52, 31)], 'varie')
text(ax, 24, 27, 'des milliers d’années', 'varie', 'm')
# le calcul des secondes
text(ax, 44, 13, '1 an = 31 536 000 secondes', 'fixe', 's')
text(ax, 44, 7, 'mille ans : plus de 31 000 milliards de ms', 'fixe', 's') if False else None
text(ax, 44, 7.5, 'mille ans, c’est plus de', 'fixe', 's')
text(ax, 44, 3, '31 000 milliards de ms', 'fixe', 's')
save(fig, '53-168')
