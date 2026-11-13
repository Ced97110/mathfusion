import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 22, 51, r'$\{a,b\}$', 'sujet', 'xl'); text(ax, 44, 51, '=', 'encre', 'xl'); text(ax, 66, 51, r'$\{b,a\}$', 'sujet', 'xl')
arrow(ax, (22, 46), (36, 34), 'varie'); arrow(ax, (66, 46), (52, 34), 'varie')
box(ax, 22, 9, 44, 25, 'resultat')
text(ax, 44, 29.5, 'un seul ensemble', 'resultat', 's')
disc(ax, 36, 17, 4.5, 'sujet', label=r'$a$'); disc(ax, 52, 15, 4.5, 'sujet', label=r'$b$')
text(ax, 44, 3.5, 'l’ordre vient de l’écriture', 'fixe', 's')
save(fig, '42-024')
