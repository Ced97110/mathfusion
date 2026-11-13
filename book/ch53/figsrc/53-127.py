import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(100)
# fabrication des clés
box(ax, 2, 84, 28, 10, 'autre', label='5 et 11')
arrow(ax, (31, 89), (43, 89), 'varie')
box(ax, 44, 84, 40, 10, 'fixe', label='55 et 40')
arrow(ax, (64, 83.5), (64, 65), 'varie')
box(ax, 40, 14, 46, 50, 'fixe', fill=False, dash=True)
box(ax, 44, 40, 38, 14, 'sujet', label='clé publique\n55 et 3', size='s')
box(ax, 44, 19, 38, 14, 'autre', label='clé privée\n27', size='s')
# chiffrement puis déchiffrement, vers le bas
box(ax, 2, 52, 24, 10, 'sujet', label='8')
box(ax, 2, 32, 24, 10, 'varie', label='17')
box(ax, 2, 12, 24, 10, 'resultat', label='8')
arrow(ax, (14, 51.5), (14, 42.5), 'sujet', lw=1.6)
arrow(ax, (14, 31.5), (14, 22.5), 'autre', lw=1.6)
line(ax, [(15.5, 47), (44, 47)], 'sujet', dash=True)
line(ax, [(15.5, 27), (44, 27)], 'autre', dash=True)
text(ax, 29, 50, 'chiffrer', 'sujet', 's')
text(ax, 29, 30, 'déchiffrer', 'autre', 's')
save(fig, '53-127')
