import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$ab = ac$ et $a \neq 0$', 'encre', 'm')
# deux produits de même premier facteur a
box(ax, 6, 48, 13, 12, 'sujet', label=r'$a$', size='l'); box(ax, 21, 48, 13, 12, 'varie', label=r'$b$', size='l')
text(ax, 44, 54, r'$=$', 'encre', 'l')
box(ax, 54, 48, 13, 12, 'sujet', label=r'$a$', size='l'); box(ax, 69, 48, 13, 12, 'varie', label=r'$c$', size='l')
text(ax, 20, 64, 'a fois b', 'fixe', 's'); text(ax, 68, 64, 'a fois c', 'fixe', 's')
text(ax, 12.5, 43.5, 'facteur commun', 'sujet', 's') if False else None
arrow(ax, (44, 42), (44, 31), 'varie')
text(ax, 62, 36.5, 'on retire a', 'varie', 's')
box(ax, 26, 18, 36, 12, 'resultat', label=r'$b = c$', size='l')
line(ax, [(6, 10), (82, 10)], 'fixe', lw=0.5)
text(ax, 44, 5, r'$3 \times b = 3 \times 5$ donne $b = 5$', 'fixe', 's')
save(fig, '51-106')
