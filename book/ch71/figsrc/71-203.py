import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 3, 24, 34, 28, 'sujet'); box(ax, 51, 24, 34, 28, 'autre')
text(ax, 20, 47, r'$x^2+y^2$', 'sujet', 'm'); text(ax, 68, 47, r'$x^2-y^2$', 'autre', 'm')
text(ax, 20, 38, r'en $(3,2i)$ :', 'sujet', 's'); text(ax, 68, 38, r'en $(3,2)$ :', 'autre', 's')
text(ax, 20, 30, r'$9-4=5$', 'sujet', 'm'); text(ax, 68, 30, r'$9-4=5$', 'autre', 'm')
arrow(ax, (38, 38), (50, 38), 'varie', lw=1.3); text(ax, 44, 43, r'$y\to iy$', 'varie', 's')
box(ax, 14, 4, 60, 11, 'resultat'); text(ax, 44, 9.5, 'même valeur : le signe ne compte plus', 'resultat', 's')
save(fig, '71-203')
