import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
X = lambda x: 30 + 8 * x; Y = lambda y: 8 + 6 * y
arrow(ax, (6, 8), (84, 8), 'fixe', lw=0.8); arrow(ax, (30, 4), (30, 86), 'fixe', lw=0.8)
text(ax, 84, 12, '$x$', 'fixe', 's'); text(ax, 34, 87, '$y$', 'fixe', 's')
line(ax, [(X(-3.5), Y(0)), (X(2.5), Y(12))], 'sujet', lw=1.5)
for (x, y) in [(0, 7), (1, 9), (-2, 3)]:
    disc(ax, X(x), Y(y), 1.5, 'resultat'); text(ax, X(x) + 3, Y(y) - 3.5, f'({x}, {y})'.replace('-', '−'), 'resultat', 's', ha='left')
text(ax, 64, 76, r'$y$ = 2$x$ + 7', 'sujet', 'm'); text(ax, 62, 36, 'chaque point :\nun couple', 'resultat', 's')
text(ax, 62, 22, 'une infinité de couples', 'fixe', 's')
save(fig, '16-141')
