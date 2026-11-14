import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, u = 8, 8, 6.0
line(ax, [(ox, oy), (ox + 6.5 * u, oy)], 'fixe'); line(ax, [(ox, oy), (ox, oy + 4.8 * u)], 'fixe')
arrow(ax, (ox, oy), (ox + 3 * u, oy + 4 * u), 'sujet', lw=1.4)
arrow(ax, (ox, oy), (ox + 5 * u, oy), 'autre', lw=1.4)
text(ax, ox + 3 * u - 2, oy + 4 * u + 3.5, r'$x=(3,\,4)$', 'sujet', 's')
text(ax, ox + 5 * u - 2, oy + 4, r'$y=(5,\,0)$', 'autre', 's')
text(ax, 62, 46, 'produit des premières', 'sujet', 's'); text(ax, 62, 41.5, r'$3\times5=15$', 'sujet', 's')
text(ax, 62, 33, 'produit des secondes', 'autre', 's'); text(ax, 62, 28.5, r'$4\times0=0$', 'autre', 's')
line(ax, [(46, 22.5), (80, 22.5)], 'fixe')
text(ax, 62, 17, r'$\langle x,y\rangle=15+0$', 'resultat', 'm', weight='bold')
save(fig, '73-076')
