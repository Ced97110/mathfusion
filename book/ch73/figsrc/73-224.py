import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
O = (8, 12); k = 6
X = (O[0] + 3 * k, O[1] + 4 * k); Y = (O[0] + 5 * k, O[1]); S = (O[0] + 8 * k, O[1] + 4 * k)
line(ax, [Y, S], 'fixe', dash=True); line(ax, [X, S], 'fixe', dash=True)
arrow(ax, O, X, 'sujet', lw=1.3); arrow(ax, O, Y, 'autre', lw=1.3); arrow(ax, O, S, 'varie', lw=1.3)
text(ax, X[0] - 2, X[1] + 3.5, r'$x$', 'sujet', 'm'); text(ax, Y[0], Y[1] - 3.5, r'$y$', 'autre', 'm')
text(ax, S[0] + 3, S[1] + 4, r'$x+y$', 'varie', 'm')
text(ax, 2, 30, r'$\|x\|^2=25$', 'sujet', 's', ha='left'); text(ax, 22, 7, r'$\|y\|^2=25$', 'autre', 's')
text(ax, 38, 31.5, r'$\|x+y\|^2=80$', 'varie', 's')
text(ax, 74, 22, r'$\frac{1}{2}(80-25-25)$', 'encre', 's')
text(ax, 74, 12, r'$=15=\langle x,y\rangle$', 'resultat', 's')
save(fig, '73-224')
