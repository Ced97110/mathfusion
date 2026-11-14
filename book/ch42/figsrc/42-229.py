import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
fig, ax = canvas(66)
xs = [10, 31, 52, 73]; vals = ['1', '2', '4', '7']
text(ax, xs[0], 62, '$S$', 'sujet', 'l'); text(ax, xs[3], 62, '$V$', 'sujet', 'l')
for x, v, r in zip(xs, vals, ('sujet', 'fixe', 'fixe', 'resultat')): disc(ax, x, 50, R, r, label=v)
for a, b, t in zip(xs[:-1], xs[1:], ('$f$', '$g$', '$h$')):
    link(ax, (a, 50), (b, 50), 'varie'); text(ax, (a + b) / 2, 54.5, t, 'varie', 's')
brace(ax, xs[1], xs[3], 44, 'autre', '$(h\\circ g)\\circ f$', depth=1.6)
brace(ax, xs[0], xs[2], 31, 'sujet', '$h\\circ(g\\circ f)$', down=True, depth=1.6)
text(ax, 44, 10, 'pour chaque $s$ : même image', 'resultat', 'm')
save(fig, '42-229')
