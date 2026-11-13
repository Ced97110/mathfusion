import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 22, 54, 'nombres réels', 'encre', 's'); text(ax, 22, 28, r'corps $F_2$', 'encre', 's')
f = numberline(ax, 8, 44, 44, -1, 1, arrow_right=False)
disc(ax, f(-1), 44, 2, 'varie'); disc(ax, f(1), 44, 2, 'sujet')
text(ax, 64, 44, '2 éléments :\n1 et −1', 'encre', 's')
g = numberline(ax, 8, 44, 18, 0, 1, arrow_right=False)
disc(ax, g(1), 18, 2, 'resultat'); disc(ax, g(0), 18, 1.4, 'fixe')
text(ax, 64, 18, r'$-1=1$ :' + '\n1 élément', 'resultat', 's')
text(ax, 22, 7, r'$1+1=0$', 'encre', 's') if False else None
text(ax, 44, 6, r'car $1+1=0$ : $PSp=Sp$', 'resultat', 's')
save(fig, '75-095')
