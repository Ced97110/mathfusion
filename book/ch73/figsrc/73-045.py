import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 10; ox, oy = 8, 10
X = lambda x: ox + u*x
Y = lambda y: oy + u*y
arrow(ax, (ox-2, oy), (X(5)+6, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy-2), (ox, Y(1)+8), 'fixe', lw=0.7)
for p, q in [((0, 1), (2, 1)), ((3, 1), (5, 1))]:
    arrow(ax, (X(p[0])+1.5, Y(1)), (X(q[0])-1.5, Y(1)), 'varie')
for p in [(0, 1), (3, 1)]:
    disc(ax, X(p[0]), Y(p[1]), 1.2, 'sujet'); text(ax, X(p[0]), Y(1)-4, f'({p[0]}, {p[1]})', 'sujet', 's')
for p in [(2, 1), (5, 1)]:
    disc(ax, X(p[0]), Y(p[1]), 1.2, 'resultat'); text(ax, X(p[0]), Y(1)+4, f'({p[0]}, {p[1]})', 'resultat', 's')
disc(ax, X(1), oy, 1.2, 'fixe'); text(ax, X(1), oy-4, '(1, 0) reste', 'fixe', 's')
text(ax, 44, 41, r'$(x,\,y) \mapsto (x + 2y,\,y)$', 'sujet', 'l')
text(ax, 80, 23, r'$y = 1$', 'fixe', 's'); 
save(fig, '73-045')
