import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# Ligne 1 : lettre ordinaire = nombre
text(ax, 18, 52, 'lettre ordinaire', 'fixe', 's')
box(ax, 6, 30, 24, 18, 'fixe', label=r'$m$', size='xl')
arrow(ax, (31, 39), (41, 39), 'fixe')
box(ax, 42, 30, 42, 18, 'fixe', label='un nombre : 5 kg', size='m')
# Ligne 2 : lettre en gras = vecteur
text(ax, 18, 24, 'lettre en gras', 'sujet', 's')
box(ax, 6, 2, 24, 18, 'sujet', label=r'$\mathbf{v}$', size='xl')
arrow(ax, (31, 11), (41, 11), 'sujet')
box(ax, 42, 2, 42, 18, 'sujet', label='nombre + direction', size='m')
save(fig, '41-020')
