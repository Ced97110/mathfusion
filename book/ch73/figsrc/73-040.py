import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
poly(ax, [(4, 28), (12, 28), (12, 36), (4, 36)], 'sujet'); text(ax, 8, 24, 'carré : aire 1', 'sujet', 's')
poly(ax, [(34, 46), (50, 46), (50, 54), (34, 54)], 'varie'); text(ax, 42, 42, 'largeurs ×2 : aire 2', 'varie', 's')
poly(ax, [(38, 4), (46, 4), (46, 20), (38, 20)], 'varie'); text(ax, 54, 12, 'hauteurs ×2:\naire 2', 'varie', 's', ha='left')
arrow(ax, (13, 36), (33, 49), 'varie'); arrow(ax, (13, 28), (37, 15), 'varie')
box(ax, 60, 26, 26, 14, 'resultat', label='même classe :\ndet 2', size='s')
arrow(ax, (51, 50), (66, 41), 'resultat', curve=0.0); arrow(ax, (59, 18), (70, 25), 'resultat')
save(fig, '73-040')
