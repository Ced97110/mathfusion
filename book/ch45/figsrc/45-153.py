import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 26, 68, r'$G$', 'sujet', 'xl'); text(ax, 44, 68, r'$\times$', 'varie', 'xl'); text(ax, 62, 68, r'$H$', 'autre', 'xl')
box(ax, 2, 36, 40, 14, 'sujet'); text(ax, 22, 43, '1re case : dans $G$', 'sujet', 's')
box(ax, 46, 36, 40, 14, 'autre'); text(ax, 66, 43, '2e case : dans $H$', 'autre', 's')
arrow(ax, (26, 63), (22, 51), 'sujet'); arrow(ax, (62, 63), (66, 51), 'autre')
arrow(ax, (44, 63), (44, 22), 'varie')
box(ax, 8, 6, 72, 16, 'resultat', label=r'groupe des couples $(g,h)$', size='m')
save(fig, '45-153')
