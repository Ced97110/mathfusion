import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(58)
ax.set_ylim(20, 78)  # coordonnées de la spec conservées ; fenêtre resserrée sur le contenu
text(ax, 44, 74, r'$8^{5}$', 'encre', 'l')
text(ax, 16, 74, '1. base : 8', 'sujet', 's')
arrow(ax, (24, 74), (41.5, 74), 'sujet')
text(ax, 70, 74, '2. exposant : 5', 'autre', 's')
arrow(ax, (60, 75), (46.5, 75), 'autre')
# cinq facteurs 8
for x in [6, 22, 38, 54, 70]:
    box(ax, x, 55, 12, 9, 'sujet', label='8')
brace(ax, 6, 82, 66, 'autre', label='3. écrire 5 facteurs 8', down=False)
# états après chaque multiplication
box(ax, 23, 34, 10, 8, 'varie', label='64')
box(ax, 39, 34, 10, 8, 'varie', label='512')
box(ax, 54.5, 34, 11, 8, 'varie', label='4 096')
box(ax, 69, 34, 14, 8, 'resultat', label='32 768')
arrow(ax, (12, 55), (24, 42), 'varie')
for x in [28, 44, 60, 76]:
    arrow(ax, (x, 55), (x, 42), 'varie')
for a, b in [(33, 39), (49, 54.5), (65.5, 69)]:
    arrow(ax, (a, 38), (b, 38), 'varie')
text(ax, 44, 24, '4 multiplications, puis fin', 'varie', 's')
line(ax, [(85, 32), (85, 44)], 'resultat', lw=2.0)
save(fig, '04-025')
