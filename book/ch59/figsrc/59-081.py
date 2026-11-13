import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
base = 16
vals = [4, 2, 1, 0]
names = ['départ', 'tour 1', 'tour 2', 'tour 3']
xs = [6, 26, 46, 66]
for x, v, n in zip(xs, vals, names):
    if v > 0:
        box(ax, x, base, 12, 7 * v, 'sujet')
    else:
        line(ax, [(x, base), (x + 12, base)], 'resultat', lw=1.6)
    text(ax, x + 6, base + 7 * v + 3.5, str(v), 'sujet' if v else 'resultat', 'l')
    text(ax, x + 6, 11, n, 'fixe', 's')
for i in range(3):
    a = (xs[i] + 13, base + 7 * vals[i] - 3)
    b = (xs[i + 1] - 1, base + 7 * vals[i + 1] + 1)
    arrow(ax, a, b, 'varie')
brace(ax, 6, 78, 52, 'fixe', label='au plus 4 tours', down=False, size='s')
text(ax, 44, 3, 'baisse d’au moins 1 par tour', 'varie', 's')
save(fig, '59-081')
