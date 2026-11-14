import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 22, 48, 'polygone', 'sujet', 'm', weight='bold'); text(ax, 66, 48, 'cercle', 'limite', 'm', weight='bold')
poly(ax, [(8, 18), (36, 18), (36, 40), (8, 40)], 'sujet', lw=1.2)
arrow(ax, (22, 8), (22, 17), 'varie'); text(ax, 22, 5, 'côtés : segments droits', 'sujet', 's')
disc(ax, 66, 29, 11, 'limite', lw=1.2)
arrow(ax, (66, 8), (66, 17), 'varie'); text(ax, 66, 5, 'aucun segment', 'limite', 's')
save(fig, '11-075')
