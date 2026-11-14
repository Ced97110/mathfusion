import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 3, 55, 38, 10, 'fixe', label='2 − x + 3x³')
box(ax, 47, 55, 38, 10, 'fixe', label='2 − t + 3t³')
text(ax, 44, 60, '=', 'resultat', 'l')
text(ax, 22, 50, 'la lettre : x', 'varie', 's')
text(ax, 66, 50, 'la lettre : t', 'varie', 's')
arrow(ax, (22, 47), (32, 29.5), 'fixe')
arrow(ax, (66, 47), (56, 29.5), 'fixe')
for cx, v in zip((26, 38, 50, 62), ('2', '−1', '0', '3')):
    box(ax, cx - 5.5, 17, 11, 12, 'sujet', label=v)
text(ax, 44, 10, 'mêmes barres : 2, −1, 0, 3', 'sujet', 's')
save(fig, '54-081')
