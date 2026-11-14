import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cells = {(0, 0): ('1', 'resultat'), (0, 1): (r'$i$', 'sujet'), (1, 0): (r'$-i$', 'autre'), (1, 1): ('1', 'resultat')}
for (r, c), (lab, ro) in cells.items():
    box(ax, 4 + c * 34, 38 - r * 26, 16, 16, ro, label=lab, size='l', weight='bold')
arrow(ax, (38, 38), (20, 30), 'varie', both=True)
text(ax, 70, 36, r'$i$ et $-i$', 'varie', 'm'); text(ax, 70, 29, 'conjugués', 'varie', 's')
text(ax, 31, 59, 'matrice 2 sur 2', 'encre', 's')
text(ax, 31, 6, 'diagonale : réels', 'resultat', 's')
save(fig, '75-151')
