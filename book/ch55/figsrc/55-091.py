import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'$x_1^2x_2\;+\;x_1x_2^2$', 'sujet', 'l')
xa, xb, w, y, h = 8, 52, 28, 22, 13
box(ax, xa, y, w, h, 'resultat', label=r'$(2,\,1)$', size='l', weight='bold')
box(ax, xb, y, w, h, 'fixe', label=r'$(1,\,2)$', size='l')
arrow(ax, (36, 46), (xa + w / 2, y + h), 'fixe')
arrow(ax, (52, 46), (xb + w / 2, y + h), 'fixe')
text(ax, 44, y + h / 2, r'$2>1$', 'resultat', 'l', weight='bold')
text(ax, xa + w / 2, 15, r'$x_1^2x_2$', 'resultat', 'm')
text(ax, xb + w / 2, 15, r'$x_1x_2^2$', 'fixe', 'm')
text(ax, xa + w / 2, 7, 'le plus haut', 'resultat', 'm', weight='bold')
text(ax, xb + w / 2, 7, 'plus bas', 'fixe', 'm')
save(fig, '55-091')
