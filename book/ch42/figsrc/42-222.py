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
fig, ax = canvas(72)
xs = [14, 44, 74]
Y = [[54, 43, 32], [49.5, 36.5], [54, 43, 32]]
labs = [[r'$1$', r'$2$', r'$3$'], [r'$a$', r'$b$'], [r'$x$', r'$y$', r'$z$']]
for x, y, l, r, n in zip(xs, Y, labs, ['sujet', 'fixe', 'autre'], [r'$S$', r'$T$', r'$U$']):
    els(ax, x, y, l, r); setbox(ax, x, y, r, n, w=12)
for a, b in [(54, 49.5), (43, 49.5), (32, 36.5)]:
    arrow(ax, (xs[0] + R + 0.4, a), (xs[1] - R - 0.4, b), 'varie')
for a, b in [(49.5, 54), (36.5, 32)]:
    arrow(ax, (xs[1] + R + 0.4, a), (xs[2] - R - 0.4, b), 'varie')
text(ax, 29, 61, r'$f$', 'varie', 'm'); text(ax, 59, 61, r'$g$', 'varie', 'm')
text(ax, 44, 22, r'$g \circ f$ existe', 'resultat', 's')
arrow(ax, (xs[2], 23), (xs[0], 23), 'limite', curve=0.0) if False else None
line(ax, [(74, 14), (14, 14)], 'limite', dash=True)
text(ax, 44, 8, r'$f \circ g$ n’existe pas', 'limite', 's')
text(ax, 44, 2.6, 'U n’est pas le départ de f', 'limite', 's')
save(fig, '42-222')
