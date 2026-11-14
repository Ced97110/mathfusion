import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 14, 50, '0', 'sujet', 'xl', weight='bold')
text(ax, 30, 50, '=', 'encre', 'xl')
text(ax, 58, 50, r'$\langle 0;\ 0\rangle$', 'sujet', 'xl')
# chaque morceau relié à son sens
box(ax, 2, 24, 26, 10, 'sujet', label='un seul signe', size='s')
arrow(ax, (14, 34), (14, 44), 'sujet', lw=0.9)
box(ax, 40, 24, 36, 10, 'sujet', label='deux composantes nulles', size='s')
arrow(ax, (58, 34), (58, 44), 'sujet', lw=0.9)
text(ax, 44, 59, 'le vecteur nul', 'sujet', 'm')
box(ax, 2, 4, 84, 11, 'resultat', label=r'$v+0=v$   au lieu d’une phrase', size='m')
save(fig, '41-059')
