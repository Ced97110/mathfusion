import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
D = 14
text(ax, 44, 67 + D, r'$f$ : élève $\to$ note', 'encre', 'm')
for i, y in enumerate((54, 40, 26)):
    box(ax, 4, y + D, 26, 10, 'sujet', label=f'élève {i + 1}', size='s'); arrow(ax, (30, y + 5 + D), (58, 45 + D), 'varie')
box(ax, 4, 8 + D, 26, 10, 'autre', label='élève 4', size='s'); arrow(ax, (30, 13 + D), (58, 13 + D), 'fixe')
box(ax, 58, 40 + D, 26, 10, 'resultat', label='une note', size='s'); box(ax, 58, 8 + D, 26, 10, 'fixe', label='une autre note', size='s')
text(ax, 44, 59 + D - 17, r'$f$', 'varie', 'm')
line(ax, [(4, 14), (84, 14)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 9, 'même note : la relation repose sur $=$', 'resultat', 's')
text(ax, 44, 3.5, 'toujours une équivalence', 'resultat', 's', weight='bold')
save(fig, '43-039')
