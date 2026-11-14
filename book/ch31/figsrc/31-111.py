import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(50)
text(ax, 44, 44, 'à démontrer : cos² x = 1 − sin² x', 'encre', 's')
box(ax, 3, 18, 24, 12, 'sujet', label='cos² x', size='m')
box(ax, 61, 18, 24, 12, 'resultat', label='1 − sin² x', size='m')
arrow(ax, (28.5, 24), (59.5, 24), 'varie', lw=1.3)
text(ax, 44, 29.5, 'cos² x + sin² x = 1', 'varie', 's')
text(ax, 44, 19, 'égalité justifiée', 'varie', 's')
text(ax, 15, 12, 'on part de là', 'sujet', 's'); text(ax, 73, 12, 'on s’arrête : c’est', 'resultat', 's')
text(ax, 73, 7, 'l’autre membre', 'resultat', 's')
save(fig, '31-111')
