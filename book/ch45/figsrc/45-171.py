import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, 'ou ordinaire', 'autre'); text(ax, 66, 60, 'ou exclusif  ⊕', 'sujet')
for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
    y = 46 - 11 * i; last = i == 3
    box(ax, 3, y, 38, 9, 'autre' if last else 'fixe', label=f'{a} ou {b} = {int(a or b)}')
    box(ax, 47, y, 38, 9, 'sujet' if last else 'fixe', label=f'{a} ⊕ {b} = {a ^ b}')
text(ax, 44, 6, 'seule différence : 1 et 1', 'varie')
save(fig, '45-171')
