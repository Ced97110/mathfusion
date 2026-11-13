import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = [2, 3, 1]; g = [4, 2, 5]
c = [sum(f[i] * g[k - i] for i in range(3) if 0 <= k - i < 3) for k in range(5)]
assert c == [8, 16, 20, 17, 5]
text(ax, 44, 58, r'$p=2$ : produit $fg$', 'encre', 'm')
xs = [2.5 + i * 16.8 for i in range(5)]
for k in range(5):
    text(ax, xs[k] + 7.5, 48, rf'$x^{k}$' if k > 1 else ('$1$' if k == 0 else '$x$'), 'fixe', 's')
    box(ax, xs[k], 36, 15, 9, 'varie' if c[k] % 2 else 'fixe', label=str(c[k]), size='m')
brace(ax, xs[0], xs[2] + 15, 35, 'fixe', label=r'$2$ divise ces trois', size='s')
arrow(ax, (xs[3] + 7.5, 35.5), (xs[3] + 7.5, 29), 'varie')
text(ax, xs[3] + 7.5, 25, r'$2\nmid17$', 'varie', 'm')
text(ax, xs[3] + 7.5, 13, '$3\\times5$ impair\n$+\\ 1\\times2$ pair\n= impair', 'varie', 's')
assert (3 * 5) % 2 == 1 and (1 * 2) % 2 == 0
save(fig, '56-151')
