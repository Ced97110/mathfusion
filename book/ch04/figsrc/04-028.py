import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(72)
# écriture 5 × 4² : le petit 2 ne porte que sur le 4
text(ax, 38, 66, '5 ×', 'fixe', 'l')
text(ax, 44, 66, '4', 'sujet', 'l')
text(ax, 46.6, 68.6, '2', 'varie', 's')
box(ax, 41.5, 62.5, 7.5, 8.5, 'varie', fill=False)
text(ax, 66, 66, 'le 2 compte les 4', 'varie', 's')
text(ax, 18, 60, 'le 5 : écrit 1 fois', 'fixe', 's')
# cinq carrés de 4 × 4 carreaux de 3,2 mm
text(ax, 4, 54.5, r'$4^{2}$ = 16', 'sujet', 's', ha='left')
for x0 in [6, 21.8, 37.6, 53.4, 69.2]:
    for i in range(4):
        for j in range(4):
            box(ax, x0 + 3.2*i, 38 + 3.2*j, 3.2, 3.2, 'sujet', r=0.1)
arrow(ax, (44, 62.5), (19.5, 51.3), 'varie')
brace(ax, 6, 82, 36, 'resultat', label='5 fois 16 = 80 carreaux', size='s')
# lecture fausse
text(ax, 44, 24, 'si le 2 portait sur 5 × 4 :', 'limite', 's')
text(ax, 44, 17, '5 × 4 × 5 × 4 = 400', 'limite', 'm')
text(ax, 44, 10, '400 ≠ 80 : autre produit', 'limite', 's')
save(fig, '04-028')
