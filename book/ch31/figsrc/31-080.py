import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 15
c, sn = 0.8192, 0.5736
tris = [  # (legs horizontal, vertical, blue side, equation, title)
    (c, sn, 'hyp', '0,3290 + 0,6710 =', '1 = hypoténuse'),
    (1.0, 0.7002, 'h', '+ 0,4903 = 1,4903', '1 = côté'),
    (1.4281, 1.0, 'v', '+ 2,0396 = 3,0396', '1 = côté')]
xs = [4, 33, 62]
for (hx, vy, blue, eq, title), x in zip(tris, xs):
    y = 22
    P0, P1, P2 = (x, y), (x + hx * s, y), (x, y + vy * s)
    poly(ax, [P0, P1, P2], 'fixe')
    side = {'hyp': [P1, P2], 'h': [P0, P1], 'v': [P0, P2]}[blue]
    line(ax, side, 'sujet', lw=2.4)
    line(ax, [(x, y + 1.8), (x + 1.8, y + 1.8), (x + 1.8, y)], 'fixe', lw=0.6)
    mx, my = (side[0][0] + side[1][0]) / 2, (side[0][1] + side[1][1]) / 2
    off = {'hyp': (3.2, 3.2), 'h': (0, -3), 'v': (-3, 0)}[blue]
    text(ax, mx + off[0], my + off[1], '1', 'sujet', 'm', weight='bold')
    text(ax, x + 11, 46, title, 'sujet', 's', weight='bold')
    if blue == 'hyp':
        text(ax, x + 20, 8, eq, 'encre', 's', ha='right'); text(ax, x + 21.2, 8, '1', 'sujet', 's', ha='left', weight='bold')
    else:
        text(ax, x + 1.4, 8, '1', 'sujet', 's', ha='right', weight='bold'); text(ax, x + 2.6, 8, eq, 'encre', 's', ha='left')
text(ax, 44, 2.5, 'le côté 1 est le rayon', 'sujet', 's')
save(fig, '31-080')
