import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
def ed(ax, p, q, role, r=R, curve=0.0):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(76)
xs = [24, 44, 64]; ys = [20, 36, 52]
for i, x in enumerate(xs):
    for j, y in enumerate(ys):
        if i == j: disc(ax, x, y, 3, 'sujet')
        else: disc(ax, x, y, 2.2, 'fixe', fill=False)
line(ax, [(18, 14), (70, 58)], 'varie', dash=True)
for k, v in enumerate('123'):
    text(ax, xs[k], 10, v, 'fixe', 's'); text(ax, 12, ys[k], v, 'fixe', 's')
text(ax, 44, 68, '$S \\times S$', 'encre', 'l')
text(ax, 77, 52, '$(s,s)$', 'sujet', 's'); text(ax, 76, 62, 'diagonale', 'varie', 's')
save(fig, '42-234')
