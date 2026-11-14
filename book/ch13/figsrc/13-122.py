import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = ['parenthèses', 'multiplications (signes)', 'le haut', 'le bas', 'division']
for i, s in enumerate(steps):
    y = 74 - i * 15
    last = i == len(steps) - 1
    box(ax, 2, y, 44, 10, 'resultat' if last else 'sujet', label=s, size='s')
    if i: arrow(ax, (24, y + 15), (24, y + 10), 'varie')
text(ax, 66, 48, 'il reste :', 'fixe', 's')
text(ax, 66, 38, '20 en haut', 'sujet', 'm'); text(ax, 66, 28, '−4 en bas', 'autre', 'm')
text(ax, 66, 15, '20 ÷ (−4) = −5', 'resultat', 'm')
save(fig, '13-122')
