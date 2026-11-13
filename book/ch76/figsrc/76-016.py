import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
u = 5.2
# gauche : u et u
ox, oy = 4, 20
P = lambda x, y: (ox + u * x, oy + u * y)
line(ax, [P(0, 0), P(6, 2)], 'sujet', lw=2.0)
arrow(ax, P(0, 0), P(3, 1), 'sujet', lw=1.3); arrow(ax, P(3, 1), P(6, 2), 'sujet', lw=1.3)
for p in [(0, 0), (3, 1), (6, 2)]: disc(ax, *P(*p), 0.9, 'sujet')
text(ax, *P(1.4, 1.2), 'u', 'sujet', 'm'); text(ax, *P(4.6, 2.2), 'u', 'sujet', 'm')
text(ax, 18, 8, 'même flèche : 0 carreau', 'resultat', 's')
# droite : u et v
ox2, oy2 = 52, 14; P2 = lambda x, y: (ox2 + u * x, oy2 + u * y)
poly(ax, [P2(*p) for p in [(0, 0), (3, 1), (4, 3), (1, 2)]], 'limite')
text(ax, *P2(2.2, 1.45), '5', 'limite', 'l')
text(ax, *P2(3.4, 0.2), 'u', 'limite', 'm'); text(ax, *P2(0.1, 2.5), 'v', 'limite', 'm')
text(ax, 66, 8, 'flèches différentes : 5', 'limite', 's')
save(fig, '76-016')
