import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cols = [40, 54, 66]
rows = [(r'$0{,}5$', '0', '0'), (r'$0{,}2$', '5', '0'), (r'$0{,}1$', '2', '5')]
for i, row in enumerate(rows):
    y = 68 - 11 * i
    for j, s in enumerate(row):
        if j == i: disc(ax, cols[j] + (0.2 if j == 0 else 0), y, 4.2, 'varie')
        if j == 0: text(ax, cols[0] + 1.6, y, s, 'encre', 'm', ha='right')
        else: text(ax, cols[j], y, s, 'encre', 'm')
text(ax, 4, 36, 'chiffres de la diagonale', 'varie', 's', ha='left')
for j in range(3):
    box(ax, cols[j] - 6, 16, 12, 12, 'resultat')
    text(ax, cols[j] + (1.6 if j == 0 else 0), 22, r'$0{,}6$' if j == 0 else '6', 'resultat', 'm', ha='right' if j == 0 else 'center')
text(ax, 4, 6, 'diffère de chaque ligne', 'resultat', 's', ha='left')
save(fig, '43-117')
