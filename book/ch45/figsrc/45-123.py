import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(64)
w = 8; gap = 1.2
text(ax, 44, 58, 'règle : $a^{3}\\,a^{0}=a^{3}$', 'fixe', 'm')
for (y, role, ok) in ((38, 'limite', False), (14, 'resultat', True)):
    text(ax, 2, y + w / 2, '$a^{0}=a$' if not ok else '$a^{0}=1$', role, 'm', ha='left')
    for i in range(3): box(ax, 24 + i * (w + gap), y, w, w, 'sujet', label='$a$')
    if ok: box(ax, 24 + 3 * (w + gap), y, w, w, 'resultat', dash=True)
    else: box(ax, 24 + 3 * (w + gap), y, w, w, 'limite', label='$a$')
    text(ax, 24 + 4 * (w + gap) + 2, y + w / 2, '4 facteurs : faux' if not ok else '3 facteurs : vrai', role, 's', ha='left')
save(fig, '45-123')
