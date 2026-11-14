import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 54, 'exposant 2', 'autre', 'm')
text(ax, 64, 54, 'exposant 3', 'sujet', 'm')
for i in range(2):
    for j in range(2):
        box(ax, 10 + 8 * i, 20 + 8 * j, 8, 8, 'autre', r=0.4)
cubes(ax, [(i, j, k) for i in range(2) for j in range(2) for k in range(2)], (64, 18), 8.0, 'sujet')
text(ax, 22, 12, '2 × 2 = 4', 'resultat', 'm')
text(ax, 22, 6, 'surface : 2 facteurs', 'autre', 's')
text(ax, 64, 12, '2 × 2 × 2 = 8', 'resultat', 'm')
text(ax, 64, 6, 'cube : 3 facteurs', 'sujet', 's')
save(fig, '11-130')
