import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
yc = 26
box(ax, 2, yc - 5, 12, 10, 'fixe', label='1')
text(ax, 8, yc - 9, 'message', 'fixe', 's')
arrow(ax, (15, yc), (28, yc), 'varie')
text(ax, 21.5, yc + 3.5, r'$G$', 'varie', 'm')
box(ax, 29, yc - 5, 20, 10, 'resultat', label='111')
text(ax, 39, yc - 9, 'mot envoyé', 'resultat', 's')
for i in range(3):
    box(ax, 62, yc - 14.5 + i * 10, 9, 9, 'sujet', label='1')
text(ax, 59, yc, r'$G=$', 'sujet', 'm', ha='right')
text(ax, 74, yc + 4, '3 lignes', 'fixe', 's', ha='left')
text(ax, 74, yc - 4, '1 colonne', 'fixe', 's', ha='left')
save(fig, '68-075')
