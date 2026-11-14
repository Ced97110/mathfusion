import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
Y = 24
f = numberline(ax, 10, 76, Y, 0, 5)
for v in (0, 2, 4): disc(ax, f(v), Y, 1.6, 'varie')
disc(ax, f(3), Y, 2.2, 'sujet')
arrow(ax, (f(0), Y + 2), (f(2), Y + 2), 'varie', curve=-0.5)
arrow(ax, (f(2), Y + 2), (f(4), Y + 2), 'varie', curve=-0.5)
text(ax, f(1), 36, '+2', 'varie', 's'); text(ax, f(3), 36, '+2', 'varie', 's')
text(ax, f(3), 29.5, r'$k=3$', 'sujet', 's')
arrow(ax, (f(2), 13), (f(3), 13), 'resultat')
text(ax, f(2.5), 8.5, r'+1 : taille $p^0=1$', 'resultat', 's')
text(ax, 44, 47, 'tailles paires : on saute 3', 'limite', 'm')
save(fig, '50-119')
