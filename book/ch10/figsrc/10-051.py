import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 3.0; x0 = 8
text(ax, 44, 76, 'Estimation : un autre nombre', 'varie', 'm')
box(ax, x0, 60, 23 * u, 8, 'sujet', label='23')
arrow(ax, (x0 + 10 * u, 59), (x0 + 10 * u, 53), 'varie')
box(ax, x0, 44, 20 * u, 8, 'varie', label='20')
box(ax, x0 + 20 * u, 44, 3 * u, 8, 'limite', fill=False, dash=True, label='3', size='s')
text(ax, x0 + 21.5 * u, 40, 'perdu', 'limite', 's')
text(ax, 44, 30, 'Distributivité : même nombre', 'resultat', 'm')
box(ax, x0, 14, 20 * u, 8, 'sujet', label='20')
box(ax, x0 + 20 * u, 14, 3 * u, 8, 'sujet', label='3', size='s')
text(ax, 44, 8, r'$23 = 20 + 3$ : rien perdu', 'resultat', 's')
save(fig, '10-051')
