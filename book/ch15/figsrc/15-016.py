import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 6, 30, 22, 11, 'fixe', label='8', size='l', weight='bold'); text(ax, 17, 46, 'nombre seul', 'fixe', 's')
arrow(ax, (30, 35.5), (52, 35.5), 'varie'); text(ax, 41, 40, '+ 0', 'varie', 'm')
box(ax, 54, 30, 28, 11, 'sujet', label='8 + 0', size='l', weight='bold'); text(ax, 68, 46, 'expression', 'sujet', 's')
disc(ax, 44, 10, 6, 'resultat', label='8', size='l')
arrow(ax, (17, 29), (38, 13), 'resultat'); arrow(ax, (68, 29), (50, 13), 'resultat')
text(ax, 44, 20, 'même valeur', 'resultat', 's')
save(fig, '15-016')
