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
fig, ax = canvas(66)
def row(y, grp, tit, lab, role):
    xs = [14, 34, 54]
    text(ax, 40, y + 11, tit, 'encre', 'm')
    for x, v in zip(xs, '234'): disc(ax, x, y, R, 'fixe', label=v)
    a, b = (xs[0], xs[1]) if grp == 0 else (xs[1], xs[2])
    brace(ax, a - R, b + R, y - 5, role, lab)
    text(ax, 76, y, '= 9', 'resultat', 'l')
row(46, 0, '$(2+3)+4$', '$2+3=5$', 'sujet')
row(16, 1, '$2+(3+4)$', '$3+4=7$', 'autre')
text(ax, 76, 31, 'même résultat', 'resultat', 's')
save(fig, '42-230')
