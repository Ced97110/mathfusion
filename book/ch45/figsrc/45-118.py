import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(60)
w = 14; gap = 3; x0 = (88 - 2 * w - gap) / 2
for i in range(2): box(ax, x0 + i * (w + gap), 34, w, 10, 'autre', label='$a^{-1}$')
brace(ax, x0, x0 + 2 * w + gap, 34, 'autre', '2 facteurs $a^{-1}$')
arrow(ax, (44, 21), (44, 13), 'fixe')
box(ax, 32, 1, 24, 11, 'autre', label='$a^{-2}$', size='xl')
text(ax, 44, 48.5, "on répète l'inverse", 'autre', 's')
save(fig, '45-118')
