import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda x: x ** 5 - 6 * x ** 3 - 27 * x - 3
pts = (-3, -2, 0, 4)
vals = [f(p) for p in pts]
assert vals == [-3, 67, -3, 529]
xs = [4 + i * 22 for i in range(4)]
for x, p, v in zip(xs, pts, vals):
    box(ax, x, 40, 15, 11, 'varie', label=f'$f({p})$'.replace('-', '−'), size='s')
    box(ax, x, 22, 15, 13, 'fixe' if v < 0 else 'resultat', label=str(v).replace('-', '−'), weight='bold')
for i in range(3):
    xm = xs[i] + 15 + 3.5
    arrow(ax, (xm - 3, 28.5), (xm + 3, 28.5), 'sujet')
    disc(ax, xm, 44, 1.6, 'sujet')
text(ax, 44, 12, 'une racine par changement de signe', 'sujet', 'm')
text(ax, 44, 58, r'$f$ en quatre points', 'encre', 'm')
save(fig, '64-176')
