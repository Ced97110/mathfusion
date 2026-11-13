import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 5, 82, 48, 'sujet'); text(ax, 44, 48, 'positifs : à droite de 0', 'sujet', 'm')
box(ax, 8, 9, 32, 33, 'autre'); text(ax, 24, 37, 'naturels : on compte', 'autre', 's')
text(ax, 24, 23, '3', 'autre', 'xl')
text(ax, 55, 28, '1/2', 'sujet', 'l'); text(ax, 73, 28, 'π', 'sujet', 'l')
save(fig, '12-062')
