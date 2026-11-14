import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
O, u = (44, 14), 7
X = lambda b, c: (O[0] + b * u, O[1] + c * u)
bs = np.linspace(-4, 4, 60)
curve = [X(b, b * b / 4) for b in bs]
poly(ax, curve + [X(4, -1), X(-4, -1)], 'resultat')
poly(ax, curve + [X(4, 5.5), X(-4, 5.5)], 'limite')
line(ax, curve, 'sujet', lw=1.7)
arrow(ax, X(-4, 0), X(4.3, 0), 'fixe', lw=0.8); arrow(ax, X(0, -1), X(0, 5.9), 'fixe', lw=0.8)
text(ax, 78, 14, 'b', 'encre', 's'); text(ax, 47, 56, 'c', 'encre', 's')
line(ax, [X(2, -1), X(2, 5.5)], 'fixe', dash=True)
disc(ax, *X(2, 0), 1.3, 'resultat'); disc(ax, *X(2, 1), 1.3, 'varie'); disc(ax, *X(2, 5), 1.3, 'limite')
text(ax, X(2, 0)[0] + 3, X(2, 0)[1] - 3.5, '(2 ; 0)', 'resultat', 's', ha='left')
text(ax, X(2, 1)[0] + 3, X(2, 1)[1] - 3.5, '(2 ; 1)', 'varie', 's', ha='left')
text(ax, X(2, 5)[0] - 3, X(2, 5)[1], '(2 ; 5)', 'limite', 's', ha='right')
text(ax, 26, 10, r'$b^2-4c\geq 0$', 'resultat', 's')
text(ax, 24, 44, r'$b^2-4c<0$', 'limite', 's')
text(ax, 77, 46, r'$c=b^2/4$', 'sujet', 's')
save(fig, '70-170')
