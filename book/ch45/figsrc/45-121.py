import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(74)
c = 4.6; g = 0.6
def blocks(x, y, sizes, role, outline):
    cur = x
    for s in sizes:
        wd = s * c + (s - 1) * g
        for i in range(s): box(ax, cur + i * (c + g), y, c, c, role, r=0.5)
        if outline: box(ax, cur - 1, y - 1, wd + 2, c + 2, 'varie', fill=False, dash=True, r=0.5)
        cur += wd + 3.5
    return cur - 3.5
for (y, sizes, lab, res) in ((50, (3, 2), '$a^{3}\\,a^{2}$', '$m+n=5$'), (18, (2, 2, 2), '$(a^{2})^{3}$', '$mn=6$')):
    e = blocks(3, y, sizes, 'sujet', True)
    text(ax, 3 + (e - 3) / 2, y + c + 6, lab, 'sujet', 's')
    arrow(ax, (e + 3, y + c / 2), (e + 11, y + c / 2), 'varie')
    n = sum(sizes)
    blocks(e + 14, y, (n,), 'resultat', False)
    text(ax, e + 14 + (n * c + (n - 1) * g) / 2, y + c + 6, res, 'resultat', 's')
text(ax, 44, 38, "associativité : plus de parenthèses", 'varie', 's')
text(ax, 44, 66, 'chaque case = un facteur $a$', 'fixe', 's')
save(fig, '45-121')
