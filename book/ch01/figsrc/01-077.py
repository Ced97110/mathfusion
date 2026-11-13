import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(86)
U = 15 / 1000  # mm par unité : 15 mm pour 1 000
L4000, L300 = 4000 * U, 300 * U  # 60 mm et 4,5 mm
n4000 = '4' + NB + '000'
text(ax, 44, 78, '+', 'sujet', 'l', weight='bold')
text(ax, 44, 66, 'met ensemble', 'sujet', 's')
line(ax, [(44, 74), (44, 69)], 'sujet', lw=0.6)
text(ax, 22, 78, n4000, 'fixe', 'l', weight='bold')
text(ax, 22, 66, 'entrepôt 1', 'fixe', 's')
line(ax, [(22, 74), (22, 69)], 'fixe', lw=0.6)
text(ax, 64, 78, '300', 'fixe', 'l', weight='bold')
text(ax, 64, 66, 'entrepôt 2', 'fixe', 's')
line(ax, [(64, 74), (64, 69)], 'fixe', lw=0.6)
# avant
box(ax, 4, 46, L4000, 7, 'fixe', label=n4000, size='s', r=0.3)
box(ax, 72, 46, L300, 7, 'autre', r=0.3)
text(ax, 82, 49.5, '300', 'autre', 's')
arrow(ax, (44, 43), (44, 33), 'varie')
# après
box(ax, 4, 23, L4000, 7, 'fixe', r=0.3)
box(ax, 4 + L4000, 23, L300, 7, 'autre', r=0.3)
box(ax, 3, 22, 66.5, 9, 'resultat', fill=False, r=0.3)
text(ax, 36, 16, 'ensemble : 4' + NB + '300', 'resultat', 'm', weight='bold')
text(ax, 44, 6, n4000 + ' + 300 + 20 + 9 = 4' + NB + '329', 'fixe', 's')
save(fig, '01-077')
