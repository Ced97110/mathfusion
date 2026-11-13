import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 3.6
def para(ox, oy, a, b, role):
    P = lambda p: (ox + p[0]*u, oy + p[1]*u)
    poly(ax, [P((0,0)), P(a), P((a[0]+b[0], a[1]+b[1])), P(b)], role)
    arrow(ax, P((0,0)), P(a), 'sujet', lw=1.2); arrow(ax, P((0,0)), P(b), 'varie', lw=1.2)
    return P
box(ax, 3, 8, 34, 40, 'fixe', fill=False, dash=True); box(ax, 41, 8, 44, 40, 'fixe', fill=False, dash=True)
P = para(8, 12, (3, 2), (1, 4), 'sujet')
Q = para(44, 14, (5, 2), (2, 1), 'autre')
text(ax, 20, 50, r'$P_1$', 'sujet', 'l'); text(ax, 63, 50, r'$P_2$', 'autre', 'l')
text(ax, 22, 29, '10', 'sujet', 'l'); text(ax, 64, 20, '1', 'autre', 'l')
text(ax, 12.5, 29.5, r'$y$', 'varie', 's'); text(ax, 21.5, 20.8, r'$x$', 'sujet', 's')
text(ax, 39, 26, '+', 'encre', 'xl')
text(ax, 44, 2.8, r'$B(x,y) = 10 + 1 = 11$', 'resultat', 'm')
save(fig, '75-039')
