import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(66)
def example(y, jumps, ends, eq):
    f = numberline(ax, 8, 62, y, -1, 3, 1, labels=False, arrow_right=False)
    for v, lab in ends: text(ax, f(v), y - 3.6, lab, 'fixe', 's')
    for (p, q, role, lab, cv, up) in jumps:
        arrow(ax, (f(p), y + (1.2 if up else -1.2)), (f(q), y + (1.2 if up else -1.2)), role, curve=cv)
        text(ax, (f(p) + f(q)) / 2, y + (10 if up else -10), lab, role, 's')
    text(ax, 66, y + 1, eq, 'resultat', 's', ha='left')
    return f
example(44, [(0, 3, 'sujet', '$a^3$', -0.5, True), (3, 2, 'autre', '$a^{-1}$', -0.7, False)], [(0, '0'), (2, '2'), (3, '3')], r'$a^3a^{-1}=a^2$')
example(14, [(0, 2, 'sujet', '$a^2$', -0.5, True), (2, 0, 'autre', '$a^{-2}$', -0.5, False)], [(0, '0'), (2, '2')], r'$a^2a^{-2}=a^0$')
text(ax, 35, 63.5, 'les nombres sont des exposants', 'fixe', 's')
save(fig, '45-126')
