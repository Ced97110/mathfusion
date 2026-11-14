import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cs = [10, 24, 38]; nums = (2, 3, 4)
text(ax, 44, 70, r'un terme dans $x-2$, $x-3$, $x-4$', 'encre', 's')
# lignes : quels facteurs donnent le terme avec moins (orange)
rows = [((0, 0, 0), 56, r'$k=0$, $(-1)^0=+1$'),
        ((1, 0, 0), 40, r'$k=1$, $(-1)^1=-1$'),
        ((1, 1, 0), 24, r'$k=2$, $(-1)^2=+1$')]
for pick, y, lab in rows:
    for c, n, p in zip(cs, nums, pick):
        if p: disc(ax, c, y, 5, 'varie', label=rf'$-{n}$', size='m')
        else: disc(ax, c, y, 5, 'fixe', label=r'$x$', size='m')
    text(ax, 50, y, lab, 'varie' if sum(pick) else 'fixe', 's', ha='left')
text(ax, 44, 8, r'$k=1$ : $-2x^2-3x^2-4x^2=-9x^2$', 'resultat', 's')
save(fig, '55-084')
