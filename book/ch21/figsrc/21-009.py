import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 14, 34, r'$\frac{1}{6}$', 'varie', 'xl'); text(ax, 28, 34, '+', 'fixe', 'l'); text(ax, 42, 34, r'$\frac{1}{4}$', 'varie', 'xl')
text(ax, 56, 34, '=', 'fixe', 'l'); text(ax, 72, 34, r'$\frac{1}{x}$', 'autre', 'xl')
box(ax, 3, 24, 48, 20, 'varie', fill=False, dash=True); box(ax, 62, 24, 20, 20, 'autre', fill=False, dash=True)
text(ax, 27, 54, 'dénominateurs 6 et 4', 'varie', 's'); text(ax, 72, 54, r'$x$ en bas', 'autre', 's')
text(ax, 27, 14, 'chapitre 7', 'varie', 's'); text(ax, 72, 14, 'outil neuf', 'autre', 's')
arrow(ax, (27, 22.5), (27, 17.5), 'varie'); arrow(ax, (72, 22.5), (72, 17.5), 'autre')
save(fig, '21-009')
