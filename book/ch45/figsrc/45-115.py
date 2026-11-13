import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(62)
w = 9; gap = 1.2; tot = 5 * w + 4 * gap; x0 = (88 - tot) / 2
for i in range(3): box(ax, x0 + i * (w + gap), 44, w, w, 'sujet', label='$a$')
for i in range(3, 5): box(ax, x0 + i * (w + gap), 44, w, w, 'varie', label='$a$')
brace(ax, x0, x0 + 3 * w + 2 * gap, 44, 'sujet', '$a^{3}$ : 3 cases')
brace(ax, x0 + 3 * (w + gap), x0 + tot, 44, 'varie', '$a^{2}$ : 2 cases')
text(ax, 44, 29, 'on efface la séparation', 'fixe', 's')
arrow(ax, (44, 26.5), (44, 20), 'fixe')
for i in range(5): box(ax, x0 + i * (w + gap), 9, w, w, 'resultat', label='$a$')
brace(ax, x0, x0 + tot, 9, 'resultat', '$a^{5}$ : 5 cases')
save(fig, '45-115')
