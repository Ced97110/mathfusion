import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s, ox, oy = 7.0, 10.0, 10.0
X = lambda v: ox + s * v
Y = lambda v: oy + s * v
arrow(ax, (X(0), Y(0)), (X(5.6), Y(0)), 'fixe', lw=0.8)
arrow(ax, (X(0), Y(0)), (X(0), Y(8.6)), 'fixe', lw=0.8)
line(ax, [(X(0), Y(5)), (X(5), Y(0))], 'sujet', lw=1.3)
line(ax, [(X(0), Y(8)), (X(4), Y(0))], 'autre', lw=1.3)
line(ax, [(X(3), Y(2)), (X(3), Y(0))], 'resultat', dash=True, lw=0.7)
line(ax, [(X(3), Y(2)), (X(0), Y(2))], 'resultat', dash=True, lw=0.7)
disc(ax, X(3), Y(2), 1.2, 'resultat')
text(ax, X(3) + 2.5, Y(0) - 2.6, r'$3$', 'resultat', 's')
text(ax, X(0) - 2.6, Y(2), r'$2$', 'resultat', 's')
line(ax, [(54, 56), (60, 56)], 'sujet', lw=1.3)
text(ax, 62, 56, 'lundi', 'sujet', 's', ha='left')
text(ax, 54, 51.5, r'$x + y = 5$', 'sujet', 's', ha='left')
line(ax, [(54, 43), (60, 43)], 'autre', lw=1.3)
text(ax, 62, 43, 'mardi', 'autre', 's', ha='left')
text(ax, 54, 38.5, r'$2x + y = 8$', 'autre', 's', ha='left')
text(ax, 54, 27, 'croisement :', 'resultat', 's', ha='left')
text(ax, 54, 23, 'la réponse', 'resultat', 's', ha='left')
arrow(ax, (53, 25), (X(3) + 1.6, Y(2) + 0.6), 'resultat')
save(fig, '24-085')
