import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
exps = [3, 2, 1, 0, -1, -2, -3]
w, g = 9, 3.5
xs = [2 + i * (w + g) for i in range(7)]
for i, e in enumerate(exps):
    box(ax, xs[i], 22, w, 10, 'resultat' if e == 0 else 'sujet', label=r'$10^{%d}$' % e, size='s')
    if i < 6: arrow(ax, (xs[i] + w + 0.3, 27), (xs[i + 1] - 0.3, 27), 'varie')
text(ax, 44, 50, 'un pas : exposant − 1, nombre ÷ 10', 'varie', 's')
brace(ax, xs[0], xs[3] + w, 20, 'sujet', 'kilo → base : 3 pas')
brace(ax, xs[3], xs[5] + w, 34, 'autre', 'base → centi : 2 pas', down=False)
save(fig, '11-043')
