import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 14
def shape(ox, oy, a, b, role, area):
    P = lambda p: (ox + p[0]*u, oy + p[1]*u)
    poly(ax, [P((0,0)), P(a), P((a[0]+b[0], a[1]+b[1])), P(b)], role)
    arrow(ax, P((0,0)), P(a), 'sujet', lw=1.2); arrow(ax, P((0,0)), P(b), 'sujet', lw=1.2)
    text(ax, *P(((a[0]+b[0])/2, (a[1]+b[1])/2)), area, role, 'l')
box(ax, 2, 14, 32, 32, 'fixe', fill=False, r=1.0); box(ax, 54, 14, 32, 32, 'fixe', fill=False, r=1.0)
shape(8, 20, (1, 0), (0, 1), 'sujet', '1')
shape(56, 20, (1, 0), (1, 1), 'autre', '1')
text(ax, 18, 42, r'$V$ : dimension $2n$', 'sujet', 's'); text(ax, 70, 42, r"$V'$ : dimension $2n$", 'autre', 's')
text(ax, 18, 9, r'base $(1,0)$ et $(0,1)$', 'sujet', 's')
text(ax, 70, 9, r'base $(1,0)$ et $(1,1)$', 'autre', 's')
arrow(ax, (35, 30), (53, 30), 'resultat', lw=1.4)
text(ax, 44, 36, 'changement', 'resultat', 's'); text(ax, 44, 25, 'de base', 'resultat', 's')
text(ax, 44, 56, 'même dimension, même géométrie', 'resultat', 's', weight='bold')
save(fig, '75-041')
