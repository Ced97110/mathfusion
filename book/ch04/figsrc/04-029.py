import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(62)
ax.set_ylim(16, 78)  # coordonnées de la spec conservées ; fenêtre resserrée sur le contenu
# rangée du haut : 5, 5, 5, 9, 9
for x in [4, 16, 28]:
    box(ax, x, 66, 10, 9, 'sujet', label='5')
for x in [48, 60]:
    box(ax, x, 66, 10, 9, 'autre', label='9')
for a, b in [(14, 16), (26, 28), (38, 48), (58, 60)]:
    line(ax, [(a, 70.5), (b, 70.5)], 'fixe')
brace(ax, 4, 38, 64, 'sujet', label='5 : 3 fois', size='s')
brace(ax, 48, 70, 64, 'autre', label='9 : 2 fois', size='s')
# écriture : chaque base reçoit son exposant
text(ax, 44, 50, r'$5^{3} \times 9^{2}$', 'resultat', 'l')
arrow(ax, (21, 58), (38, 53), 'varie')
arrow(ax, (59, 58), (50, 53), 'varie')
# rangée du bas : 5, 9, 5, 9, 5 (ordre mélangé)
for x, v in zip([11, 25, 39, 53, 67], ['5', '9', '5', '9', '5']):
    box(ax, x, 20, 10, 9, 'sujet' if v == '5' else 'autre', label=v)
for a, b in [(21, 25), (35, 39), (49, 53), (63, 67)]:
    line(ax, [(a, 24.5), (b, 24.5)], 'fixe')
text(ax, 44, 35, r'autre ordre : même $5^{3} \times 9^{2}$', 'varie', 's')
arrow(ax, (44, 37.5), (44, 47.8), 'varie')
save(fig, '04-029')
