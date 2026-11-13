import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import random
fig, ax = canvas(58)
random.seed(3)
# crystal
for i in range(4):
    for j in range(4): disc(ax, 5 + i*6.5, 20 + j*6.5, 1.5, 'autre')
text(ax, 15, 46, 'cristal', 'autre', 's'); text(ax, 15, 8, 'avec réseau', 'autre', 's')
# quasi-crystal: ordered, order 5
c = (44, 30)
disc(ax, *c, 1.5, 'sujet')
for (r, off, n) in ((6, 0, 5), (10.5, 36, 5), (14.5, 0, 10)):
    for k in range(n):
        a = math.radians(90 + off + k*360/n); disc(ax, c[0] + r*math.cos(a), c[1] + r*math.sin(a), 1.5, 'sujet')
text(ax, 44, 52, 'quasi-cristal', 'sujet', 's'); text(ax, 44, 8, 'ordre sans réseau', 'sujet', 's')
# disorder
pts = []
while len(pts) < 16:
    p = (random.uniform(67, 85), random.uniform(20, 45))
    if all(math.hypot(p[0]-q[0], p[1]-q[1]) > 4.5 for q in pts): pts.append(p)
for p in pts: disc(ax, *p, 1.5, 'fixe')
text(ax, 76, 52, 'désordre', 'fixe', 's'); text(ax, 76, 8, 'sans ordre', 'fixe', 's')
save(fig, '74-182')
