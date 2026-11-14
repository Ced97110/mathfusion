import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 21, 70, r'primitif $\neq$ unitaire', 'varie', 'm', weight='bold')
text(ax, 67, 70, r'primitif $\neq$ irréductible', 'autre', 'm', weight='bold')
line(ax, [(44, 8), (44, 74)], 'fixe', dash=True)
# gauche : deux primitifs, coefficient de tête différent
box(ax, 4, 46, 36, 10, 'sujet', label=r'$2x^2+3x+5$')
text(ax, 22, 40, r'contenu $1$ ; tête $2$', 'varie', 's')
box(ax, 4, 22, 36, 10, 'sujet', label=r'$x^2+2x+4$')
text(ax, 22, 16, r'contenu $1$ ; tête $1$', 'varie', 's')
# droite : primitif qui se casse
box(ax, 48, 46, 36, 10, 'sujet', label=r'$x^2-1$')
text(ax, 66, 40, r'contenu $1$', 'sujet', 's')
arrow(ax, (66, 35), (66, 29), 'autre')
box(ax, 48, 18, 36, 10, 'autre', label=r'$(x-1)(x+1)$')
text(ax, 66, 12, 'mais il se casse', 'autre', 's')
save(fig, '56-144')
