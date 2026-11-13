import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 5.5
cx = [11, 33, 55, 77]
oy = 30
text(ax, 44, 55, 'nombre de vecteurs de la base', 'encre', 's')
# dim 0 : un point
disc(ax, cx[0], oy, 1.6, 'sujet')
text(ax, cx[0], oy + 5, 'O', 'sujet', 's')
# dim 1 : une droite
O = (cx[1], oy)
line(ax, [iso(-1.2, -1.2 * 0, 0, O, u), iso(1.8, 0, 0, O, u)], 'fixe', lw=0.8)
arrow(ax, O, iso(1, 0, 0, O, u), 'sujet', lw=1.6)
# dim 2 : un plan
O = (cx[2], oy)
poly(ax, [iso(-1, -1, 0, O, u), iso(1.6, -1, 0, O, u), iso(1.6, 1.6, 0, O, u), iso(-1, 1.6, 0, O, u)], 'fixe')
arrow(ax, O, iso(1, 0, 0, O, u), 'sujet', lw=1.6)
arrow(ax, O, iso(0, 1, 0, O, u), 'sujet', lw=1.6)
# dim 3 : l'espace
O = (cx[3], oy - 2)
for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
    arrow(ax, O, iso(d[0] * 1.5, d[1] * 1.5, d[2] * 1.5, O, u), 'sujet', lw=1.6)
for c, n in zip(cx, range(4)):
    text(ax, c, 12, f'dim {n}', 'sujet', 'm', weight='bold')
    text(ax, c, 6.5, f'{n} vecteur' + ('s' if n > 1 else ''), 'fixe', 's')
save(fig, '58-304')
