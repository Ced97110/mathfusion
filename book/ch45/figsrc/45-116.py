import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(66)
w = 9; gap = 1.2; tot = 5 * w + 4 * gap; x0 = (88 - tot) / 2
for i in range(5): box(ax, x0 + i * (w + gap), 50, w, w, 'sujet', label='$a$')
brace(ax, x0, x0 + tot, 50, 'sujet', '5 facteurs égaux à $a$')
arrow(ax, (44, 35), (44, 27), 'fixe')
text(ax, 41, 20, '$a$', 'sujet', 'xl')
text(ax, 46.5, 24, '5', 'varie', 'l')
text(ax, 30, 8, "l'élément", 'sujet', 's', ha='right'); arrow(ax, (31, 8.8), (38.5, 17), 'sujet', lw=0.7)
text(ax, 58, 8, 'nombre de facteurs', 'varie', 's', ha='left'); arrow(ax, (57, 8.8), (46.5, 21), 'varie', lw=0.7)
save(fig, '45-116')
