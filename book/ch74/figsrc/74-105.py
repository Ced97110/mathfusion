import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
vals = [[2, 5], [7, 4]]
for i in range(2):
    for j in range(2):
        d = i == j
        box(ax, 8 + j * 16, 24 - i * 16, 14, 14, 'sujet' if d else 'fixe', label=str(vals[i][j]), size='l', weight='bold' if d else 'normal')
text(ax, 20, 5, 'diagonale en bleu', 'sujet', 's')
arrow(ax, (42, 31), (52, 31), 'varie'); text(ax, 47, 36, 'somme', 'varie', 's')
arrow(ax, (42, 15), (52, 15), 'varie')
box(ax, 54, 18, 30, 18, 'resultat', label=r'$2+4=6$', size='l')
text(ax, 69, 9, r'$\mathrm{tr}\,M=6$', 'resultat', 'l')
save(fig, '74-105')
