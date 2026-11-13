import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 22, 46, 22, 11, 'sujet', label='n = 55')
arrow(ax, (28, 46), (16, 36), 'varie')
arrow(ax, (38, 46), (50, 36), 'varie')
box(ax, 6, 25, 20, 11, 'sujet', label='5', size='l')
box(ax, 40, 25, 20, 11, 'sujet', label='11', size='l')
text(ax, 33, 17, 'une seule réponse', 'resultat', 'm')
box(ax, 64, 32, 21, 13, 'fixe', fill=False, dash=True, label='autre couple ?', size='s')
text(ax, 74.5, 27, 'aucun', 'fixe', 's')
text(ax, 44, 7, '55 = 5 × 11 et pas autrement', 'resultat', 'm') if False else None
text(ax, 44, 6, '« quels sont les facteurs ? »', 'encre', 's')
save(fig, '53-190')
