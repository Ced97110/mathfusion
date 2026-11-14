import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'Trois nombres d’éléments', 'encre', 'm')
text(ax, 13, 62, r'$4=2^2$', 'resultat', 'l'); text(ax, 13, 55, 'un corps existe', 'resultat', 's')
for i in range(2):
    box(ax, 30 + i * 15, 52, 8, 10, 'resultat', label='2')
text(ax, 41.5, 57, '×', 'encre', 'm')
text(ax, 13, 38, r'$256=2^8$', 'resultat', 'l'); text(ax, 13, 31, 'un corps existe', 'resultat', 's')
for i in range(8):
    box(ax, 26 + i * 7.5, 28, 6, 10, 'resultat', label='2', size='s')
text(ax, 13, 14, r'$6=2\times3$', 'limite', 'l'); text(ax, 13, 7, 'aucun corps', 'limite', 's')
box(ax, 30, 4, 8, 10, 'fixe', label='2'); box(ax, 45, 4, 8, 10, 'autre', label='3')
text(ax, 41.5, 9, '×', 'encre', 'm')
text(ax, 70, 9, 'deux premiers\ndifférents', 'limite', 's')
save(fig, '67-005')
