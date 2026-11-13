import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s = 22.0; ox, oy = 6, 10
P = lambda x, y: (ox + x*s, oy + y*s)
poly(ax, [P(1,0), P(2,1), P(1,2), P(0,1)], 'varie')
line(ax, [P(1,0), P(1,2)], 'encre', lw=0.7); line(ax, [P(0,1), P(2,1)], 'encre', lw=0.7)
poly(ax, [P(0,0), P(1,0), P(1,1), P(0,1)], 'sujet', fill=False, lw=1.6)
for n, (x, y) in enumerate(((2/3, 2/3), (4/3, 2/3), (2/3, 4/3), (4/3, 4/3)), 1):
    text(ax, *P(x, y), str(n), 'varie', 'm')
text(ax, P(0.5, 0.18)[0], P(0.5, 0.18)[1], 'aire 1', 'sujet', 's')
text(ax, P(0.5,0)[0], 5, 'carré de côté 1', 'sujet', 's')
text(ax, 66, 27, 'carré sur la\ndiagonale :\n4 triangles égaux', 'varie', 's')
arrow(ax, (50, 27), P(1.6, 1.0), 'varie')
save(fig, '22-012')
