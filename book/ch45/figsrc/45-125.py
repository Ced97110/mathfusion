import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(64)
w = 10; gap = 2; x0 = (88 - 4 * w - 3 * gap) / 2; y = 34
X = [x0 + i * (w + gap) for i in range(4)]
for i in range(2): box(ax, X[i], y, w, w, 'sujet', label='$a$')
for i in range(2, 4): box(ax, X[i], y, w, w, 'autre', label='$a^{-1}$', size='s')
def bracket(i, j, h, lab):
    xa, xb = X[i] + w / 2, X[j] + w / 2
    line(ax, [(xa, y + w), (xa, y + w + h), (xb, y + w + h), (xb, y + w)], 'varie', lw=0.9)
    text(ax, (xa + xb) / 2, y + w + h + 2.2, lab, 'varie', 's')
bracket(1, 2, 3, '1re paire : s\'annule')
bracket(0, 3, 9, '2e paire : s\'annule')
brace(ax, X[0], X[1] + w, y, 'sujet', '$a^{2}$')
brace(ax, X[2], X[3] + w, y, 'autre', '$a^{-2}$')
arrow(ax, (44, 15), (44, 8), 'resultat')
box(ax, 34, 0, 20, 7, 'resultat', label='$1$ : neutre', size='s')
save(fig, '45-125')
