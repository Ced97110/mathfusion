import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(46)
g = 16.0
A = (14.0, g); B = (74.0, g)
line(ax, [(4, g), (84, g)], 'fixe', lw=0.7)
disc(ax, A[0], A[1], 1.6, 'sujet'); disc(ax, B[0], B[1], 1.6, 'sujet')
text(ax, A[0], g - 5, 'A', 'sujet', 'm')
text(ax, B[0], g - 5, 'B', 'sujet', 'm')
arrow(ax, (A[0] + 2.5, g + 5), (B[0] - 2.5, g + 5), 'sujet', both=True)
text(ax, 44, g + 10, 'd = 1 000 m', 'sujet', 'l', weight='bold')
text(ax, 44, g - 5, 'base AB, mesurée au ruban', 'fixe', 's')
text(ax, 44, g + 22, 'd = « longueur de AB »', 'encre', 's')
save(fig, '38-035')
