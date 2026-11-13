import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [34 + 16 * k for k in range(4)]
ys = {'h': 50, 'n': 30, 'r': 10}
for y, s, r in [(50, 'heure', 'sujet'), (30, 'nombre', 'autre'), (10, 'rotation', 'varie')]:
    text(ax, 4, y, s, r, 's', ha='left')
heures = ['0', '1', '2', '3']; nombres = ['$1$', '$i$', '$-1$', '$-i$']
for k, x in enumerate(xs):
    box(ax, x - 5, 45, 10, 10, 'sujet', label=heures[k])
    box(ax, x - 5, 25, 10, 10, 'autre', label=nombres[k])
    line(ax, [(x, 45), (x, 35)], 'fixe', dash=True); line(ax, [(x, 25), (x, 15)], 'fixe', dash=True)
    th = math.radians(90 * k + 45)
    pts = [(x + 5 * math.cos(th + j * math.pi / 2), 10 + 5 * math.sin(th + j * math.pi / 2)) for j in range(4)]
    poly(ax, pts, 'varie')
    px, py = pts[0]
    disc(ax, (px + x) / 2 + 0.0, (py + 10) / 2, 1.1, 'sujet')
text(ax, 44, 61, r'$\eta:k\mapsto i^k$ : mêmes quatre cases', 'fixe', 's')
save(fig, '45-217')
