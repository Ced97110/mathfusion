import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 57, "l'histoire dit : gagner 3", 'varie', 'm')
box(ax, 4, 38, 22, 10, 'sujet', label='avant ?')
box(ax, 62, 38, 22, 10, 'resultat', label='44')
arrow(ax, (27, 43), (61, 43), 'varie')
text(ax, 44, 47.5, '+ 3', 'varie', 'm')
text(ax, 44, 26, 'la réponse dit : retirer 3', 'varie', 'm')
box(ax, 4, 7, 22, 10, 'sujet', label='41')
box(ax, 62, 7, 22, 10, 'resultat', label='44')
arrow(ax, (61, 12), (27, 12), 'varie')
text(ax, 44, 16.5, '− 3', 'varie', 'm')
save(fig, '16-002')
