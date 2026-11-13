import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u, ox, oy = 10.0, 30, 14
box(ax, ox, oy, 4 * u, 3 * u, 'sujet', r=0.3)
line(ax, [(ox, oy), (ox + 4 * u, oy + 3 * u)], 'fixe', dash=True)
arrow(ax, (ox, oy - 3), (ox + 4 * u, oy - 3), 'varie'); arrow(ax, (ox - 3, oy), (ox - 3, oy + 3 * u), 'varie')
text(ax, ox + 2 * u, oy - 7, 'avancer de 4', 'varie', 's'); text(ax, ox - 5, oy + 1.5 * u, 'monter de 3', 'varie', 's', ha='right')
disc(ax, ox, oy, 1.0, 'fixe'); disc(ax, ox + 4 * u, oy + 3 * u, 1.4, 'resultat')
text(ax, ox + 3.5, oy + 3.5, r'$O$', 'fixe', 'm'); text(ax, ox + 4 * u - 3.5, oy + 3 * u + 4, r'$P$', 'resultat', 'l', weight='bold')
text(ax, ox + 4 * u - 8, oy + 3 * u + 10, 'coin opposé', 'resultat', 's')
save(fig, '09-016')
