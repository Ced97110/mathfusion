import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
box(ax, 2, 10, 32, 28, 'fixe'); box(ax, 54, 10, 32, 28, 'resultat')
text(ax, 18, 32, 'affirmation', 'fixe', 'm'); text(ax, 18, 24, 'multiple de 4', 'encre', 's'); text(ax, 18, 18, 'alors pair', 'encre', 's')
text(ax, 70, 32, 'proposition', 'resultat', 'm', weight='bold'); text(ax, 70, 24, 'multiple de 4', 'encre', 's'); text(ax, 70, 18, 'alors pair', 'encre', 's')
arrow(ax, (35.5, 24), (52.5, 24), 'varie')
text(ax, 44, 30, 'preuve', 'varie', 's'); text(ax, 44, 18, r'$4 = 2 \times 2$', 'varie', 's')
text(ax, 44, 43, 'un énoncé prouvé', 'sujet', 'm')
save(fig, '42-101')
