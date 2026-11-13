import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'soit $x$ la largeur, en mètres', 'sujet', 'm')
u = 7
x0, y0 = 28, 20
poly(ax, [(x0, y0), (x0 + u * 7, y0), (x0 + u * 7, y0 + u * 3), (x0, y0 + u * 3)], 'fixe')
line(ax, [(x0, y0), (x0, y0 + u * 3)], 'sujet', lw=2.4)
line(ax, [(x0, y0), (x0 + u * 7, y0)], 'autre', lw=2.4)
text(ax, x0 - 3.5, y0 + 10.5, r'largeur : $x$', 'sujet', 's', rot=90)
text(ax, x0 + u * 3.5, y0 - 5, r'longueur : $x + 4$', 'autre', 's')
text(ax, x0 + u * 3.5, y0 + 10.5, 'jardin', 'fixe', 's')
save(fig, '16-106')
