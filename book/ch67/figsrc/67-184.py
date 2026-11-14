import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
R = 6
X = (34, 62)
Y = (52, 28)
pos = [(X[0], Y[0]), (X[1], Y[0]), (X[1], Y[1]), (X[0], Y[1])]
labs = [r'$\alpha$', r'$\alpha^{2}$', r'$\alpha^{4}$', r'$\alpha^{8}$']
for (x, y), l in zip(pos, labs):
    disc(ax, x, y, R, 'sujet', label=l)
arrow(ax, (X[0] + R, Y[0]), (X[1] - R, Y[0]), 'varie')
arrow(ax, (X[1], Y[0] - R), (X[1], Y[1] + R), 'varie')
arrow(ax, (X[1] - R, Y[1]), (X[0] + R, Y[1]), 'varie')
arrow(ax, (X[0], Y[1] + R), (X[0], Y[0] - R), 'resultat')
text(ax, 48, 56.5, 'carré', 'varie', 's')
text(ax, 65, 40, 'carré', 'varie', 's', ha='left')
text(ax, 48, 23.5, 'carré', 'varie', 's')
text(ax, 31, 40, r'$\alpha^{16}=\alpha$', 'resultat', 'm', ha='right')
text(ax, 44, 14, 'après 8 : 16 − 15 = 1', 'encre', 'm')
text(ax, 44, 6, r'racines de $x^{4}+x+1$', 'sujet', 'm')
save(fig, '67-184')
