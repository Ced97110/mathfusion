import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
r = 3.6
C = [('4', 20, 14), ('12', 20, 32), ('60', 20, 50)]
for (a, x, y), (b, x2, y2) in zip(C, C[1:]): line(ax, [(x, y + r), (x2, y2 - r)], 'sujet', lw=1.3)
for k, x, y in C: disc(ax, x, y, r, 'sujet', label=k, size='s')
D = {'4': (64, 14), '12': (50, 32), '20': (78, 32), '60': (64, 50)}
for a, b in [('4','12'),('4','20'),('12','60'),('20','60')]:
    (x1, y1), (x2, y2) = D[a], D[b]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], 'autre', lw=1.3)
for k, (x, y) in D.items(): disc(ax, x, y, r, 'autre', label=k, size='s')
line(ax, [(54, 32), (74, 32)], 'limite', dash=True, lw=1.0)
text(ax, 22, 5, 'en ligne : tout se compare', 'sujet', 's'); text(ax, 66, 5, 'côte à côte : sans chemin', 'autre', 's')
save(fig, '79-011')
