import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, s = 8, 14, 11.0
P = lambda x, y: (ox + x * s, oy + y * s)
cl0 = {(0, 0), (2, 1), (4, 2), (6, 3)}
cl1 = {(1, 0), (3, 1), (5, 2)}
for x in range(7):
    for y in range(4):
        if (x, y) in cl0: r = 'sujet'
        elif (x, y) in cl1: r = 'autre'
        else: r = 'fixe'
        px, py = P(x, y)
        disc(ax, px, py, 1.5 if r == 'fixe' else 2.0, r, fill=(r != 'fixe'))
arrow(ax, (P(0, 0)[0] + 2, P(0, 0)[1] + 0.8), (P(2, 1)[0] - 2.2, P(2, 1)[1] - 0.6), 'varie', lw=1.2)
text(ax, P(1, 0)[0] - 4, P(1, 0)[1] + 7.5, r'$u=(2\,;\,1)$', 'varie', 's', ha='center')
text(ax, 22, 62, 'classe de (0 ; 0) et de (2 ; 1)', 'sujet', 's')
text(ax, 22, 57, 'classe de (1 ; 0) et de (3 ; 1)', 'autre', 's')
text(ax, 66, 8, 'combien de classes ?', 'encre', 'm')
save(fig, '57-182')
