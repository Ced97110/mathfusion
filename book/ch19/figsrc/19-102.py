import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
steps = [(66, 'fixe', r'$y-3=2(x-4)$'), (44, 'varie', r'$y-3=2x-8$'), (22, 'resultat', r'$y=2x-5$')]
for y, r, s in steps: box(ax, 6, y, 44, 12, r, label=s, size='l')
arrow(ax, (28, 66), (28, 56.5), 'varie'); text(ax, 54, 61.2, 'on développe', 'varie', 's', ha='left')
arrow(ax, (28, 44), (28, 34.5), 'varie'); text(ax, 54, 39.2, '+ 3 des deux côtés', 'varie', 's', ha='left')
text(ax, 28, 80, 'pente 2, point (4, 3)', 'sujet', 's')
arrow(ax, (28, 22), (28, 14.5), 'resultat')
text(ax, 28, 8, r'$x=4$ : $2\times4-5=3$ ✓', 'resultat', 's')
save(fig, '19-102')
