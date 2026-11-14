import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
O = (14, 12); u = 12
X = lambda a: O[0] + u * a
Y = lambda b: O[1] + u * b
for a in range(6):
    for b in range(6):
        disc(ax, X(a), Y(b), 0.45, 'fixe')
arrow(ax, O, (X(5.6), O[1]), 'fixe', lw=0.7)
arrow(ax, O, (O[0], Y(5.6)), 'fixe', lw=0.7)
text(ax, X(5.6) + 1.5, O[1] + 3, 'a', 'fixe', 'm')
text(ax, O[0] + 3, Y(5.6) + 1.5, 'b', 'fixe', 'm')
line(ax, [(X(4), Y(0)), (X(4), Y(3))], 'autre', dash=True)
line(ax, [(X(0), Y(3)), (X(4), Y(3))], 'autre', dash=True)
arrow(ax, (X(0), Y(0)), (X(3), Y(0)), 'varie', lw=1.4)
arrow(ax, (X(3), Y(0)), (X(3), Y(4)), 'varie', lw=1.4)
text(ax, X(1.5), Y(0) + 2.6, '3', 'varie', 'm')
text(ax, X(3) - 2.6, Y(2), '4', 'varie', 'm')
disc(ax, X(3), Y(4), 1.6, 'sujet')
text(ax, X(3) - 2.5, Y(4) + 4, '(3, 4)', 'sujet', 'm')
disc(ax, X(4), Y(3), 1.6, 'autre')
text(ax, X(4) + 2.8, Y(3) - 0.2, '(4, 3)', 'autre', 'm', ha='left')
text(ax, 44, 86, r'$(3,4)\neq(4,3)$', 'encre', 'l')
text(ax, 26, 3, 'a : numérateur', 'varie', 's')
text(ax, 62, 3, 'b : dénominateur', 'varie', 's')
save(fig, '54-013')
