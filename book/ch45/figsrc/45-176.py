import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, 'répéter le couple 4 fois', 'encre')
for i, l in enumerate(['(1, 1)', '(0, 2)', '(1, 0)', '(0, 1)']):
    box(ax, 3 + 21 * i, 40, 17, 10, 'resultat' if i == 3 else 'fixe', label=l)
    if i: arrow(ax, (3 + 21 * i - 3.5, 45), (3 + 21 * i - 0.5, 45), 'varie')
text(ax, 44, 33, 'répéter chaque case', 'encre')
box(ax, 3, 18, 40, 10, 'sujet', label='4 ajouts de 1 : reste 0'); box(ax, 45, 18, 40, 10, 'autre', label='4 ajouts de 1 : reste 1')
arrow(ax, (23, 18), (36, 11.5), 'varie'); arrow(ax, (65, 18), (52, 11.5), 'varie')
box(ax, 22, 2, 44, 9, 'resultat', label='(0, 1) : le même couple')
save(fig, '45-176')
