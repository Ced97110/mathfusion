import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 20, 58, r'$R = \mathbb{Z}$', 'fixe'); text(ax, 68, 58, r'$R/I$', 'fixe')
box(ax, 6, 38, 28, 14, 'sujet', label='8 ∈ I', size='m'); box(ax, 6, 14, 28, 14, 'fixe', label='5 ∉ I', size='m')
box(ax, 54, 38, 28, 14, 'sujet', label='classe 0 = I', size='s'); box(ax, 54, 14, 28, 14, 'fixe', label='classe de 1', size='s')
arrow(ax, (34, 45), (54, 45), 'varie'); arrow(ax, (34, 21), (54, 21), 'varie')
text(ax, 44, 49, r'$\nu$', 'varie'); text(ax, 44, 25, r'$\nu$', 'varie')
text(ax, 44, 4, r'$\ker\,\nu = I$', 'resultat', 'l', weight='bold')
save(fig, '52-150')
