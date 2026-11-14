import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 54, r'départ $X$', 'sujet', 'm', ha='left')
text(ax, 4, 24, r'ajoutées $X^{\prime}$', 'autre', 'm', ha='left')
for x, a, b in [(18, r'$x$', r'$x^{\prime}$'), (46, r'$y$', r'$y^{\prime}$')]:
    box(ax, x, 38, 14, 10, 'sujet', label=a)
    box(ax, x, 6, 14, 10, 'autre', label=b)
    arrow(ax, (x + 7, 37.5), (x + 7, 16.5), 'varie')
text(ax, 80, 43, '2 lettres', 'sujet', 's'); text(ax, 80, 11, '+ 2 lettres', 'autre', 's')
text(ax, 80, 27, '= 4', 'resultat', 'l')
text(ax, 28, 27, 'sans lien', 'varie', 's', ha='left')
save(fig, '49-041')
