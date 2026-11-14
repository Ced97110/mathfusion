import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(74)
text(ax, 44, 69, 'code (7, 4)', 'sujet', 'l')
box(ax, 8, 12, 72, 52, 'sujet', fill=False, dash=True)
brow(fig, ax, 44, 52, '1100101', role='sujet')
brow(fig, ax, 44, 30, '1110010', role='sujet')
arrow(ax, (44, 47), (44, 35), 'varie')
text(ax, 48, 41, 'décalage', 'varie', 's', ha='left')
text(ax, 44, 19, 'et encore…', 'fixe', 's')
text(ax, 44, 5, 'toujours dans le code', 'resultat', 'm')
save(fig, '68-184')
