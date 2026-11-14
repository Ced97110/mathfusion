import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
disc(ax, 44, 50, 2.4, 'fixe')
text(ax, 44, 56.5, 'un seul point P', 'encre', 'm')
box(ax, 2, 18, 36, 18, 'sujet', label='distance et angle\n40 km ; 30°')
box(ax, 50, 18, 36, 18, 'autre', label='deux distances\nest, nord')
arrow(ax, (42, 48), (20, 36), 'sujet')
arrow(ax, (46, 48), (68, 36), 'autre')
arrow(ax, (39.5, 27), (48.5, 27), 'varie', both=True)
brace(ax, 2, 86, 16, 'varie', label='comment convertir ?', down=True)
save(fig, '39-002')
