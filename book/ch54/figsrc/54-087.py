import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
arrow(ax, (8, 55), (80, 55), 'varie')
text(ax, 44, 59, 'lire de gauche à droite', 'varie', 's')
text(ax, 4, 41, '(', 'sujet', 'xl')
text(ax, 84, 41, ')', 'sujet', 'xl')
cs = [14, 30, 46, 62]
for i, cx in enumerate(cs):
    box(ax, cx - 6.5, 36, 13, 10, 'sujet', label=rf'$a_{i}$')
text(ax, 74, 40, '…', 'sujet', 'l')
for cx, v in zip(cs, ('2', '−1', '0', '3')):
    arrow(ax, (cx, 35), (cx, 28), 'fixe')
    box(ax, cx - 6.5, 17, 13, 10, 'resultat', label=v)
text(ax, 22, 8, '( ) : l’ordre compte', 'sujet', 's')
text(ax, 66, 8, '… : et ainsi de suite', 'sujet', 's')
save(fig, '54-087')
