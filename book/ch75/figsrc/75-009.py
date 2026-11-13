import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, 'nombres réels', 'fixe', 'm'); text(ax, 66, 56, 'corps à 2 éléments', 'sujet', 'm')
poly(ax, [(6, 14), (38, 14), (38, 46), (6, 46)], 'fixe')
for i in range(9):
    for j in range(9):
        disc(ax, 8 + i * 3.5, 16 + j * 3.5, 0.5, 'fixe')
text(ax, 22, 8, 'une infinité de points', 'fixe', 's')
ox, oy, u = 54, 14, 24
arrow(ax, (ox, oy), (ox + u + 8, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, oy + u + 8), 'fixe', lw=0.8)
for i in (0, 1):
    for j in (0, 1): disc(ax, ox + i * u, oy + j * u, 2, 'sujet')
text(ax, ox, oy - 3.5, '0', 'fixe', 's'); text(ax, ox + u, oy - 3.5, '1', 'fixe', 's')
text(ax, ox - 3, oy + u, '1', 'fixe', 's'); text(ax, ox - 3, oy, '0', 'fixe', 's')
text(ax, 66, 8, '4 points : on les compte', 'sujet', 's')
save(fig, '75-009')
