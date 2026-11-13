import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 36, 66, 'M', 'sujet', 'l', weight='bold'); text(ax, 41, 66, '(', 'fixe', 'l'); text(ax, 46, 66, 'S', 'varie', 'l', weight='bold'); text(ax, 51, 66, ')', 'fixe', 'l')
text(ax, 24, 46, 'toutes les transformations', 'sujet', 's'); text(ax, 68, 46, 'l’ensemble de départ', 'varie', 's')
arrow(ax, (35, 62), (27, 50), 'sujet'); arrow(ax, (47, 62), (63, 50), 'varie')
text(ax, 16, 24, r'$S = \{1, 2\}$', 'varie', 'm'); text(ax, 64, 24, r'$M(\{1, 2\})$', 'sujet', 'm')
text(ax, 16, 8, r'$S = \{1, 2, 3\}$', 'varie', 'm'); text(ax, 64, 8, r'$M(\{1, 2, 3\})$', 'sujet', 'm')
arrow(ax, (31, 24), (47, 24), 'fixe'); arrow(ax, (31, 8), (47, 8), 'fixe'); text(ax, 64, 16, r'$\neq$', 'limite', 'm')
save(fig, '44-045')
