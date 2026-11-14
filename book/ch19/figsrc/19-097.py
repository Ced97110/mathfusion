import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'le moins va sur la montée', 'sujet', 'm', weight='bold')
# one line, slope -1/2 : y = 47 - (x - 6) / 2
Y = lambda x: 47 - (x - 6) / 2
line(ax, [(6, Y(6)), (84, Y(84))], 'sujet', lw=1.2)
text(ax, 6, 51, 'la même droite', 'sujet', 's', ha='left')
# chosen writing: advance 2 to the right (positive), rise -1 (down)
A, C, B = (20, Y(20)), (44, Y(20)), (44, Y(44))
arrow(ax, A, C, 'resultat', lw=1.6); arrow(ax, C, B, 'varie', lw=1.6)
disc(ax, *A, 1.1, 'sujet')
text(ax, 32, A[1] + 3.5, 'avancée 2', 'resultat', 's')
text(ax, 46.5, (C[1] + B[1]) / 2, 'montée −1', 'varie', 's', ha='left')
# other writing: same line, kept in grey, not retained
D, E, F = (80, Y(80)), (56, Y(80)), (56, Y(56))
arrow(ax, D, E, 'fixe', lw=0.9); arrow(ax, E, F, 'fixe', lw=0.9)
text(ax, 68, D[1] - 3.6, 'avancée −2', 'fixe', 's')
text(ax, 53.5, (E[1] + F[1]) / 2, 'montée 1', 'fixe', 's', ha='right')
text(ax, 68, 2.2, 'écriture non retenue', 'fixe', 's')
text(ax, 32, 24, 'écriture choisie', 'resultat', 's')
save(fig, '19-097')
