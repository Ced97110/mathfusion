import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 5.6
def axes(ox, oy):
    arrow(ax, (ox, oy), (ox + 5.6 * s, oy), 'fixe', lw=0.8)
    arrow(ax, (ox, oy), (ox, oy + 5.6 * s), 'fixe', lw=0.8)
    return (lambda v: ox + s * v), (lambda v: oy + s * v)
def base(ox):
    X, Y = axes(ox, 14)
    line(ax, [(X(0), Y(5)), (X(5), Y(0))], 'sujet', lw=1.3)
    line(ax, [(X(1.5), Y(5)), (X(4), Y(0))], 'autre', lw=1.3)
    return X, Y
X, Y = base(7)
line(ax, [(X(1), Y(0)), (X(5), Y(4))], 'varie', lw=1.3)
disc(ax, X(3), Y(2), 1.2, 'resultat')
X2, Y2 = base(51)
line(ax, [(X2(2), Y2(5)), (X2(5), Y2(2))], 'varie', lw=1.3)
disc(ax, X2(3), Y2(2), 1.2, 'fixe')
text(ax, 21, 58, '3e droite par (3, 2)', 'varie', 's')
text(ax, 65, 58, '3e droite hors de (3, 2)', 'varie', 's')
text(ax, 21, 5, '1 point commun', 'resultat', 's')
text(ax, 65, 5, '0 point commun', 'encre', 's')
save(fig, '24-088')
