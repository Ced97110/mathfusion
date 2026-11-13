import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 14, 10, 10
arrow(ax, (ox - 2, oy), (ox + 5.6 * u, oy), 'fixe'); arrow(ax, (ox, oy - 2), (ox, oy + 4.6 * u), 'fixe')
for i in range(1, 6): line(ax, [(ox + i * u, oy - 1), (ox + i * u, oy + 1)]); text(ax, ox + i * u, oy - 3.5, str(i), 'fixe', 's')
for j in range(1, 5): line(ax, [(ox - 1, oy + j * u), (ox + 1, oy + j * u)]); text(ax, ox - 3.5, oy + j * u, str(j), 'fixe', 's')
arrow(ax, (ox, oy), (ox + 3 * u - 0.5, oy), 'varie', lw=1.4); arrow(ax, (ox + 3 * u, oy), (ox + 3 * u, oy + 2 * u - 0.5), 'varie', lw=1.4)
text(ax, ox + 1.5 * u, oy + 3.5, 'avancer de 3', 'varie', 's'); text(ax, ox + 3 * u + 2, oy + u, 'monter de 2', 'varie', 's', ha='left')
disc(ax, ox + 3 * u, oy + 2 * u, 1.6, 'sujet'); text(ax, ox + 3 * u + 2, oy + 2 * u + 4, r'$P(3, 2)$', 'sujet', 'm', ha='left')
text(ax, ox - 3, oy - 3.5, r'$O$', 'encre', 's')
save(fig, '19-012')
