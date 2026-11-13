import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [14 + 16 * i for i in range(5)]
vals = [48, 24, 12, 6, 3]
pts = [48 // d + 1 for d in vals]
assert pts == [2, 3, 5, 9, 17]
yt, yb = 38, 10
line(ax, [(6, yt), (84, yt)], 'fixe', lw=0.6)
line(ax, [(6, yb), (84, yb)], 'fixe', lw=0.6)
for x, v, n in zip(xs, vals, pts):
    ax.add_patch(Rectangle((x - 5, yt), 10, v * 0.2, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
    text(ax, x, yt - 3.5, str(v), 'varie', 's')
    ax.add_patch(Rectangle((x - 5, yb), 10, n * 0.6, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    text(ax, x, yb - 3.5, f'({v})', 'sujet', 's')
text(ax, 44, 57, 'valeur absolue : elle diminue', 'varie', 's')
text(ax, 44, 26.5, 'idéal : il grandit', 'sujet', 's')
save(fig, '56-097')
