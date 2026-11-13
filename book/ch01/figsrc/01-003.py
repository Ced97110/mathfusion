import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for i in range(12):
    line(ax, [(6 + i, 56), (6 + i, 60)], 'sujet')
text(ax, 22, 58, '12 boîtes : 12 traits', 'sujet', 's', ha='left')
for i in range(75):
    line(ax, [(6 + i, 38), (6 + i, 42)], 'sujet')
text(ax, 44, 47, '4 329 boîtes → 4 329 traits', 'sujet', 's')
arrow(ax, (81, 40), (86, 40), 'limite')
text(ax, 44, 33, 'ici 75 traits sur 4 329', 'limite', 's')
text(ax, 22, 19, '4 329', 'resultat', 'l')
brace(ax, 17, 27, 14.5, 'resultat', label='4 signes')
text(ax, 64, 19, '43 290', 'resultat', 'l')
brace(ax, 58.5, 69.5, 14.5, 'resultat', label='5 signes')
arrow(ax, (28, 19), (57, 19), 'varie')
text(ax, 42.5, 22.5, '× 10', 'varie', 's')
save(fig, '01-003')
