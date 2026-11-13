import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
X = lambda x: 14 + x * 15
Y = lambda y: 8 + y * 5.5
line(ax, [(14, 6), (14, 62)], 'fixe'); line(ax, [(14, 8), (62, 8)], 'fixe')
line(ax, [(X(1), Y(2)), (X(3), Y(8))], 'resultat', lw=1.4)
line(ax, [(X(1), Y(2)), (X(1), Y(5))], 'limite', lw=1.4, dash=True)
for (x, y), c in [((1, 2), 'sujet'), ((3, 8), 'sujet'), ((1, 5), 'limite')]:
    disc(ax, X(x), Y(y), 1.3, c)
text(ax, X(1) - 2.5, Y(2) - 3, '(1, 2)', 'sujet', 's', ha='right')
text(ax, X(3) + 2.5, Y(8), '(3, 8)', 'sujet', 's', ha='left')
text(ax, X(1) - 2.5, Y(5), '(1, 5)', 'limite', 's', ha='right')
text(ax, 50, 28, r'pente $\frac{6}{2}=3$', 'resultat', 'm')
text(ax, 44, 66, r'pente $\frac{3}{0}$ : n’existe pas', 'limite', 'm')
save(fig, '21-143')
