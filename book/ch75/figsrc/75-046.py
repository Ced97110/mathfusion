import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 5; oy = 12
def shape(ox, a, b, role, area, la, lb):
    P = lambda p: (ox + p[0]*u, oy + p[1]*u)
    poly(ax, [P((0,0)), P(a), P((a[0]+b[0], a[1]+b[1])), P(b)], role)
    arrow(ax, P((0,0)), P(a), 'sujet', lw=1.2); arrow(ax, P((0,0)), P(b), 'varie', lw=1.2)
    text(ax, *P(((a[0]+b[0])/2, (a[1]+b[1])/2)), area, role, 'l')
    t = P(a); text(ax, t[0] + 3.5, t[1] - 2, la, 'sujet', 's'); t = P(b); text(ax, t[0] - 3.5, t[1] + 1.5, lb, 'varie', 's')
shape(5, (3, 1), (1, 2), 'sujet', '5', r'$x$', r'$y$')
shape(52, (4, 1), (3, 2), 'resultat', '5', r'$\eta x$', r'$\eta y$')
arrow(ax, (27, 22), (45, 22), 'varie', lw=1.2); text(ax, 36, 26, r'$\eta$', 'varie', 'm')
text(ax, 44, 4, 'même aire : 5', 'resultat', 'm')
text(ax, 44, 41, 'de base symplectique à base symplectique', 'fixe', 's')
save(fig, '75-046')
