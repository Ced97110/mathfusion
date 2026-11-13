import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
O = (10, 8); ux, uy = 10, 7
X = lambda a: O[0] + ux * a
Y = lambda b: O[1] + uy * b
for a in range(8):
    for b in range(11):
        disc(ax, X(a), Y(b), 0.4, 'fixe')
arrow(ax, O, (X(7.5), O[1]), 'fixe', lw=0.7)
arrow(ax, O, (O[0], Y(10.6)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0)), (X(6.6), Y(9.9))], 'sujet', lw=1.2)
for a, b in [(2, 3), (4, 6), (6, 9)]:
    disc(ax, X(a), Y(b), 1.5, 'sujet')
    t = text(ax, X(a) + 3, Y(b) - 0.5, f'{a}/{b}', 'varie', 'm', ha='left')
    t.set_bbox(dict(fc='white', ec='none', pad=0.8))
text(ax, 44, 88, 'la fraction : toute la droite', 'sujet', 'm')
text(ax, 44, 3, 'même droite, trois noms', 'varie', 's')
save(fig, '54-021')
