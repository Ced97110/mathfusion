import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(58)
text(ax, 22, 52, 'commutent', 'resultat', 'm'); text(ax, 66, 52, 'ne commutent pas', 'limite', 'm')
for (cx, rows, role) in ((22, (('$ab$', 'r'), ('$ba$', 'r')), 'resultat'), (66, (('$ab$', 's'), ('$ba$', 't')), 'limite')):
    for k, (p, r) in enumerate(rows):
        y = 34 - k * 18
        box(ax, cx - 18, y, 14, 10, 'sujet', label=p)
        arrow(ax, (cx - 3, y + 5), (cx + 5, y + 5), 'varie')
        box(ax, cx + 6, y, 10, 10, role, label=r)
line(ax, [(44, 8), (44, 48)], 'fixe', dash=True)
text(ax, 22, 3, 'même résultat : $ab=ba$', 'resultat', 's')
text(ax, 66, 3, 'résultats différents', 'limite', 's')
save(fig, '45-128')
