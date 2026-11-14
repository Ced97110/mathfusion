import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 58, 'ℤ/4', 'sujet', 'xl'); text(ax, 44, 58, '⊕', 'varie', 'xl'); text(ax, 66, 58, 'ℤ/3', 'autre', 'xl')
text(ax, 44, 50, 'un de chaque', 'varie', 's')
for j in range(4):
    box(ax, 4 + 9 * j + 0.4, 36, 8.2, 9, 'varie' if j == 3 else 'sujet', label=str(j), size='s', r=0.6)
for j in range(3):
    box(ax, 52.5 + 9 * j + 0.4, 36, 8.2, 9, 'varie' if j == 1 else 'autre', label=str(j), size='s', r=0.6)
box(ax, 34, 14, 20, 9, 'resultat', label='(3, 1)', size='m')
arrow(ax, (31.5 + 0.5, 35.5), (38, 23.5), 'varie')
arrow(ax, (66.5 - 0.5, 35.5), (50, 23.5), 'varie')
text(ax, 22, 29, '1re place : 3', 'varie', 's')
text(ax, 66, 29, '2e place : 1', 'varie', 's')
text(ax, 44, 6, 'un couple : un élément de chaque', 'encre', 's')
save(fig, '60-006')
