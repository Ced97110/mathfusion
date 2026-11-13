import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'les flèches (1, 2) et (3, 4)', 'encre', 'm')
box(ax, 2, 34, 24, 15, 'autre', label='mesure\nhabituelle', size='s')
text(ax, 58, 41.5, r'$1\times3\;+\;2\times4=11$', 'autre', 'm')
box(ax, 2, 14, 24, 15, 'sujet', label='seconde\nmesure', size='s')
text(ax, 58, 21.5, r'$1\times3\;-\;2\times4=-5$', 'sujet', 'm')
text(ax, 44, 5.5, r'seconde mesure de (1, 1) : $1-1=0$', 'resultat', 's')
save(fig, '72-017')
