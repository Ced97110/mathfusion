import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ax.set_ylim(24, 96)  # même échelle ; centre le contenu verticalement
text(ax, 44, 90, "étape 2 : d'abord ² et √", 'fixe', 's')
# ligne 1 : exposant
text(ax, 9, 80, '2 ×', 'encre', 'l')
box(ax, 16, 75, 12, 10, 'varie', label='3²', size='l')
arrow(ax, (28, 80), (40, 80), 'varie')
for i in range(3):
    for j in range(3):
        box(ax, 40 + 3 * i, 75.5 + 3 * j, 3, 3, 'sujet', r=0.3)
text(ax, 56, 80, '= 9', 'encre', 'm')
arrow(ax, (61, 80), (66, 80), 'fixe')
box(ax, 66, 75, 20, 10, 'resultat', label='2 × 9 = 18', size='m')
line(ax, [(4, 67), (84, 67)], 'fixe', dash=True)
# ligne 2 : racine
text(ax, 9, 52, '10 +', 'encre', 'l')
box(ax, 17, 47, 14, 10, 'varie', label='√16', size='l')
arrow(ax, (31, 52), (40, 52), 'varie')
for i in range(4):
    for j in range(4):
        box(ax, 40 + 3 * i, 46 + 3 * j, 3, 3, 'sujet', r=0.3)
text(ax, 46, 62, '16 carreaux', 'sujet', 's')
brace(ax, 40, 52, 45, 'varie', label='côté 4', down=True, size='s')
text(ax, 58, 52, '= 4', 'encre', 'm')
arrow(ax, (62.3, 52), (66, 52), 'fixe')
box(ax, 66, 47, 20, 10, 'resultat', label='10 + 4 = 14', size='m')
text(ax, 44, 30, "pas 10 + 16 d'abord", 'limite', 's')
save(fig, '04-060')
