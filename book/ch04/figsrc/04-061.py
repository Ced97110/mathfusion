import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ax.set_ylim(19, 95)  # même échelle ; centre le contenu verticalement
text(ax, 44, 90, '24 ÷ 4 × 2', 'encre', 'l', weight='bold')
line(ax, [(44, 20), (44, 85)], 'fixe', dash=True)
# gauche : ÷ 4 d'abord
text(ax, 23, 82, "÷ 4 d'abord : 4 parts de 6", 'resultat', 's')
ROW_X = [12, 16.5, 21, 25.5, 30, 34.5]
for k, y in enumerate([74, 69.5, 65, 60.5]):
    for x in ROW_X:
        disc(ax, x, y, 1.4, 'varie' if k == 0 else 'fixe')
arrow(ax, (38, 73), (38, 50), 'varie')
text(ax, 41.5, 61.5, '× 2', 'varie', 's')
for y in (48, 43.5):
    for x in ROW_X:
        disc(ax, x, y, 1.4, 'resultat')
box(ax, 13, 30, 20, 8, 'resultat', label='= 12', size='l')
text(ax, 23, 24, 'le × porte sur 6', 'resultat', 's')
# droite : × 2 d'abord
text(ax, 66, 82, "4 × 2 d'abord : 8 parts de 3", 'limite', 's')
for k, y in enumerate([74, 69.5, 65, 60.5, 56, 51.5, 47, 42.5]):
    for x in (61.5, 66, 70.5):
        disc(ax, x, y, 1.4, 'varie' if k == 0 else 'fixe')
box(ax, 56, 30, 20, 8, 'limite', label='= 3', size='l')
text(ax, 66, 24, 'le × porte sur le 4 seul', 'limite', 's')
save(fig, '04-061')
