import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
u = 2.6; x0 = 6
text(ax, 44, 87, r'$23 = 20 + 3$', 'sujet', 'm')
box(ax, x0, 72, 20 * u, 8, 'varie', label='20')
box(ax, x0 + 20 * u, 72, 3 * u, 8, 'autre', label='3', size='s')
text(ax, 44, 65, r'$25 \times 20 + 25 \times 3 = 500 + 75 = 575$', 'resultat', 's')
text(ax, 44, 53, r'$23 = 30 - 7$', 'sujet', 'm')
box(ax, x0, 38, 23 * u, 8, 'sujet', label='23')
box(ax, x0 + 23 * u, 38, 7 * u, 8, 'varie', fill=False, dash=True, label=r'$-7$', size='s')
brace(ax, x0, x0 + 30 * u, 38, 'fixe', label='30')
text(ax, 44, 24, r'$25 \times 30 - 25 \times 7 = 750 - 175 = 575$', 'resultat', 's')
text(ax, 44, 12, 'même résultat, coupure au choix', 'encre', 's')
save(fig, '10-063')
