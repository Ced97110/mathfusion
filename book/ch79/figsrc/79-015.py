import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 24, 54, 'par le calcul', 'encre', 'm'); text(ax, 70, 54, 'par le dessin', 'encre', 'm')
for k, v in enumerate(['12', '24', '36', '48', '60']): box(ax, 2 + k * 8.8, 34, 8, 6, 'resultat' if v == '60' else 'sujet', label=v, size='s')
for k, v in zip([2, 3, 4], ['20', '40', '60']): box(ax, 2 + k * 8.8, 20, 8, 6, 'resultat' if v == '60' else 'autre', label=v, size='s')
line(ax, [(2 + 4 * 8.8 + 4, 26), (2 + 4 * 8.8 + 4, 34)], 'resultat', lw=1.5)
r = 4
D = {'12': (59, 22, 'sujet'), '20': (81, 22, 'autre'), '60': (70, 42, 'resultat')}
for a in ('12', '20'):
    (x1, y1), (x2, y2) = D[a][:2], D['60'][:2]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], 'resultat', lw=1.5)
for k, (x, y, c) in D.items(): disc(ax, x, y, r, c, label=k, size='s')
text(ax, 70, 8, '60 : disque au-dessus', 'resultat', 's')
save(fig, '79-015')
