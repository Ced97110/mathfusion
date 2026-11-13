import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, s = 12, 14, 9.0
P = lambda x, y: (ox + (x + 1) * s, oy + y * s)
for x in range(-1, 8):
    for y in range(0, 3):
        px, py = P(x, y)
        if y == 0 and x % 2 == 0: disc(ax, px, py, 2.0, 'sujet')
        elif (x, y) in ((1, 0), (0, 1)): disc(ax, px, py, 2.0, 'limite')
        else: disc(ax, px, py, 0.9, 'fixe', fill=False)
arrow(ax, (P(0, 0)[0] + 2.2, P(0, 0)[1] + 3.2), (P(2, 0)[0] - 2.2, P(2, 0)[1] + 3.2), 'varie', lw=1.2)
text(ax, P(1, 0)[0], P(1, 0)[1] + 6.5, r'$u^{\prime}=(2\,;\,0)$', 'varie', 's')
text(ax, 44, 50, r'$N^{\prime}$ : les $(2k\,;\,0)$', 'sujet', 'm')
text(ax, P(1, 0)[0], P(1, 0)[1] - 5, '(1 ; 0)', 'limite', 's')
text(ax, P(0, 1)[0] - 6, P(0, 1)[1] + 4.5, '(0 ; 1)', 'limite', 's')
text(ax, 44, 5, 'rouge : pas dans N′', 'limite', 's')
save(fig, '57-189')
