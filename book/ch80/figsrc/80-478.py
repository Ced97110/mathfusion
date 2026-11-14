import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
u = 72 / 600
text(ax, 44, 51, 'même gain à grande échelle', 'encre', 'm') if False else None
box(ax, 8, 32, 600 * u, 10, 'sujet', label='600 interrupteurs')
box(ax, 8, 12, 100 * u, 10, 'resultat')
box(ax, 8 + 100 * u, 12, 500 * u, 10, 'varie', fill=False, dash=True, label='500 en moins')
text(ax, 8 + 6 * u * 0 + 6, 7, '100', 'resultat', 's')
text(ax, 48, 49, 'avant', 'sujet', 's') if False else None
text(ax, 44, 50, 'avant : 600', 'sujet', 's', ha='center') if False else None
text(ax, 44, 2.5, 'moins de place, de coût, de chaleur', 'encre', 's') if False else None
text(ax, 44, 47, 'avant', 'sujet', 's'); text(ax, 44, 27.5, 'après', 'resultat', 's')
save(fig, '80-478')
