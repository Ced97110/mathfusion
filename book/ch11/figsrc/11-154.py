import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k = 6.0
xs = [32, 52, 73]   # column centres
heads = [r'$r^1$', r'$r^2$', r'$r^3$']
res = ['C × 2', 'A × 4', 'V × 8']
for x, hd, rs in zip(xs, heads, res):
    text(ax, x, 68, hd, 'encre', 'l')
    text(ax, x, 5, rs, 'resultat', 'l', weight='bold')
text(ax, 6, 52, 'r', 'sujet', 'm'); text(ax, 6, 27, '2r', 'varie', 'm')
# column 1: segments
y1 = 52
line(ax, [(xs[0] - k / 2, y1), (xs[0] + k / 2, y1)], 'sujet', lw=2)
yb = 27
line(ax, [(xs[0] - k, yb), (xs[0], yb)], 'sujet', lw=2)
line(ax, [(xs[0], yb), (xs[0] + k, yb)], 'varie', lw=2)
# column 2: squares
box(ax, xs[1] - k / 2, 49, k, k, 'sujet')
for i in range(2):
    for j in range(2):
        box(ax, xs[1] - k + i * k, 14 + j * k + 0, k, k, 'sujet' if (i, j) == (0, 0) else 'varie', r=0.3, lw=0.6)
# column 3: cubes
cubes(ax, [(0, 0, 0)], (xs[2], 46), k, 'sujet')
cells = [(i, j, kk) for i in range(2) for j in range(2) for kk in range(2) if (i, j, kk) != (0, 0, 0)]
cubes(ax, cells, (xs[2], 14), k, 'varie')
cubes(ax, [(0, 0, 0)], (xs[2], 14), k, 'sujet')
save(fig, '11-154')
