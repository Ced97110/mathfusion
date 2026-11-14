import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for i, b in enumerate('101'):
    box(ax, 22 + i * 11, 34, 9, 9, 'varie', label=b, size='l')
for i, b in enumerate('111'):
    box(ax, 22 + i * 11, 10, 9, 9, 'resultat', label=b, size='l')
text(ax, 2, 38.5, 'reçu\n(orange)', 'varie', 's', ha='left')
text(ax, 2, 14.5, 'envoyé', 'resultat', 's', ha='left')
text(ax, 58, 38.5, 'à 1 pas de 111\nà 2 pas de 000', 'varie', 's', ha='left')
arrow(ax, (37.5, 33.5), (37.5, 19.8), 'varie')
text(ax, 40.5, 26.5, '2e bit inversé', 'varie', 's', ha='left')
text(ax, 44, 4, 'valable si une seule erreur', 'fixe', 's')
save(fig, '68-018')
