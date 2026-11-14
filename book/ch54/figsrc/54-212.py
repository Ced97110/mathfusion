import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# polynôme de départ et sa courbe au-dessus de l'axe
box(ax, 2, 62, 38, 11, 'sujet', label=r'$x^4+4$', size='l')
ax0, ay0 = 67.0, 62.0
line(ax, [(50, ay0), (84, ay0)], 'fixe', lw=1.6)
pts = [(ax0 + t * 11, ay0 + (t ** 4 + 4) * 0.9) for t in [i / 20 - 1.4 for i in range(57)]]
line(ax, pts, 'sujet', lw=1.4)
text(ax, 67, 57.5, 'aucune racine réelle', 'sujet', 's')
text(ax, 21, 56, '=', 'encre', 'xl')
box(ax, 2, 38, 38, 10, 'autre', label=r'$x^2-2x+2$', size='m')
text(ax, 44, 43, '×', 'encre', 'xl')
box(ax, 48, 38, 38, 10, 'autre', label=r'$x^2+2x+2$', size='m')
text(ax, 44, 29, 'vérification en x = 2', 'encre', 's')
box(ax, 2, 6, 38, 13, 'sujet', label=r'$16+4=20$', size='m')
box(ax, 48, 6, 38, 13, 'autre', label=r'$2\times10=20$', size='m')
text(ax, 44, 12.5, '=', 'resultat', 'xl', weight='bold')
save(fig, '54-212')
