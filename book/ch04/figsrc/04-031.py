import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(58)
ax.set_ylim(11, 69)  # coordonnées de la spec conservées ; fenêtre resserrée sur le contenu
# carré de 4 × 4 carreaux de 7 mm
for i in range(4):
    for j in range(4):
        box(ax, 12 + 7*i, 22 + 7*j, 7, 7, 'sujet', r=0.2)
text(ax, 26, 56, r'$A$ = 16', 'sujet', 'm')
text(ax, 6.5, 36, r'$c$ = ?', 'fixe', 's')
# étape 1 : compter une rangée (la rangée du bas)
for i in range(4):
    box(ax, 12 + 7*i, 22, 7, 7, 'varie', r=0.2)
    text(ax, 15.5 + 7*i, 25.5, str(i + 1), 'varie', 's')
brace(ax, 12, 40, 20, 'resultat', label=r'$c$ = 4', size='s')
text(ax, 26, 64, '1. compter', 'varie', 's')
text(ax, 70, 64, '2. vérifier', 'resultat', 's')
arrow(ax, (41, 36), (55, 36), 'varie')
# étape 2 : quatre rangées de 4 remplissent le carré
for i in range(4):
    for j in range(4):
        box(ax, 56 + 7*i, 22 + 7*j, 7, 7, 'resultat', r=0.2, lw=0.4)
for y in [29, 36, 43]:
    line(ax, [(56, y), (84, y)], 'resultat', lw=1.4)
box(ax, 56, 22, 28, 28, 'fixe', fill=False, dash=True)  # contour pointillé, dessiné par-dessus
text(ax, 70, 56, '4 rangées de 4', 'resultat', 's')
text(ax, 70, 16, '4 × 4 = 16 : rempli', 'resultat', 's')
save(fig, '04-031')
