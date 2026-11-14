import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cx, cy, R = 22, 40, 15
disc(ax, cx, cy, R, 'fixe', fill=False)
P = [(cx + R * math.cos(math.pi / 2 - math.pi * k / 6), cy + R * math.sin(math.pi / 2 - math.pi * k / 6)) for k in range(12)]
poly(ax, [P[0], P[4], P[8]], 'sujet')
for k in range(12):
    disc(ax, P[k][0], P[k][1], 1.2, 'sujet' if k in (0, 4, 8) else 'fixe')
for k in (0, 4, 8):
    a = math.pi / 2 - math.pi * k / 6
    text(ax, cx + (R + 5) * math.cos(a), cy + (R + 5) * math.sin(a), str(k), 'sujet', 's')
text(ax, 22, 14, 'horloge à 12', 'fixe', 's')
ys = [66, 48, 30, 12]
labs = [(r'$n_3 = 1$', 'sujet'), ('unique donc normal', 'varie'), ('3 éléments : propre', 'sujet'), ('pas simple', 'resultat')]
for y, (l, r) in zip(ys, labs): box(ax, 48, y, 36, 10, r, label=l, size='s')
for y in ys[1:]: arrow(ax, (66, y + 15), (66, y + 10.8), 'fixe')
for i in range(3): pass
save(fig, '50-180')
