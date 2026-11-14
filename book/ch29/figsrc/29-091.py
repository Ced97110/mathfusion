import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cy, R = 28, 11
xs = [15, 44, 73]
disc(ax, xs[0], cy, R, 'fixe', fill=True)
disc(ax, xs[1], cy, R, 'fixe', fill=False)
poly(ax, [(xs[1], cy)] + arcp(xs[1], cy, R, 20, 100, 24), 'fixe')
line(ax, [(xs[1], cy), (xs[1] + R * math.cos(math.radians(20)), cy + R * math.sin(math.radians(20)))], 'fixe', lw=1.4)
line(ax, [(xs[1], cy), (xs[1] + R * math.cos(math.radians(100)), cy + R * math.sin(math.radians(100)))], 'fixe', lw=1.4)
disc(ax, xs[2], cy, R, 'fixe', fill=False)
poly(ax, arcp(xs[2], cy, R, 35, 145, 30), 'sujet')
line(ax, arcp(xs[2], cy, R, 35, 145, 30), 'sujet', lw=1.6)
text(ax, xs[0], 11, 'disque', 'fixe', 'm')
text(ax, xs[1], 11, 'secteur', 'fixe', 'm')
text(ax, xs[2], 11, 'segment circulaire', 'sujet', 'm', weight='bold')
text(ax, xs[0], 5, 'toute la surface', 'fixe', 's')
text(ax, xs[1], 5, '2 rayons + arc', 'fixe', 's')
text(ax, xs[2] + 1, 5, 'corde + arc', 'sujet', 's')
save(fig, '29-091')
