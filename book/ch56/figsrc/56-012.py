import sys, os, random; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, name in [(2, 'plan entier'), (31, 'réseau'), (60, 'nuage au hasard')]:
    text(ax, x + 13, 57, name, 'encre', 's')
box(ax, 2, 16, 26, 36, 'fixe', fill=False)
for i in range(10):
    for j in range(15):
        disc(ax, 4.6 + i * 2.2, 18.6 + j * 2.2, 0.5, 'fixe')
box(ax, 30, 16, 28, 36, 'sujet', fill=False)
dx, dy = 4.0, 4.0 * 5 ** 0.5
xs = [38 + dx * i for i in range(5)]
ys = [24 + dy * j for j in range(3)]
for x in xs:
    line(ax, [(x, ys[0]), (x, ys[-1])], 'fixe', lw=0.4)
for y in ys:
    line(ax, [(xs[0], y), (xs[-1], y)], 'fixe', lw=0.4)
for x in xs:
    for y in ys:
        disc(ax, x, y, 0.9, 'sujet')
box(ax, 60, 16, 26, 36, 'fixe', fill=False)
rnd = random.Random(7)
for _ in range(22):
    disc(ax, rnd.uniform(62, 84), rnd.uniform(18, 50), 0.8, 'fixe')
text(ax, 15, 11, 'points partout', 'fixe', 's')
text(ax, 44, 11, 'écarts réguliers', 'sujet', 's')
text(ax, 73, 11, 'écarts quelconques', 'fixe', 's')
text(ax, 44, 5, 'colonnes : 1, lignes : 2,24', 'sujet', 's')
save(fig, '56-012')
