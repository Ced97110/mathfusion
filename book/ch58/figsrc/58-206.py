import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# stock (5, 4) : 5 fois la colonne 1, puis 4 fois la colonne 2, bout à bout
ox, oy, u = 8, 8, 3.2
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(0, 0), P(10, 5), 'sujet', lw=1.8)
arrow(ax, P(10, 5), P(14, 17), 'varie', lw=1.8)
arrow(ax, P(0, 0), P(14, 17), 'resultat', lw=1.8)
disc(ax, *P(10, 5), 0.9, 'fixe')
text(ax, 57, 60, r'$5 \times (2, 1) = (10, 5)$', 'sujet', 's', ha='left')
text(ax, 57, 50, r'$4 \times (1, 3) = (4, 12)$', 'varie', 's', ha='left')
text(ax, 57, 40, r'$(10, 5) + (4, 12)$', 'encre', 's', ha='left')
text(ax, 57, 33, r'$= (14, 17)$', 'resultat', 'm', ha='left', weight='bold')
text(ax, P(10, 5)[0] + 1.5, P(10, 5)[1] - 3.5, '(10, 5)', 'fixe', 's', ha='left')
save(fig, '58-206')
