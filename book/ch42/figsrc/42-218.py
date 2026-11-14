import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R=2.6
def els(ax, x, ys, labels, role, dashed=False):
    for y, l in zip(ys, labels):
        disc(ax, x, y, R, role, label=l)
def setbox(ax, x, ys, role, name=None, w=14, pad=5):
    box(ax, x - w/2, min(ys) - pad, w, max(ys) - min(ys) + 2*pad, role, fill=False)
    if name: text(ax, x, max(ys) + pad + 2.6, name, role, 'l')
def link(ax, xa, ya, xb, yb, role='varie', curve=0.0):
    arrow(ax, (xa + R + 0.4, ya), (xb - R - 0.4, yb), role, curve=curve)
fig, ax = canvas(58)
xs = [12, 44, 76]
for x, l, r, n in zip(xs, [r'$4$', r'$6$', r'$18$'], ['sujet', 'fixe', 'resultat'], [r'$s$', r'$f(s)$', r'$g(f(s))$']):
    box(ax, x - 9, 22, 18, 12, r, label=l, size='l'); text(ax, x, 15, n, r, 's')
arrow(ax, (xs[0] + 10, 28), (xs[1] - 10, 28), 'varie'); arrow(ax, (xs[1] + 10, 28), (xs[2] - 10, 28), 'varie')
text(ax, 28, 33, r'$f$ : $+\,2$', 'varie', 's'); text(ax, 60, 33, r'$g$ : $\times\,3$', 'varie', 's')
text(ax, 44, 48, r'$(g \circ f)(s) = g(f(s))$', 'encre', 'l')
text(ax, 44, 5, 'deux temps : f, puis g', 'varie', 's')
save(fig, '42-218')
