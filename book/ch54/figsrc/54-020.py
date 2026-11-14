import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
O = (12, 12); ux, uy = 7, 6
X = lambda a: O[0] + ux * a
Y = lambda b: O[1] + uy * b
arrow(ax, O, (X(10.6), O[1]), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0.5)), (X(0), Y(8.8))], 'autre', lw=1.3)
line(ax, [(X(0), Y(0)), (X(9.6), Y(3.2))], 'sujet', lw=1.0)
for a in (3, 6, 9):
    disc(ax, X(a), Y(a // 3), 1.4, 'sujet')
    text(ax, X(a), Y(a // 3) + 4.3, f'({a}, {a // 3})', 'sujet', 's')
for b in (5, 8):
    disc(ax, X(0), Y(b), 1.4, 'autre')
    text(ax, X(0) + 2.8, Y(b), f'(0, {b})', 'autre', 's', ha='left')
disc(ax, X(0), Y(0), 1.4, 'limite', fill=False)
text(ax, X(0) + 2.8, Y(0) - 4.5, '(0, 0) exclu', 'limite', 's', ha='left')
text(ax, 58, 39, r'$3/1=3$', 'sujet', 'm')
text(ax, X(0) + 3, Y(6.5), r'$0/b=0$', 'autre', 'm', ha='left')
save(fig, '54-020')
