import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 5.2; oy = 14
def shape(ox, a, b, role, area):
    P = lambda p: (ox + p[0]*u, oy + p[1]*u)
    poly(ax, [P((0,0)), P(a), P((a[0]+b[0], a[1]+b[1])), P(b)], role)
    arrow(ax, P((0,0)), P(a), 'sujet', lw=1.2); arrow(ax, P((0,0)), P(b), 'sujet', lw=1.2)
    text(ax, *P(((a[0]+b[0])/2, (a[1]+b[1])/2)), area, role, 'm')
shape(3, (1, 0), (0, 1), 'fixe', '1')
shape(24, (1, 0), (1, 1), 'resultat', '1')
shape(46, (1, 0), (5, 1), 'resultat', '1')
arrow(ax, (14, 22), (22, 22), 'varie', lw=1.1); text(ax, 18, 27, '1 s', 'varie', 's')
arrow(ax, (38, 22), (44, 22), 'varie', lw=1.1); text(ax, 41, 27, '4 s', 'varie', 's')
text(ax, 44, 6, 'enchaînés : l’aire reste 1', 'resultat', 'm')
text(ax, 44, 42, r'$Sp_{2n}(F)$ : groupe', 'sujet', 'm')
save(fig, '75-044')
