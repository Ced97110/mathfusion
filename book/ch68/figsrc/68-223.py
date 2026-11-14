import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(90)
text(ax, 44, 86, 'débit = bits utiles sur bits envoyés', 'encre', 's', weight='bold')
x0, y0, xl = 12, 36, 52
arrow(ax, (x0, y0), (82, y0), 'fixe')
arrow(ax, (x0, y0), (x0, 78), 'fixe')
text(ax, 82, y0 - 4, 'débit', 'fixe', 's', ha='right')
text(ax, x0 + 1, 80.5, 'probabilité d’erreur', 'fixe', 's', ha='left')
line(ax, [(x0 + 1, y0 + 3), (xl, y0 + 3)], 'resultat', lw=2.0)
ax.add_patch(Rectangle((x0, y0), xl - x0, 22, fc=FILL['resultat'], ec='none', alpha=0.5, zorder=1))
line(ax, [(xl, y0 - 2), (xl, 78)], 'varie', lw=1.2, dash=True)
text(ax, xl, y0 - 4, 'limite fixée\npar le bruit', 'varie', 's')
box(ax, 14, 41, 28, 12, 'resultat', fill=False, dash=True, label='erreur aussi petite\nqu’on veut', size='s')
box(ax, 4, 14, 38, 10, 'resultat', label='il existe de tels codes', size='s')
box(ax, 46, 14, 38, 10, 'fixe', fill=False, dash=True, label='comment les construire ?\nnon dit', size='s')
save(fig, '68-223')
