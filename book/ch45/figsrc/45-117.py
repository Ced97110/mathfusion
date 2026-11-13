import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(64)
w = 8; gap = 1.2; x0 = 30
for r, n in enumerate((3, 2, 1, 0)):
    y = 48 - r * 14
    text(ax, 24, y + w / 2, '$a^{%d}$' % n, 'sujet' if n else 'resultat', 'l', ha='right')
    for i in range(n): box(ax, x0 + i * (w + gap), y, w, w, 'sujet', label='$a$')
box(ax, x0, 48 - 3 * 14, w, w, 'resultat', dash=True)
text(ax, x0 + w + 4, 48 - 3 * 14 + w / 2, '$=1$ : le neutre', 'resultat', 'm', ha='left')
text(ax, x0 + w + 4, 48 - 3 * 14 - 3.2, 'aucun facteur', 'fixe', 's', ha='left')
save(fig, '45-117')
