import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
fig, ax = canvas(62)
def row(y, grp, lab):
    xs = [10, 32, 54, 76]; vals = ['4', '6', '18', '17']
    for x, v, r in zip(xs, vals, ('fixe', 'fixe', 'fixe', 'resultat')): box(ax, x - 6, y - 4, 12, 8, r, label=v)
    for k, (a, b, t) in enumerate(zip(xs[:-1], xs[1:], ('$f$', '$g$', '$h$'))):
        arrow(ax, (a + 6.5, y), (b - 6.5, y), 'varie'); text(ax, (a + b) / 2, y + 3.2, t, 'varie', 's')
    x0, x1 = (xs[0] + 6.5, xs[2] - 6.5) if grp == 0 else (xs[1] + 6.5, xs[3] - 6.5)
    brace(ax, x0, x1, y - 6, 'sujet', lab)
row(50, 0, '$g \\circ f$ en bloc')
row(22, 1, '$h \\circ g$ en bloc')
text(ax, 44, 60, 'mêmes actions, même ordre', 'fixe', 's')
save(fig, '42-228')
