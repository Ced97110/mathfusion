import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(60)
w = 10; gap = 3; x0 = (88 - 3 * w - 2 * gap) / 2
xs = row(ax, x0, 34, 3, w, gap, 'sujet', '$a$')
brace(ax, x0, x0 + 3 * w + 2 * gap, 34, 'sujet', '$n=3$ facteurs égaux à $a$')
arrow(ax, (44, 20), (44, 11), 'varie')
box(ax, 34, 0, 20, 10, 'resultat', label='$a^{n}$', size='xl')
text(ax, 62, 5, 'puissance $n$-ième', 'resultat', 's', ha='left')
save(fig, '45-114')
