import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(80)
ax.set_ylim(4, 84)  # coordonnées de la spec conservées ; fenêtre resserrée sur le contenu
# aller et retour : + 3 et − 3
box(ax, 14, 66, 12, 10, 'fixe', label='4')
box(ax, 62, 66, 12, 10, 'fixe', label='7')
arrow(ax, (27, 74), (61, 74), 'fixe', curve=-0.25)
text(ax, 44, 81, '+ 3', 'fixe', 's')
arrow(ax, (61, 68), (27, 68), 'fixe', curve=-0.25)
text(ax, 44, 61, '− 3', 'fixe', 's')
# même famille
text(ax, 44, 53, 'même famille : on défait', 'encre', 's')
line(ax, [(4, 57), (84, 57)], 'fixe')
line(ax, [(4, 49), (84, 49)], 'fixe')
# côté : une rangée de 4 carreaux de 6 mm
for i in range(4):
    box(ax, 8 + 6*i, 28, 6, 6, 'resultat', r=0.1)
brace(ax, 8, 32, 26, 'resultat', label='côté : 4', size='s')
# aire : carré de 4 × 4 carreaux de 6 mm
for i in range(4):
    for j in range(4):
        box(ax, 58 + 6*i, 16 + 6*j, 6, 6, 'fixe', r=0.1)
text(ax, 70, 44, 'aire : 16', 'fixe', 's')
# au carré (côté vers aire) et racine carrée (aire vers côté)
arrow(ax, (33, 32), (57.5, 35), 'autre', curve=-0.2)  # du bord du côté au bord de l'aire
text(ax, 45, 41, 'au carré', 'autre', 's')
arrow(ax, (58, 20), (32.8, 28.5), 'sujet', lw=1.6, curve=-0.2)  # du bord de l'aire au bord du côté
text(ax, 45, 16, 'racine carrée', 'sujet', 's')
text(ax, 44, 7, 'de même : de 25, on a 5', 'sujet', 's')
save(fig, '04-033')
