import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for i in range(4):
    k = i + 1; x = 2 + i * 22; odd = k % 2 == 1
    box(ax, x, 34, 19, 12, 'sujet' if odd else 'fixe', label=r'$x$' if odd else '1 sur la\ndiagonale', size='m' if odd else 's')
    text(ax, x + 9.5, 50, r'$x^%d$' % k, 'sujet' if odd else 'fixe', 'm')
box(ax, 22, 6, 44, 10, 'resultat', label=r'$x^2\circ x^2=x^4$')
arrow(ax, (35, 33.5), (32, 16.5), 'varie')
arrow(ax, (58, 16.5), (76, 33.5), 'resultat')
text(ax, 50, 24, '2 + 2 = 4', 'resultat', 's')
save(fig, '78-070')
