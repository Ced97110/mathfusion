import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
B = 52
labs = [(r'$x$', 'sujet'), (r'$y$', 'autre'), (r'$x^{-1}$', 'sujet'), (r'$y^{-1}$', 'autre')]
X = [13 + 16 * i for i in range(4)]
for xi, (l, r) in zip(X, labs): box(ax, xi, B, 14, 10, r, label=l, size='l')
brace(ax, X[1], X[3] + 14, B + 10, 'sujet', label=r'$yx^{-1}y^{-1}\in P$', down=False)
brace(ax, X[0], X[3] + 14, B + 17, 'sujet', label='le tout est dans $P$', down=False)
brace(ax, X[0], X[2] + 14, B, 'autre', label=r'$xyx^{-1}\in Q$')
brace(ax, X[0], X[3] + 14, B - 7, 'autre', label='le tout est dans $Q$')
arrow(ax, (44, 38.5), (44, 34), 'resultat')
box(ax, 10, 24, 68, 9.5, 'resultat', label=r'$xyx^{-1}y^{-1}\in P\cap Q$')
save(fig, '50-168')
