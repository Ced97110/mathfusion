import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 3, 56, 32, 11, 'sujet', label='n premier impair', size='s')
arrow(ax, (35, 61.5), (53, 61.5), 'resultat', lw=1.4)
text(ax, 44, 65.5, 'toujours', 'resultat', 's')
box(ax, 53, 56, 32, 11, 'resultat', label='reste 1', size='s')
box(ax, 3, 30, 32, 11, 'resultat', label='reste 1', size='s')
arrow(ax, (35, 35.5), (53, 35.5), 'limite', lw=1.4)
text(ax, 44, 39.5, 'pas toujours', 'limite', 's')
text(ax, 44, 35.5, '✗', 'limite', 'l') if False else None
box(ax, 53, 30, 32, 11, 'sujet', label='n premier', size='s')
line(ax, [(44, 35.5), (44, 20)], 'limite', dash=True)
box(ax, 14, 6, 60, 14, 'limite', label='341 = 11 × 31 : reste 1', size='m')
text(ax, 44, 1.5, 'contre-exemple', 'limite', 's') if False else None
save(fig, '53-182')
