import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
S = 12
def sq(x, y, n, role='sujet', pos=None):
    poly(ax, [(x - S/2, y - S/2), (x + S/2, y - S/2), (x + S/2, y + S/2), (x - S/2, y + S/2)], role)
    cx, cy = {1: (S/2 - 2.4, S/2 - 2.4), 2: (-S/2 + 2.4, S/2 - 2.4), 3: (-S/2 + 2.4, -S/2 + 2.4), 4: (S/2 - 2.4, -S/2 + 2.4)}[n]
    disc(ax, x + cx, y + cy, 2.2, 'varie', label=str(n), size='s')
text(ax, 44, 79, r'$s\,r = r^3\,s$ : le coin 1 va en 3', 'encre', 'm')
cols = [14, 44, 74]
chains = [(70 - 0, [1, 2, 3], [r'$r$', r'$s$'], 'sujet'), (36, [1, 4, 3], [r'$s$', r'$r^3$'], 'autre')]
for (y, ns, labs, role), ytxt in zip([(60, [1, 2, 3], [r'$r$', r'$s$'], 'sujet'), (28, [1, 4, 3], [r'$s$', r'$r^3$'], 'autre')], [0, 0]):
    for k, n in enumerate(ns):
        sq(cols[k], y, n, role if k < 2 else 'resultat')
    for k in range(2):
        arrow(ax, (cols[k] + 8, y), (cols[k + 1] - 8, y), 'varie', lw=1.2)
        text(ax, (cols[k] + cols[k + 1]) / 2, y + 4.5, labs[k], 'varie', 'm')
text(ax, 44, 72, r"$r$ d'abord, puis $s$", 'sujet', 's'); text(ax, 44, 40, r"$s$ d'abord, puis $r^3$", 'autre', 's')
text(ax, 44, 12, 'mêmes arrivées : 3 = 3', 'resultat', 'm')
save(fig, '44-138')
