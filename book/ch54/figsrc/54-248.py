import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = lambda v: v ** 3 - 2 * v ** 2 + 4
assert [f(v) for v in (-4, -2, -1, 1, 2, 4)] == [-92, -12, 1, 3, 4, 36]
text(ax, 44, 72, r'racine $p/q$ de $x^3-2x^2+4$', 'sujet', 's')
box(ax, 4, 54, 24, 10, 'sujet', label=r'$q=1$')
box(ax, 32, 54, 24, 10, 'sujet', label=r'$p$ divise 4')
box(ax, 60, 54, 24, 10, 'sujet', label=r'$\pm1,\pm2,\pm4$')
arrow(ax, (28, 59), (32, 59), 'varie'); arrow(ax, (56, 59), (60, 59), 'varie')
text(ax, 44, 47, r'candidat : valeur de $f$', 'fixe', 's')
for i, v in enumerate((-4, -2, -1, 1, 2, 4)):
    col, row = i % 3, i // 3
    x = 4 + col * 28.5
    y = 34 - row * 14
    box(ax, x, y, 25, 10, 'limite', label=(f'{v} : {f(v)}').replace('-', '−'))
text(ax, 44, 6, 'aucune valeur nulle : tous écartés', 'limite', 's')
save(fig, '54-248')
