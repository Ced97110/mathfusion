import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y, title, op in [(42, 'pour l’addition', '+ 0'), (20, 'pour la multiplication', '· 1')]:
    text(ax, 44, y + 10, title, 'encre', 's')
    box(ax, 10, y - 4.5, 14, 9, 'fixe', label='12')
    arrow(ax, (27, y), (61, y), 'varie')
    text(ax, 44, y + 3.5, op, 'sujet', 'l', weight='bold')
    box(ax, 64, y - 4.5, 14, 9, 'resultat', label='12')
text(ax, 44, 6, 'le nombre ne change pas', 'resultat', 'm')
save(fig, '12-103')
