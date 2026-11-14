import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 12, 48, r'$\beta$', 'autre', 'l'); text(ax, 20, 48, r'$\circ$', 'fixe', 'l'); text(ax, 28, 48, r'$\alpha$', 'varie', 'l')
text(ax, 41, 48, '=', 'encre', 'l')
text(ax, 56, 48, r'$\beta$', 'autre', 'l'); text(ax, 64, 48, r'$\alpha$', 'varie', 'l')
text(ax, 52, 38, 'ensuite', 'autre', 's'); text(ax, 70, 38, 'd’abord', 'varie', 's')
arrow(ax, (70, 33), (52, 33), 'encre')
text(ax, 62, 22, 'se lit de droite à gauche', 'sujet', 'm')
save(fig, '44-037')
