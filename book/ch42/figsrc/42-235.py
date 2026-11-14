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
fig, ax = canvas(74)
def row(ys, tit, first, second, y0):
    text(ax, 44, y0, tit, 'encre', 'm')
    xs = [12, 44, 76]
    for c, (x, L) in enumerate(zip(xs, (['1', '2'], None, [r'$a$', r'$b$']))):
        for k, y in enumerate(ys):
            disc(ax, x, y, 2.8, 'sujet' if c == 0 else ('resultat' if c == 2 else 'fixe'), label=None if L is None else L[k])
    for (xa, xb, (nm, rl)) in ((12, 44, first), (44, 76, second)):
        for y in ys: arrow(ax, (xa + 3.3, y), (xb - 3.3, y), rl)
        text(ax, (xa + xb) / 2, ys[0] + 4, nm, rl, 's')
row([54, 44], '$1_T \\circ \\alpha$', ('$\\alpha$', 'sujet'), ('$1_T$', 'fixe'), 66)
row([24, 14], '$\\alpha \\circ 1_S$', ('$1_S$', 'fixe'), ('$\\alpha$', 'sujet'), 36)
save(fig, '42-235')
