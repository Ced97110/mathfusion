import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
O, u = (44, 14), 9
cubes(ax, [(i, j, k) for i in range(3) for j in range(3) for k in range(3)], O, u, 'sujet')
text(ax, 44, 84, r'restes $a+bx+cx^2$', 'sujet', 'l')
text(ax, 74, 20, 'a : 0, 1, 2', 'fixe', 's')
text(ax, 14, 20, 'b : 0, 1, 2', 'fixe', 's')
text(ax, 10, 52, 'c : 0, 1, 2', 'fixe', 's')
text(ax, 44, 5, r'$3\times3\times3=27$ restes', 'resultat', 'l')
save(fig, '54-203')
