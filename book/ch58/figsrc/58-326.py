import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = lambda v: 8 + v * 6.0
text(ax, 44, 60, 'deux sous-modules non nuls de ℤ', 'encre', 's')
text(ax, 6, 50, '2ℤ', 'sujet', 's', ha='left', weight='bold')
text(ax, 6, 33, '3ℤ', 'autre', 's', ha='left', weight='bold')
for v in range(0, 13):
    if v % 2 == 0:
        disc(ax, f(v), 44, 2.3, 'sujet', label=str(v), size='s')
    if v % 3 == 0:
        disc(ax, f(v), 27, 2.3, 'autre', label=str(v), size='s')
for v in (6, 12):
    line(ax, [(f(v), 41.5), (f(v), 29.5)], 'limite', lw=1.2, dash=True)
text(ax, f(6) + 14, 36, '6 dans les deux', 'limite', 's')
box(ax, 8, 4, 72, 14, 'limite', label='intersection ≠ {0}\nℤ n’est pas somme directe', size='s')
save(fig, '58-326')
