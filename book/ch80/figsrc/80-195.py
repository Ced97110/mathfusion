import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 34
line(ax, [(6, y), (22, y)], 'fixe'); line(ax, [(34, y), (52, y)], 'fixe'); line(ax, [(64, y), (82, y)], 'fixe')
disc(ax, 6, y, 1.4, 'fixe'); disc(ax, 82, y, 1.4, 'fixe')
box(ax, 22, y - 6, 12, 12, 'sujet', label=r'$a$', size='l')
box(ax, 52, y - 6, 12, 12, 'varie', label=r'$b^{\prime}$', size='l')
text(ax, 28, y - 10, 'fermé', 'sujet', 's')
text(ax, 58, y - 10, 'fermé', 'varie', 's')
text(ax, 44, 52, r'position $(1,\ 0)$', 'encre', 'm')
arrow(ax, (28, 17), (28, 25), 'sujet') if False else None
text(ax, 28, 8, r'$a$ = 1 : fermé', 'sujet', 's')
text(ax, 60, 8, r'$b$ = 0 : ouvert', 'varie', 's')
text(ax, 44, 44, r'série : $a$, $b^{\prime}$', 'resultat', 'm')
save(fig, '80-195')
