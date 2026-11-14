import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 76 / 44.0
brace(ax, 6, 82, 42, 'fixe', label='44 € cette année', down=False)
box(ax, 6, 30, 41 * u, 10, 'sujet', label=r'$x$ : prix de l’an dernier', size='s')
box(ax, 6 + 41 * u, 30, 3 * u, 10, 'varie', label='3', size='s')
arrow(ax, (82 - 1.5 * u, 29), (60, 22), 'varie', curve=-0.2); text(ax, 36, 22, 'retirer 3 €', 'varie', 'm')
box(ax, 14, 4, 60, 10, 'resultat', label=r'$x=44-3=41$')
save(fig, '16-063')
