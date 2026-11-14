import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# ligne 1 : sur ℤ, le sous-module 4ℤ
text(ax, 44, 62, 'sur ℤ : le sous-module 4ℤ', 'resultat', 's', weight='bold')
f = lambda v: 8 + v * 6.0
for v in range(0, 13):
    ok = v % 4 == 0
    disc(ax, f(v), 52, 2.2 if ok else 1.0, 'sujet' if ok else 'fixe', label=str(v) if ok else None, size='s')
line(ax, [(f(0), 52), (f(12), 52)], 'fixe', lw=0.4)
arrow(ax, (f(0), 46), (f(4), 46), 'varie', lw=1.4)
text(ax, f(2), 41.5, 'base (4)', 'varie', 's')
box(ax, 62, 38, 24, 7, 'resultat', label='libre', size='s')
# changement d'anneau
arrow(ax, (44, 34), (44, 27), 'encre', lw=1.0)
text(ax, 52, 30.5, 'autre anneau', 'encre', 's', ha='left')
# ligne 2 : sur ℤ/4ℤ, le sous-module {0, 2}
xs = [14 + i * 20 for i in range(4)]
for i, x in enumerate(xs):
    inside = i in (0, 2)
    disc(ax, x, 18, 4.2, 'limite' if inside else 'fixe', label=str(i), size='s')
text(ax, 44, 7, 'sur ℤ/4ℤ : {0, 2}, 2 × 2 = 0', 'limite', 's')
save(fig, '58-323')
