import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(88)
box(ax, 4, 72, 44, 12, 'sujet', label=r'$y=mx+b$', size='l')
arrow(ax, (26, 71), (26, 60), 'varie'); text(ax, 30, 65.5, r'$x$ devient 0', 'varie', 's', ha='left')
box(ax, 4, 46, 44, 12, 'fixe', label=r'$y=m\times0+b$', size='l')
arrow(ax, (26, 45), (26, 34), 'varie'); text(ax, 30, 39.5, r'$m\times0=0$', 'varie', 's', ha='left')
box(ax, 4, 20, 44, 12, 'resultat', label=r'$y=b$', size='l')
text(ax, 26, 12, r'le point $(0,\ b)$ est sur l’axe', 'resultat', 's')
box(ax, 56, 22, 30, 52, 'fixe', fill=False, dash=True)
text(ax, 71, 68, 'cas', 'fixe', 's'); text(ax, 71, 56, r'$y=2x+1$', 'fixe', 's')
text(ax, 71, 46, r'$x=0$', 'varie', 's'); text(ax, 71, 36, r'$2\times0+1$', 'fixe', 's'); text(ax, 71, 26, r'$y=1$', 'resultat', 's')
save(fig, '19-088')
