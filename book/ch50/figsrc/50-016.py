import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(cx, cy, R, n=12):
    return [(cx + R * math.cos(math.radians(90 - 360 / n * k)), cy + R * math.sin(math.radians(90 - 360 / n * k))) for k in range(n)]

fig, ax = canvas(46)
specs = [(16, [0, 6], 'pas de 6\n2 éléments'), (44, [0, 4, 8], 'pas de 4\n3 éléments'), (72, [0, 2, 4, 6, 8, 10], 'pas de 2\n6 éléments')]
for cx, hrs, cap in specs:
    for k, p in enumerate(ring(cx, 28, 11.5)):
        if k in hrs: disc(ax, p[0], p[1], 2.4, 'sujet', label=str(k), size='s')
        else: disc(ax, p[0], p[1], 1.0, 'fixe')
    text(ax, cx, 8, cap, 'sujet', 's')
save(fig, '50-016')
