import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, s = 12, 14, 7.0
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(-1, 0), P(5, 0), 'fixe', lw=0.7)
arrow(ax, P(0, -1), P(0, 7), 'fixe', lw=0.7)
arrow(ax, P(0, 0), P(3, 4), 'sujet', lw=1.3)
text(ax, P(3, 4)[0] + 8, P(3, 4)[1] + 1, r'$\langle 3,\ 4\rangle$', 'sujet', 's')
disc(ax, ox, oy, 1.3, 'varie')
text(ax, ox + 11, oy - 5, 'vecteur nul : un point', 'varie', 's')
text(ax, ox + 2, oy + 31, 'angle ?', 'limite', 's')
# le calcul de l'angle exige une division par la norme du vecteur nul
box(ax, 50, 40, 36, 24, 'fixe')
text(ax, 68, 58, 'division demandée', 'fixe', 's')
text(ax, 68, 50, r'$0\ \div\ (0\times 5)$', 'encre', 'm')
text(ax, 68, 43.5, r'$0\ \div\ 0$ : impossible', 'limite', 's')
text(ax, 68, 28, r'$u\cdot v=0$ ne dit', 'encre', 's')
text(ax, 68, 22, 'rien sur l’angle', 'encre', 's')
save(fig, '41-148')
