import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 20, 65, 'expression', 'sujet', 'm'); text(ax, 62, 65, 'équation', 'autre', 'm')
box(ax, 6, 48, 28, 10, 'sujet', label=r'$x+1$'); box(ax, 40, 48, 44, 10, 'autre', label=r'$x+1=5$')
text(ax, 20, 40, 'ni vrai ni faux', 'fixe', 's')
box(ax, 40, 20, 20, 9, 'resultat', label=r'$x=4$'); box(ax, 64, 20, 20, 9, 'limite', label=r'$x=2$')
arrow(ax, (50, 47), (50, 30.5), 'fixe'); arrow(ax, (74, 47), (74, 30.5), 'fixe')
text(ax, 50, 14, 'vrai', 'resultat', 'm', weight='bold'); text(ax, 74, 14, 'faux', 'limite', 'm', weight='bold')
save(fig, '15-018')
