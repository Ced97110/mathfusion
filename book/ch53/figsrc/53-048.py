import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# points (p, 5p + 3) : 3, 8, 13, 18, 23
ox, oy, ux, uy = 14.0, 8.0, 14.0, 2.2
X = lambda p: ox + ux * p
Y = lambda v: oy + uy * v
arrow(ax, (ox, oy), (ox + 4 * ux + 8, oy), 'fixe', lw=0.8)
line(ax, [(ox, oy), (ox, Y(26))], 'fixe', lw=0.8)
line(ax, [(ox - 3, Y(25)), (ox + 4 * ux + 6, Y(25))], 'fixe', lw=0.6, dash=True)
text(ax, ox + 4 * ux + 7, Y(25) + 3, '25 : fin de l’horloge', 'fixe', 's', ha='right')
line(ax, [(X(0), Y(3)), (X(4), Y(23))], 'sujet', lw=1.0, dash=True)
vals = [3, 8, 13, 18, 23]
for p, v in enumerate(vals):
    disc(ax, X(p), Y(v), 1.5, 'sujet')
    text(ax, X(p) - 3.2, Y(v) + 2.2, str(v), 'sujet', 's', ha='right')
    text(ax, X(p), oy - 3.5, str(p), 'fixe', 's')
# un pas : +1 sur p donne +5 sur le résultat
line(ax, [(X(1), Y(8)), (X(2), Y(8))], 'varie', lw=1.3)
arrow(ax, (X(2), Y(8)), (X(2), Y(13)), 'varie', lw=1.3)
text(ax, (X(1) + X(2)) / 2, Y(8) - 3, '+1', 'varie', 's', weight='bold')
text(ax, X(2) + 2.5, (Y(8) + Y(13)) / 2, '+5', 'varie', 's', weight='bold', ha='left')
text(ax, 44, 79, r'$y=ax+b$ avec $a=5$, $b=3$', 'sujet', 'm', weight='bold')
save(fig, '53-048')
