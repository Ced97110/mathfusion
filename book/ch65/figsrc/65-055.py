import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 65, r'$d=\prod(r_i-r_j)^2$ : un facteur nul suffit', 'sujet', 's', weight='bold')
cases = [([1, 1, 2], 'racines 1, 1, 2', 'varie', 44), ([1, 2, 3], 'racines 1, 2, 3', 'resultat', 14)]
for vals, name, role, y in cases:
    prs = [(0, 1), (0, 2), (1, 2)]
    fs = [(vals[i] - vals[j]) ** 2 for i, j in prs]
    tot = fs[0] * fs[1] * fs[2]
    text(ax, 44, y + 17, name, role, 's', weight='bold')
    for k, ((i, j), f) in enumerate(zip(prs, fs)):
        x = 4 + k * 19
        zero = f == 0
        box(ax, x, y, 17, 11, 'varie' if zero else 'fixe', label='(%d−%d)² = %d' % (vals[i], vals[j], f) if False else '(%d−%d)²' % (vals[i], vals[j]), size='s', lw=1.6 if zero else 0.8)
        text(ax, x + 8.5, y - 3.5, '= %d' % f, 'varie' if zero else 'fixe', 's', weight='bold' if zero else 'normal')
    arrow(ax, (62, y + 5.5), (66, y + 5.5), 'fixe', lw=0.8)
    box(ax, 67, y, 19, 11, role, label='d = %d' % tot, size='s', weight='bold')
    assert (tot == 0) == (role == 'varie')
save(fig, '65-055')
