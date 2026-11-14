import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 18, 67, 'la preuve', 'sujet', 's', weight='bold')
text(ax, 69, 67, 'feuille des règles', 'fixe', 's', weight='bold')
box(ax, 52, 28, 34, 36, 'fixe')
ent = [r'$a+(-a)=0$', 'règle de la ligne 2', 'règle de la ligne 3']
for i in range(3):
    y = 52 - 10 * i
    box(ax, 2, y - 3, 32, 9, 'sujet', label='ligne %d' % (i + 1), size='s')
    text(ax, 69, y + 1.5, ent[i], 'encre', 's')
    arrow(ax, (34, y + 1.5), (52, y + 1.5), 'varie')
box(ax, 20, 4, 66, 18, 'resultat')
text(ax, 53, 17, 'monde avec toutes ces règles', 'resultat', 's')
text(ax, 53, 9, 'la preuve y marche', 'resultat', 'm', weight='bold')
arrow(ax, (69, 28), (69, 22), 'resultat')
save(fig, '51-005')
