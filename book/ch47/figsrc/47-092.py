import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'sous-groupes emboîtés de l’horloge', 'fixe', 's')
for x, w_, lab, role in [(3, 24, '12 heures', 'sujet'), (35, 22, '4 heures', 'varie'), (65, 20, '2 heures', 'autre')]:
    box(ax, x, 56, w_, 14, role, label=lab, size='s')
arrow(ax, (27.5, 63), (34.5, 63), 'fixe'); arrow(ax, (57.5, 63), (64.5, 63), 'fixe')
text(ax, 31, 74, '3', 'varie', 'm'); text(ax, 61, 74, '2', 'varie', 'm')
text(ax, 44, 46, r'$3\times2=6$', 'resultat', 'l')
box(ax, 6, 8, 76, 24, 'fixe', fill=False, dash=True)
text(ax, 44, 26, 'chapitre 61 : degrés des corps', 'fixe', 's')
text(ax, 44, 15, 'même forme de règle', 'resultat', 's')
save(fig, '47-092')
