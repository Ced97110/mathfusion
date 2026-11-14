import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
o = (44, 6); u = 7.0
def P(x, y, z): return iso(x, y, z, o, u)
X, Y, Z = 4, 3, 2
for a, b in (((0,0,0),(X,0,0)),((0,Y,0),(X,Y,0)),((0,0,Z),(X,0,Z)),((0,Y,Z),(X,Y,Z)),
             ((0,0,0),(0,Y,0)),((X,0,0),(X,Y,0)),((0,0,Z),(0,Y,Z)),((X,0,Z),(X,Y,Z)),
             ((0,0,0),(0,0,Z)),((X,0,0),(X,0,Z)),((0,Y,0),(0,Y,Z)),((X,Y,0),(X,Y,Z))):
    line(ax, [P(*a), P(*b)], 'fixe', lw=0.7)
line(ax, [P(0,0,0), P(X,0,0)], 'sujet', lw=1.8); line(ax, [P(X,0,0), P(X,Y,0)], 'varie', lw=1.8); line(ax, [P(X,Y,0), P(X,Y,Z)], 'autre', lw=1.8)
line(ax, [P(0,0,0), P(X,Y,Z)], 'resultat', lw=1.8)
text(ax, P(0,0,0)[0]-3, P(0,0,0)[1]-3, 'A', 'encre', 's'); text(ax, P(X,Y,Z)[0], P(X,Y,Z)[1]+3, 'G', 'encre', 's')
a = P(2,0,0); text(ax, a[0]+1, a[1]-4, 'x = 4', 'sujet', 's')
a = P(X,1.5,0); text(ax, a[0]+10, a[1]-3, 'y = 3', 'varie', 's')
a = P(X,Y,1); text(ax, a[0]+6, a[1], 'z = 2', 'autre', 's')
text(ax, 18, 56, r'$AG=\sqrt{x^2+y^2+z^2}$', 'resultat', 's')
text(ax, 18, 48, r'$=\sqrt{29}\approx 5{,}39$', 'resultat', 's')
save(fig, '27-124')
