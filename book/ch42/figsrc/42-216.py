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
fig, ax = canvas(62)
xs = [14, 44, 74]
ys = [[40, 22], [40, 22], [40, 22]]
names = [r'$S$', r'$T$', r'$U$']; roles = ['sujet', 'fixe', 'autre']
labs = [[r'$1$', r'$3$'], [r'$a$', r'$b$'], [r'$x$', r'$y$']]
for x, y, n, r, l in zip(xs, ys, names, roles, labs):
    els(ax, x, y, l, r); setbox(ax, x, y, r, n, w=12)
# f : 1->a, 3->b ; g : a->y, b->x
def lk(i, j, a, b, role='fixe', curve=0):
    arrow(ax, (xs[i] + R + 0.4, a), (xs[j] - R - 0.4, b), role, curve=curve)
lk(0, 1, 40, 40, 'fixe'); lk(0, 1, 22, 22, 'varie')
lk(1, 2, 40, 22, 'fixe'); lk(1, 2, 22, 40, 'varie')
text(ax, 29, 49, r'$f$', 'fixe', 'm'); text(ax, 59, 49, r'$g$', 'fixe', 'm')
arrow(ax, (xs[0], 14), (xs[2], 14), 'resultat', curve=0.28)
text(ax, 44, 4, r'$g \circ f$ : $3 \mapsto x$ en une flèche', 'resultat', 's')
save(fig, '42-216')
