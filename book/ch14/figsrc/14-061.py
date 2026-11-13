import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [10 + 17 * k for k in range(5)]
vals = ['9', '3', '1', '1/3', '1/9']; exps = [2, 1, 0, -1, -2]
hs = [26, 20, 14, 10, 7]; base = 42; bw = 13
for k, x in enumerate(xs):
    role = 'sujet' if k < 3 else 'resultat'
    box(ax, x - bw / 2, base, bw, hs[k], role, label=vals[k], size='s', r=0.5)
    text(ax, x, base + hs[k] + 3, r'$3^{%d}$' % exps[k], role, 's')
    if k < 4: arrow(ax, (x + bw / 2 + 0.5, base + hs[k] - 3), (xs[k + 1] - bw / 2 - 0.5, base + hs[k + 1] - 3), 'varie')
line(ax, [(2, base), (86, base)], 'fixe')
text(ax, 44, base + 33, '÷ 3 à chaque marche', 'varie', 's')
for k in (3, 4):
    box(ax, xs[k] - bw / 2, base - 12, bw, 10, 'limite', label=('−3', '−9')[k - 3], size='s', dash=True, r=0.5)
text(ax, 62, base - 18, 'si « moins » = opposé', 'limite', 's')
text(ax, 62, base - 24, 'la suite casse', 'limite', 's')
save(fig, '14-061')
