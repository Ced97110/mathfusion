import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
disc(ax, 30, 32, 28, 'autre'); disc(ax, 22, 28, 12.5, 'sujet')
text(ax, 22, 31, 'corps de', 'sujet', 's'); text(ax, 22, 26, 'décomposition', 'sujet', 's')
text(ax, 22, 12, 'un polynôme', 'sujet', 's')
text(ax, 73, 40, 'clôture', 'autre', 's'); text(ax, 73, 35, 'algébrique :', 'autre', 's'); text(ax, 72, 30, 'tous les', 'autre', 's'); text(ax, 72, 25, 'polynômes', 'autre', 's')
line(ax, [(58, 32), (62.5, 32)], 'autre')
save(fig, '61-251')
