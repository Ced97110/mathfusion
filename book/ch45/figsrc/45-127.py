import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(60)
text(ax, 44, 54, 'on cherche $x$ avec $2x=1$ (mod 4)', 'fixe', 's')
w = 19; gap = 2.5; x0 = (88 - 4 * w - 3 * gap) / 2
for i, (x, r) in enumerate(((0, 0), (1, 2), (2, 0), (3, 2))):
    box(ax, x0 + i * (w + gap), 30, w, 12, 'limite', label='$2\\times%d=%d$' % (x, r), size='s')
    text(ax, x0 + i * (w + gap) + w / 2, 45.5, '$x=%d$' % x, 'fixe', 's')
text(ax, 44, 22, 'aucun résultat ne vaut $1$', 'limite', 's')
arrow(ax, (44, 19), (44, 13), 'limite')
box(ax, 26, 1, 36, 11, 'limite', label='pas de $2^{-1}$', size='m')
save(fig, '45-127')
