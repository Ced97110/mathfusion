import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 8; oy = 16
def shape(ox, a, b, role, area, name):
    P = lambda p: (ox + p[0]*u, oy + p[1]*u)
    poly(ax, [P((0,0)), P(a), P((a[0]+b[0], a[1]+b[1])), P(b)], role)
    arrow(ax, P((0,0)), P(a), 'sujet', lw=1.2); arrow(ax, P((0,0)), P(b), 'sujet', lw=1.2)
    text(ax, *P(((a[0]+b[0])/2, (a[1]+b[1])/2)), area, role, 'l')
    text(ax, ox + 6, oy - 7, name, role, 's')
shape(4, (1, 0), (0, 1), 'fixe', '1', 'départ')
shape(26, (2, 0), (0, 1), 'limite', '2', 'doubler : non')
shape(52, (1, 0), (2, 1), 'resultat', '1', 'mouvement libre : oui')
text(ax, 44, 44, r'$B(\eta x, \eta y) = B(x, y)\ ?$', 'encre', 'm')
save(fig, '75-043')
