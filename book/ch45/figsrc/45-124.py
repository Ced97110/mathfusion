import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(60)
f = numberline(ax, 20, 68, 16, -2, 2, 1, arrow_right=False)
c = 9.5
for k in (-2, -1, 1, 2): ax.plot([f(k)] * 2, [16, 16], alpha=0)
for i in range(2): box(ax, f(-2) - c - 0.5 + i * (c + 1), 30, c, 9, 'autre', label='$a^{-1}$', size='s')
for i in range(2): box(ax, f(2) - c - 0.5 + i * (c + 1), 30, c, 9, 'sujet', label='$a$')
box(ax, f(0) - 5, 30, 10, 9, 'resultat', label='$1$')
arrow(ax, (f(-2), 29), (f(-2), 20), 'autre'); arrow(ax, (f(2), 29), (f(2), 20), 'sujet'); arrow(ax, (f(0), 29), (f(0), 20), 'resultat')
text(ax, f(-1.5), 46, '$a^{-2}=(a^{-1})^{2}$', 'autre', 's')
text(ax, f(1.8), 46, '$a^{2}$', 'sujet', 's')
text(ax, 44, 3, 'exposant : un entier, même négatif', 'fixe', 's')
save(fig, '45-124')
