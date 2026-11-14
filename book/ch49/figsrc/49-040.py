import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
pts = [14, 44, 74]
labs = ['départ', r'après $x$', r'après $xy$']
for p, l in zip(pts, labs):
    disc(ax, p, 30, 3, 'sujet'); text(ax, p, 21.5, l, 'sujet', 's')
for a, b, t in [(0, 1, r'$x$'), (1, 2, r'$y$')]:
    arrow(ax, (pts[a] + 3.5, 32), (pts[b] - 3.5, 32), 'varie', curve=-0.45)
    text(ax, (pts[a] + pts[b]) / 2, 45, t, 'varie', 'm')
for a, b, t in [(2, 1, r'$y^{-1}$'), (1, 0, r'$x^{-1}$')]:
    arrow(ax, (pts[a] - 3.5, 28), (pts[b] + 3.5, 28), 'autre', curve=-0.45)
    text(ax, (pts[a] + pts[b]) / 2, 17, t, 'autre', 'm')
text(ax, 44, 3.5, r'inverse de $xy$ : $y^{-1}x^{-1}$', 'autre', 'm')
text(ax, 44, 56, 'défaire un geste = une lettre de plus', 'encre', 's')
save(fig, '49-040')
