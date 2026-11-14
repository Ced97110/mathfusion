import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 30.0; ox, oy = 12.0, 14.0           # Re 3 en x=ox ; Im -1 en y=oy
X = lambda re: ox + (re - 3) * u * 0.9
Y = lambda im: oy + (im + 1) * u * 1.0
for re in (3, 4):
    for im in (-1, 0):
        disc(ax, X(re), Y(im), 1.2, 'fixe')
line(ax, [(X(3), Y(-1)), (X(4), Y(-1)), (X(4), Y(0)), (X(3), Y(0)), (X(3), Y(-1))], 'fixe', lw=0.5, dash=True)
px, py = X(3.2), Y(-0.6)
disc(ax, px, py, 1.7, 'sujet')
text(ax, px + 3, py + 3, r'$a/b=3{,}2-0{,}6\,i$', 'sujet', 's', ha='left')
disc(ax, X(3), Y(-1), 2.0, 'resultat', fill=True)
arrow(ax, (px - 0.4, py - 1.5), (X(3) + 0.8, Y(-1) + 1.5), 'varie', lw=1.2)
text(ax, X(3) + 3, Y(-1) - 4, r'$q=3-i$', 'resultat', 'm', ha='left')
text(ax, X(3), oy - 9, '3', 'fixe', 's')
text(ax, X(4), oy - 9, '4', 'fixe', 's')
text(ax, X(3) - 4, Y(-1), r'$-1$', 'fixe', 's', ha='right')
text(ax, X(3) - 4, Y(0), '0', 'fixe', 's', ha='right')
text(ax, 70, Y(-0.5), 'arrondir', 'varie', 's')
text(ax, 70, Y(-0.5) - 5, '3,2 → 3', 'varie', 's')
text(ax, 70, Y(-0.5) - 9, '−0,6 → −1', 'varie', 's')
save(fig, '56-129')
