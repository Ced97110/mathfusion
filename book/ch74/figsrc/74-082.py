import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
Y = lambda y: 15 + (y + 1) * 7
X = lambda x: 12 + x * 7
for i in range(2, 5):
    for j in range(-1, 5):
        disc(ax, X(i), Y(j), 0.5, 'fixe')
p, a, b, c = (X(2), Y(3)), (X(3), Y(-1)), (X(4), Y(-1)), (X(2), Y(4))
arrow(ax, p, a, 'varie'); arrow(ax, a, b, 'varie'); arrow(ax, b, c, 'varie')
arrow(ax, (X(2), Y(3) + 1.5), (X(2), Y(4) - 1.5), 'resultat', lw=1.4)
disc(ax, *p, 1.4, 'sujet'); disc(ax, *a, 1.1, 'fixe'); disc(ax, *b, 1.1, 'fixe'); disc(ax, *c, 1.4, 'resultat')
text(ax, X(2) - 3, Y(4), r'arrivée $(2\ ;\ 4)$', 'resultat', 's', ha='right')
text(ax, X(2) - 3, Y(3) - 2, r'départ $(2\ ;\ 3)$', 'sujet', 's', ha='right')
text(ax, X(2) + 3.5, Y(3.5), r'$Av=(0\ ;\ 1)$', 'resultat', 's', ha='left')
text(ax, 24.5, 30, r'$f^{-1}$', 'varie', 's')
text(ax, X(3.5), Y(-1) - 3.5, r'$t_v$', 'varie', 's')
text(ax, 37, 32, r'$f$', 'varie', 's')
text(ax, 58, 42, 'trois mouvements', 'varie', 's', ha='left')
text(ax, 58, 38.5, 'à la suite :', 'varie', 's', ha='left')
text(ax, 58, 30, 'le point glisse', 'resultat', 's', ha='left')
text(ax, 58, 26.5, 'de la flèche Av', 'resultat', 's', ha='left')
save(fig, '74-082')
