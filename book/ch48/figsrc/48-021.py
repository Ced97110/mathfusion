import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 6, 38, 40, 'sujet', fill=True)
box(ax, 48, 6, 38, 40, 'autre', fill=True)
text(ax, 21, 41, r'$G$ : les entiers', 'sujet', 's'); text(ax, 67, 41, r"$G'$ : les positions", 'autre', 's')
text(ax, 21, 28, r'$ab$ : 5 + 9 = 14', 'sujet'); text(ax, 21, 16, 'addition ordinaire', 'sujet', 's')
text(ax, 67, 28, r"$f(a)f(b)$ : 1 + 1 = 2", 'autre'); text(ax, 67, 16, 'addition, reste ÷ 4', 'autre', 's')
arrow(ax, (14, 54), (74, 54), 'varie'); text(ax, 44, 58, r'$f$', 'varie', 'l')
save(fig, '48-021')
