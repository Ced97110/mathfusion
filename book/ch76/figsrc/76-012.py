import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
u = 8.5; ox, oy = 8, 8
P = lambda x, y: (ox + u * x, oy + u * y)
poly(ax, [P(*p) for p in [(0, 0), (4, 0), (4, 3), (3, 1)]], 'varie'); poly(ax, [P(*p) for p in [(0, 0), (1, 2), (4, 3), (0, 3)]], 'varie')
poly(ax, [P(*p) for p in [(0, 0), (3, 1), (4, 3), (1, 2)]], 'sujet')
text(ax, *P(2.2, 1.45), '5', 'sujet', 'l')
text(ax, *P(3.55, 0.7), '3,5', 'varie', 's'); text(ax, *P(0.55, 2.45), '3,5', 'varie', 's')
text(ax, *P(2, -0.4), '4', 'fixe', 's'); text(ax, *P(-0.45, 1.5), '3', 'fixe', 's')
text(ax, 65, 41, r'rectangle $4\times 3=12$', 'fixe', 's')
text(ax, 65, 32, r'deux morceaux : $7$', 'varie', 's')
text(ax, 65, 22, r'$12-7=5$', 'resultat', 'l')
save(fig, '76-012')
