import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
O = (16, 32); r = 14
disc(ax, *O, r, 'fixe', fill=False)
arrow(ax, O, (84, 32), 'sujet', lw=1.2)
arrow(ax, (2, 46), (84, 46), 'autre', lw=1.2)
disc(ax, 16 + r, 32, 1.0, 'sujet'); disc(ax, 16, 46, 1.0, 'fixe'); disc(ax, *O, 1.0, 'fixe')
text(ax, 12.5, 29.5, 'O', 'encre', 's'); text(ax, 30, 28.5, 'A = P', 'encre', 's'); text(ax, 12.5, 49, 'B', 'encre', 's')
text(ax, 62, 49.5, 'tangente en B', 'autre', 's'); text(ax, 62, 28.5, 'demi-droite OP', 'sujet', 's')
text(ax, 22, 11, 'sin 0° = 0', 'encre', 's'); text(ax, 66, 11, 'pas de point S', 'limite', 's')
text(ax, 22, 4, 'cosec 0° = 1/0', 'limite', 's'); text(ax, 66, 4, 'cotan 0° = cos 0°/0', 'limite', 's')
save(fig, '31-102')
