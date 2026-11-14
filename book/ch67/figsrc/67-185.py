import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
R = 6
X = (34, 62)
Y = (52, 28)
pos = [(X[0], Y[0]), (X[1], Y[0]), (X[1], Y[1]), (X[0], Y[1])]
labs = [r'$\alpha^{3}$', r'$\alpha^{6}$', r'$\alpha^{12}$', r'$\alpha^{9}$']
for (x, y), l in zip(pos, labs):
    disc(ax, x, y, R, 'autre', label=l)
arrow(ax, (X[0] + R, Y[0]), (X[1] - R, Y[0]), 'varie')
arrow(ax, (X[1], Y[0] - R), (X[1], Y[1] + R), 'varie')
arrow(ax, (X[1] - R, Y[1]), (X[0] + R, Y[1]), 'varie')
arrow(ax, (X[0], Y[1] + R), (X[0], Y[0] - R), 'resultat')
text(ax, 48, 56.5, 'carré', 'varie', 's')
text(ax, 65, 40, 'carré', 'varie', 's', ha='left')
text(ax, 48, 23.5, '24 − 15 = 9', 'varie', 's')
text(ax, 31, 40, '18 − 15 = 3', 'resultat', 's', ha='right')
text(ax, 44, 14, 'quatre éléments d’ordre 5', 'encre', 'm')
text(ax, 44, 6, r'racines de $x^{4}+x^{3}+x^{2}+x+1$', 'autre', 'm')
save(fig, '67-185')
