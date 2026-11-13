import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
disc(ax, 16, 14, 12, 'fixe', fill=False)
arrow(ax, (16, 14), (16, 60), 'sujet', lw=1.2)
arrow(ax, (28, 4), (28, 60), 'autre', lw=1.2)
disc(ax, 16, 26, 1.0, 'sujet'); disc(ax, 28, 14, 1.0, 'fixe'); disc(ax, 16, 14, 1.0, 'fixe')
text(ax, 12.7, 11.5, 'O', 'encre', 's'); text(ax, 12.8, 26, 'P', 'encre', 's'); text(ax, 31.2, 11.5, 'A', 'encre', 's')
text(ax, 12.2, 46, 'demi-droite OP', 'sujet', 's', rot=90)
text(ax, 31.5, 56, 'tangente en A', 'autre', 's', ha='left')
text(ax, 33, 44, 'ne se rencontrent pas', 'limite', 's', ha='left')
text(ax, 33, 36, 'donc pas de point T', 'limite', 's', ha='left')
text(ax, 33, 26, r'sec 90° = 1/0 : impossible', 'limite', 's', ha='left')
save(fig, '31-099')
