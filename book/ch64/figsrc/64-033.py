import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
xs = [3, 24, 45, 66]; w = 17; y = 38; h = 12
labs = [r'$G$ : 8', '4', '2', '1']
for i, (x, l) in enumerate(zip(xs, labs)):
    box(ax, x, y, w, h, 'sujet' if i == 0 else 'fixe', label=l, size='l')
for i in range(3):
    arrow(ax, (xs[i] + w + 0.4, y + h / 2), (xs[i + 1] - 0.4, y + h / 2), 'fixe')
text(ax, 44, 31, 'normal dans le précédent', 'encre', 's')
text(ax, 44, 17, 'normal dans G tout entier', 'encre', 's')
for i in (1, 2, 3):
    cx = xs[i] + w / 2
    text(ax, cx, 25, '✓', 'resultat', 'l', weight='bold')
    ok = i != 2
    text(ax, cx, 11, '✓' if ok else '✗', 'resultat' if ok else 'limite', 'l', weight='bold')
save(fig, '64-033')
