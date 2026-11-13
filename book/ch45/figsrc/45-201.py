import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$m$ = 60', 'sujet', 'l')
xs = [14, 30, 58, 74]
for x, v in zip(xs, [2, 2, 3, 5]):
    disc(ax, x, 48, 5, 'fixe', label=str(v), size='m')
for x0, w, v, role in [(9, 26, 4, 'sujet'), (51, 14, 3, 'varie'), (67, 14, 5, 'autre')]:
    box(ax, x0, 22, w, 10, role, label=str(v), size='l', weight='bold')
for x, tx in zip(xs, (22, 22, 58, 74)):
    arrow(ax, (x, 42.5), (tx, 32.5), 'fixe', lw=0.7)
text(ax, 44, 14, 'premiers entre eux deux à deux', 'resultat', 's')
text(ax, 44, 6, 'ℤ/60 ≅ ℤ/4 × ℤ/3 × ℤ/5', 'encre', 'm')
save(fig, '45-201')
