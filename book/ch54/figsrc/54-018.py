import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
O = (14, 12); ux, uy = 11, 6
X = lambda a: O[0] + ux * a
Y = lambda b: O[1] + uy * b
arrow(ax, O, (X(6.6), O[1]), 'fixe', lw=0.7)
arrow(ax, O, (O[0], Y(10.8)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0)), (X(5.2), Y(10.4))], 'sujet', lw=1.0)
for k in (1, 3, 5):
    disc(ax, X(k), Y(2 * k), 1.4, 'sujet')
    text(ax, X(k) + 2.6, Y(2 * k), rf'${2 * k}/{k}=2$', 'sujet', 's', ha='left')
disc(ax, X(3), Y(4), 1.4, 'limite', fill=False)
text(ax, X(3) + 2.6, Y(4), r'$4/3\neq2$', 'limite', 's', ha='left')
text(ax, 44, 84, 'une droite : $b/a=2$', 'sujet', 'm')
text(ax, 44, 3, 'b/a : second ÷ premier', 'fixe', 's')
save(fig, '54-018')
