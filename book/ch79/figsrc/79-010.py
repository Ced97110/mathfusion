import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
P = {'4': (44, 10), '12': (20, 34), '20': (68, 34), '60': (44, 58)}; r = 3.8
for a, b, c in [('4','12','×3'),('12','60','×5'),('4','20','×5'),('20','60','×3')]:
    (x1, y1), (x2, y2) = P[a], P[b]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], 'varie', lw=1.5)
    mx = (x1 + x2) / 2; text(ax, mx + (-5 if mx < 44 else 5), (y1 + y2) / 2, c, 'varie', 'm')
line(ax, [(44, 10 + r), (44, 58 - r)], 'limite', dash=True, lw=1.2)
text(ax, 44, 40, '×15', 'limite', 'm'); text(ax, 44, 28, 'pas de trait', 'limite', 's')
for k, (x, y) in P.items(): disc(ax, x, y, r, 'sujet' if k in ('4', '60') else 'fixe', label=k, size='s')
save(fig, '79-010')
