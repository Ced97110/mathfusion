import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
core, plates, bars, small = [], [], [], []
for i in range(3):
    for j in range(3):
        for k in range(3):
            n = (i == 0) + (j == 0) + (k == 2)
            [core, plates, bars, small][n].append((i, j, k))
role = {c: r for lst, r in ((core, 'fixe'), (plates, 'varie'), (bars, 'autre'), (small, 'resultat')) for c in lst}
for c in sorted(role, key=lambda c: (c[2] - c[0] - c[1], c[2])):
    cubes(ax, [c], (24, 6), 8.0, role[c])
assert (len(core), len(plates), len(bars), len(small)) == (8, 12, 6, 1)
for y, r, lab in [(46, 'fixe', '8 : cube de côté 2'), (36, 'varie', '12 : 3 plaques'), (26, 'autre', '6 : 3 barres'), (16, 'resultat', '1 : petit cube')]:
    box(ax, 50, y, 36, 8, r, True, lab, 's')
text(ax, 68, 6, '8 + 12 + 6 + 1 = 27', 'resultat', 's')
save(fig, '23-107')
