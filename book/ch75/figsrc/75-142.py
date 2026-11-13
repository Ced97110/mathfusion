import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
C = (40, 50); R = 15
V = {'(1, 0)': (1, 0), '(0, 1)': (0, 1), '(2, 0)': (-1, 0), '(0, 2)': (0, -1)}
poly(ax, [(C[0] + R * dx, C[1] + R * dy) for dx, dy in V.values()], 'sujet')
line(ax, [(C[0] - R - 5, C[1]), (C[0] + R + 5, C[1])], 'fixe', dash=True)
for lab, (dx, dy) in V.items():
    disc(ax, C[0] + R * dx, C[1] + R * dy, 2.2, 'sujet')
    text(ax, C[0] + (R + 12) * dx, C[1] + (R + 6) * dy, lab, 'sujet', 's')
arrow(ax, (C[0] + R + 3, C[1] + 6), (C[0] + 6, C[1] + R + 3), 'varie', curve=0.4)
arrow(ax, (C[0], C[1] + 8), (C[0], C[1] - 8), 'varie', both=True)
text(ax, 44, 20, 'flèche courbe : quart de tour', 'varie', 's'); text(ax, 44, 14, 'flèche droite : symétrie', 'varie', 's')
text(ax, 44, 6, '8 transformations en tout', 'resultat', 'm', weight='bold')
save(fig, '75-142')
