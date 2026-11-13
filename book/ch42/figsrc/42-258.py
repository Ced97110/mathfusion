import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x, l in ((2, '(1, 1)'), (34, '(4, 7)'), (66, '(1, 1)')): box(ax, x, 40, 20, 9, 'fixe', label=l)
arrow(ax, (22, 44.5), (34, 44.5), 'autre'); text(ax, 28, 53, r'$T_A$', 'autre')
arrow(ax, (54, 44.5), (66, 44.5), 'sujet'); text(ax, 60, 53, r'$A^{-1}$', 'sujet')
box(ax, 2, 6, 34, 24, 'autre'); text(ax, 19, 21, r'$3\quad 1$', 'autre', 'l'); text(ax, 19, 13, r'$5\quad 2$', 'autre', 'l')
box(ax, 52, 6, 34, 24, 'sujet'); text(ax, 69, 21, r'$2\quad -1$', 'sujet', 'l'); text(ax, 69, 13, r'$-5\quad 3$', 'sujet', 'l')
text(ax, 19, 34, r'tableau $A$', 'autre', 's'); text(ax, 69, 34, r'tableau $A^{-1}$', 'sujet', 's')
save(fig, '42-258')
