import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 22, 52, 'vecteur : élément de $V$', 'sujet', 's')
text(ax, 68, 52, 'scalaire : élément de $F$', 'varie', 's')
o = (6, 10); U = 14.0
line(ax, [o, (o[0] + 36, o[1])], 'fixe', lw=0.5)
line(ax, [o, (o[0], o[1] + 30)], 'fixe', lw=0.5)
arrow(ax, o, (o[0] + 2 * U, o[1] + U), 'sujet', lw=1.8)
text(ax, o[0] + 2 * U + 1, o[1] + U + 4, '(2, 1)', 'sujet', 'm')
text(ax, 49, 24, '×', 'encre', 'l')
disc(ax, 68, 30, 8, 'varie', label='3', size='xl')
text(ax, 44, 4, '3 multiplie la flèche (2, 1)', 'encre', 's')
save(fig, '58-085')
