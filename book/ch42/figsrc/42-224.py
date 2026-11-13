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
fig, ax = canvas(66)
xs = [14, 44, 74]; y = [46, 30]
for x, l, r, n in zip(xs, [[r'$1$', r'$2$'], [r'$a$', r'$b$'], [r'$x$', r'$y$']], ['sujet', 'fixe', 'autre'], [r'$S$', r'$T$', r'$U$']):
    els(ax, x, y, l, r); setbox(ax, x, y, r, n, w=12)
for i in (0, 1):
    for v in y: arrow(ax, (xs[i] + R + 0.4, v), (xs[i + 1] - R - 0.4, v), 'varie')
text(ax, 29, 56, r'$f$', 'varie', 's'); text(ax, 59, 56, r'$g$', 'varie', 's')
arrow(ax, (xs[0], 20), (xs[2], 20), 'resultat', curve=0.22)
text(ax, 44, 8, r'$g \circ f$ : une flèche par arrivée', 'resultat', 's')
save(fig, '42-224')
