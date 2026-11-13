import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ax.set_ylim(14.75, 74.75)  # même échelle ; centre le contenu verticalement
text(ax, 44, 70, '10 − 4 + 3', 'encre', 'l', weight='bold')
text(ax, 44, 63.5, 'gauche à droite : 6, puis 9', 'resultat', 's')
# premier pas : 10 − 4 = 6
arrow(ax, (84, 56), (52.8, 56), 'resultat')
text(ax, 68.4, 58.5, '− 4', 'resultat', 's')
# second pas : 6 + 3 = 9
arrow(ax, (52.8, 50), (76.2, 50), 'resultat')
text(ax, 64.5, 52.5, '+ 3', 'resultat', 's')
line(ax, [(52.8, 56), (52.8, 40)], 'fixe', dash=True)
line(ax, [(76.2, 50), (76.2, 40)], 'fixe', dash=True)
# droite graduée de 0 à 10
f = numberline(ax, 6, 84, 40, 0, 10, step=1, labels=False, arrow_right=False)
text(ax, f(0), 36.5, '0', 'fixe', 's')
text(ax, f(6), 36.5, '6', 'fixe', 's')
text(ax, f(10), 36.5, '10', 'fixe', 's')
text(ax, f(9), 36.5, '9', 'resultat', 's')
text(ax, f(3), 36.5, '3', 'limite', 's')
disc(ax, f(9), 40, 1.2, 'resultat')
disc(ax, f(3), 40, 1.2, 'limite')
# autre ordre : retirer 7 d'un coup
arrow(ax, (84, 30), (f(3), 30), 'limite')
text(ax, 56.7, 27, '− 7', 'limite', 's')
text(ax, 44, 19, "4 + 3 d'abord : 10 − 7 = 3", 'limite', 's')
save(fig, '04-062')
