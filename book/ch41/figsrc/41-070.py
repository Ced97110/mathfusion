import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k = 3.0
cases = [((1, 3), (4, 2), 10), ((2, 0), (0, 5), 0), ((3, 4), (3, 4), 25)]
for r, (u, v, res) in enumerate(cases):
    assert u[0] * v[0] + u[1] * v[1] == res
    y = 56 - r * 22
    text(ax, 2, y, r'$\langle %d;%d\rangle\cdot\langle %d;%d\rangle$' % (u + v), 'sujet', 's', ha='left')
    x = 36
    for i, role in ((0, 'sujet'), (1, 'autre')):
        w, h = k * u[i], k * v[i]
        if w > 0 and h > 0:
            box(ax, x, y - 6, w, h, role, r=0.01, lw=0.7)
        else:
            line(ax, [(x, y - 6), (x + w, y - 6 + h)], role, lw=1.4)
        x += max(w, 0.0) + 4
    text(ax, 86, y, r'$%d\times %d+%d\times %d=%d$' % (u[0], v[0], u[1], v[1], res), 'resultat', 's', ha='right')
text(ax, 44, 68, 'aires : une par produit, puis on les additionne', 'fixe', 's')
save(fig, '41-070')
