import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(52)
w = 7; gap = 1
for (m, n, y) in ((2, 3, 32), (2, 1, 10)):
    for i in range(m): box(ax, 4 + i * (w + gap), y, w, w, 'sujet', label='$a$')
    for i in range(m, m + n): box(ax, 4 + i * (w + gap) + 2, y, w, w, 'varie', label='$a$')
    text(ax, 52, y + w / 2, '$a^{%d}a^{%d}=a^{%d}$' % (m, n, m + n), 'resultat', 'm', ha='left')
    text(ax, 52, y - 3.5, '$%d+%d=%d$ facteurs' % (m, n, m + n), 'resultat', 's', ha='left')
text(ax, 44, 48, "les exposants s'additionnent", 'fixe', 's')
save(fig, '45-119')
