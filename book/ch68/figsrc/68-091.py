import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'gros points : mots du code', 'fixe', 's')
for row, (d, t) in enumerate([(3, 1), (4, 1), (5, 2)]):
    y = 46 - row * 14
    text(ax, 3, y, rf'$d={d}$, $t={t}$', 'encre', 'm', ha='left')
    xs = [36 + 9 * i for i in range(d + 1)]
    line(ax, [(xs[0], y), (xs[-1], y)], 'fixe')
    for i, x in enumerate(xs):
        role = 'sujet' if i <= t else ('autre' if i >= d - t else 'fixe')
        disc(ax, x, y, 3.8 if i in (0, d) else 2.4, role)
text(ax, 44, 6, r'il faut $d=5$ pour $t=2$', 'resultat', 'm')
save(fig, '68-091')
