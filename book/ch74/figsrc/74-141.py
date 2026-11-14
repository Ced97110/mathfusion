import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s3 = math.sqrt(3)/2; c75, s75 = math.cos(math.radians(75)), math.sin(math.radians(75))
types = [('quelconque', (6, 1), (1.5, 4.5)), ('rectangle', (6, 0), (0, 4.5)),
         ('losange', (5.5, 0), (5.5*c75, 5.5*s75)), ('carré', (5.5, 0), (0, 5.5)),
         ('hexagonal', (5.5, 0), (2.75, 5.5*s3))]
offs = [(5, 38), (34, 38), (63, 38), (19, 8), (48, 8)]
for (name, a, b), (ox, oy) in zip(types, offs):
    P = lambda i, j: (ox + i*a[0] + j*b[0], oy + i*a[1] + j*b[1])
    poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'varie')
    for i in range(4):
        for j in range(4):
            disc(ax, P(i, j)[0], P(i, j)[1], 0.8, 'sujet')
    text(ax, ox + 11, oy + 21 if oy > 20 else oy + 21, name, 'sujet', 's')
box(ax, 4, 3, 4, 3, 'varie'); text(ax, 10, 4.5, 'maille', 'varie', 's', ha='left')
save(fig, '74-141')
