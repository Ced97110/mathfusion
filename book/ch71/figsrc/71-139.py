import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
box(ax, 3, 42, 30, 14, 'sujet', label=r'$x\perp y$', size='l')
text(ax, 44, 49, r'$\Leftrightarrow$', 'encre', 'l')
box(ax, 55, 42, 30, 14, 'resultat', label=r'$B(x,y)=0$', size='m')
o = (34, 8)
arrow(ax, o, (o[0] + 22, o[1]), 'sujet', lw=1.5); arrow(ax, o, (o[0], o[1] + 22), 'autre', lw=1.5)
line(ax, [(o[0] + 3, o[1]), (o[0] + 3, o[1] + 3), (o[0], o[1] + 3)], 'fixe')
text(ax, o[0] + 25, o[1] + 1, r'$x$', 'sujet', 'm'); text(ax, o[0] + 3, o[1] + 25, r'$y$', 'autre', 'm')
text(ax, 18, 22, 'produit scalaire', 'fixe', 's')
save(fig, '71-139')
