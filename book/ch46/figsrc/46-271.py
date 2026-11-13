import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def loop(ax, x, y, role, r=3.0):
    c = (x, y + 1.5)
    ts = [math.radians(-60 + 300 * i / 30) for i in range(31)]
    pts = [(c[0] + r * math.cos(t), c[1] + r * math.sin(t)) for t in ts]
    line(ax, pts[:-1], role, lw=0.9)
    arrow(ax, pts[-2], pts[-1], role, lw=0.9)
xs = [6 + 16.5 * i for i in range(5)]
for y, tag in ((50, 0), (16, 1)):
    for i, x in enumerate(xs):
        c = i + 1
        role = 'sujet' if (tag == 0 and c == 4) or (tag == 1 and c in (4, 5)) else 'fixe'
        box(ax, x, y, 12, 9, role, label=str(c), size='m')
loop(ax, xs[3] + 6, 59 - 0.5, 'varie')
arrow(ax, (xs[3] + 6 - 0.0, 24.8), (xs[4] + 6, 24.8), 'varie', curve=-0.6)
arrow(ax, (xs[4] + 6, 24.8), (xs[3] + 6, 24.8), 'varie', curve=-0.6)
text(ax, 44, 66, '(4) : la carte 4 ne bouge pas', 'sujet', 's')
text(ax, 44, 40, 'c’est le neutre : rien ne change', 'fixe', 's')
text(ax, 44, 8, '(4 5) : deux fois, tout en place', 'varie', 's')
save(fig, '46-271')
