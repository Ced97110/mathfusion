import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(58)
w = 9; gap = 1; bg = 5; x0 = (88 - (6 * w + 3 * gap + 2 * bg)) / 2
xs = []
for b in range(3):
    xb = x0 + b * (2 * w + gap + bg)
    box(ax, xb - 1.5, 28.5, 2 * w + gap + 3, w + 3, 'varie', fill=False, dash=True)
    for i in range(2):
        box(ax, xb + i * (w + gap), 30, w, w, 'sujet', label='$a$')
    text(ax, xb + w + gap / 2, 44, '$a^{2}$', 'varie', 's')
text(ax, 44, 52, '$n=3$ blocs de $m=2$', 'varie', 's')
arrow(ax, (44, 26), (44, 18), 'fixe')
tot = 6 * w + 3 * gap + 2 * bg
brace(ax, x0, x0 + tot, 14, 'resultat', '$3\\times2=6$ facteurs : $a^{6}$')
save(fig, '45-120')
