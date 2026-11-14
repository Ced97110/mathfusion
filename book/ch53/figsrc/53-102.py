import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'Nombre privé d’Alice', 'encre', 'm')
box(ax, 6, 36, 24, 13, 'sujet', label=r'$d$', size='xl')
text(ax, 38, 42.5, '=', 'encre', 'l')
box(ax, 46, 36, 24, 13, 'fixe', label='27', size='l', dash=True)
text(ax, 76, 42.5, 'privé', 'sujet', 's')
arrow(ax, (18, 34), (18, 22), 'varie')
text(ax, 18, 27.5, 'sert à', 'varie', 's', ha='left') if False else None
box(ax, 6, 8, 24, 13, 'autre', label=r'$c^{d}$', size='l')
text(ax, 38, 14.5, '=', 'encre', 'l')
box(ax, 46, 8, 24, 13, 'resultat', label=r'$17^{27}$', size='l')
text(ax, 76, 14.5, 'si c = 17', 'encre', 's')
save(fig, '53-102')
