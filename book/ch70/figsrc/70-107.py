import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [2, 32, 62]
for x, h in zip(xs, ['abscisse', 'hauteur avec $g$', 'contrôle dans $f$']):
    text(ax, x + 12, 58, h, 'fixe', 's')
rows = [(r'$x=\pm\sqrt{3}$', r'$y=3-2=1$', r'$3+1=4$'), (r'$x=0$', r'$y=0-2=-2$', r'$0+4=4$')]
for i, (a, b, c) in enumerate(rows):
    y = 34 - 24 * i + 10
    y = 40 - 26 * i
    box(ax, xs[0], y, 24, 12, 'varie', label=a, size='s')
    box(ax, xs[1], y, 24, 12, 'autre', label=b, size='s')
    box(ax, xs[2], y, 24, 12, 'resultat', label=c, size='s')
    arrow(ax, (xs[0] + 25, y + 6), (xs[1] - 1, y + 6), 'varie', lw=1.0)
    arrow(ax, (xs[1] + 25, y + 6), (xs[2] - 1, y + 6), 'varie', lw=1.0)
save(fig, '70-107')
