import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
X = lambda v: 14 + 22 * v
Y = lambda h: 14 + 9 * h
text(ax, 44, 60, r'$s\times s$ sort des $a+bs$', 'encre', 's')
line(ax, [(8, 14), (70, 14)], 'fixe')
line(ax, [(14, 14), (14, 54)], 'fixe')
for v in (0, 1, 2):
    text(ax, X(v), 9.5, str(v), 'fixe', 's')
for h in (1, 2, 4):
    text(ax, 9.5, Y(h), str(h), 'fixe', 's')
line(ax, [(X(0), Y(0)), (X(2), Y(2))], 'autre', lw=1.1)
for v, h in ((0, 0), (1, 1), (2, 4)):
    disc(ax, X(v), Y(h), 1.5, 'sujet')
disc(ax, X(2), Y(2), 1.5, 'autre', fill=False)
arrow(ax, (X(2), Y(2) + 2.2), (X(2), Y(4) - 2.2), 'limite', both=True)
text(ax, X(2) + 4, Y(4), r'$s^2$', 'sujet', 's', ha='left')
text(ax, X(2) + 4, Y(2), r'$a+bs$', 'autre', 's', ha='left')
text(ax, X(2) + 4, 41, r'$4\neq2$', 'limite', 's', ha='left')
save(fig, '55-029')
