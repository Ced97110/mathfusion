import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(66)
text(ax, 22, 61, 'listes', 'sujet', 'm', weight='bold')
text(ax, 66, 61, 'fonctions', 'autre', 'm', weight='bold')
line(ax, [(44, 22), (44, 63)], 'fixe', lw=0.6, dash=True)
# listes
for i, l in enumerate([r'$u_1$', r'$u_2$', r'$u_3$']):
    box(ax, 4 + i * 12.5, 38, 12.5, 9, 'sujet', label=l, size='s')
text(ax, 10.25, 51.5, 'case 1', 'varie', 's')
text(ax, 22.75, 51.5, 'case 2', 'fixe', 's')
box(ax, 4, 38, 12.5, 9, 'varie', fill=False, lw=1.4)
# fonctions
xs = np.linspace(0, 36, 50)
cx, cy = 50, 38
line(ax, [(cx + x, cy + 4 + 4 * np.sin(x / 36 * 6)) for x in xs], 'autre', lw=1.3)
for x, lab, role in [(8, 'point 1', 'varie'), (26, 'point 2', 'fixe')]:
    yy = cy + 4 + 4 * np.sin(x / 36 * 6)
    disc(ax, cx + x, yy, 1.1, role)
    line(ax, [(cx + x, cy - 1), (cx + x, yy)], role, lw=0.4, dash=True)
text(ax, cx + 8, cy - 4, 'point 1', 'varie', 's')
text(ax, cx + 26, cy - 4, 'point 2', 'fixe', 's')
# vers un calcul sur des nombres
arrow(ax, (10.25, 37), (36, 21.5), 'varie', lw=1.1)
arrow(ax, (cx + 8, cy - 7), (52, 21.5), 'varie', lw=1.1)
box(ax, 14, 8, 60, 13, 'resultat', label='un calcul sur des nombres', size='s')
save(fig, '58-106')
