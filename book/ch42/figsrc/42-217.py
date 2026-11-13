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
fig, ax = canvas(60)
xs = [14, 44, 74]; y = 40
for x, n, r, l in zip(xs, [r'$S$', r'$T$', r'$U$'], ['sujet', 'fixe', 'autre'], [r'$3$', r'$b$', r'$x$']):
    disc(ax, x, y, R, r, label=l); box(ax, x - 7, y - 8, 14, 16, r, fill=False); text(ax, x, y + 12, n, r, 'l')
arrow(ax, (xs[0] + 3, y), (xs[1] - 3, y), 'varie'); arrow(ax, (xs[1] + 3, y), (xs[2] - 3, y), 'varie')
text(ax, 29, y + 4, r'$f$', 'varie', 'm'); text(ax, 59, y + 4, r'$g$', 'varie', 'm')
arrow(ax, (xs[0], y - 9), (xs[2], y - 9), 'resultat', curve=0.3)
text(ax, 44, 20, r'$g \circ f : S \to U$', 'resultat', 'm')
text(ax, 44, 5, 'arrivée de f = départ de g', 'fixe', 's')
save(fig, '42-217')
