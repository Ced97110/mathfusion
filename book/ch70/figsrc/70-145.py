import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
ox, oy, u = 10, 42, 20
X = lambda x: ox + u * x
Yv = lambda y: oy + u * y
arrow(ax, (ox - 6, oy), (X(2.4), oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 31), (ox, oy + 36), 'fixe', lw=0.6)
text(ax, X(2.4) + 1, oy - 3, r'$x$', 'fixe', 's')
text(ax, ox + 3, oy + 36, r'$y$', 'fixe', 's')
line(ax, [(X((t / 20) ** 2), Yv(t / 20)) for t in range(-29, 30)], 'sujet', lw=1.4)
line(ax, [(X(x), Yv(1 + (x - 1) / 2)) for x in (-0.3, 2.2)], 'resultat', lw=1.4)
disc(ax, X(1), Yv(1), 1.4, 'varie')
text(ax, X(1) - 2, Yv(1) + 3.5, r'$(1,\ 1)$', 'varie', 's', ha='right')
text(ax, X(2.2) - 1, Yv(1.6) + 4.5, 'tangente', 'resultat', 's', ha='right')
text(ax, X(1.9), Yv(-1.25), r'$y^2-x=0$', 'sujet', 's', ha='left')
box(ax, 58, 62, 28, 9, 'sujet', label=r'$f=y^2-x$', size='s')
box(ax, 58, 50, 28, 9, 'fixe', label=r'$\partial f/\partial x=-1$', size='s')
box(ax, 58, 38, 28, 9, 'fixe', label=r'$\partial f/\partial y=2$', size='s')
box(ax, 58, 22, 28, 11, 'resultat', label=r'$-1(x-1)+2(y-1)=0$', size='s')
for y0 in (62, 50, 38):
    arrow(ax, (72, y0), (72, y0 - 3), 'varie', lw=0.9)
text(ax, 72, 14, r'pente $1/2$', 'resultat', 's')
save(fig, '70-145')
