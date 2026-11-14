import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
O = (10, 8); u = 10
X = lambda a: O[0] + u * a
Y = lambda b: O[1] + u * b
for a in range(8):
    for b in range(7):
        disc(ax, X(a), Y(b), 0.45, 'fixe')
arrow(ax, O, (X(7.5), O[1]), 'fixe', lw=0.7)
arrow(ax, O, (O[0], Y(6.5)), 'fixe', lw=0.7)
text(ax, 85, 9, 'a', 'fixe', 'm')
text(ax, 10, 78, 'b', 'fixe', 'm')
line(ax, [(X(3), Y(0)), (X(7.2), Y(4.2))], 'autre', lw=1.0)
line(ax, [(X(0), Y(0)), (X(3.2), Y(6.4))], 'sujet', lw=1.0)
for a, b in [(5, 2), (6, 3)]:
    disc(ax, X(a), Y(b), 1.4, 'autre')
for a, b in [(1, 2), (2, 4)]:
    disc(ax, X(a), Y(b), 1.4, 'sujet')
text(ax, X(5) + 2.5, Y(2) - 3.2, '(5, 2)', 'autre', 's', ha='left')
text(ax, X(6) - 5, Y(3) + 4.5, '(6, 3)', 'autre', 's')
text(ax, X(1) + 2.5, Y(2), '(1, 2)', 'sujet', 's', ha='left')
text(ax, X(2) + 2.5, Y(4), '(2, 4)', 'sujet', 's', ha='left')
text(ax, 86, 55, r'ch. 13 : $a-b=3$', 'autre', 's', ha='right')
text(ax, X(3.2) + 2, 74, r'ici : $b=2a$', 'sujet', 's', ha='left')
save(fig, '54-014')
