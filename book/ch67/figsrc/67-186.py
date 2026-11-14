import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'un paquet = un polynôme', 'encre', 'm')
rows = [('1, 2, 4, 8', r'$x^{4}+x+1$', 'sujet'),
        ('7, 14, 13, 11', r'$x^{4}+x^{3}+1$', 'autre'),
        ('3, 6, 12, 9', r'$x^{4}+x^{3}+x^{2}+x+1$', 'fixe')]
r = 1.8
for i, (ex, pol, role) in enumerate(rows):
    y = 56 - 20 * i
    cx = 14
    c = [(cx - 5, y + 5), (cx + 5, y + 5), (cx + 5, y - 5), (cx - 5, y - 5)]
    for (px, py) in c:
        disc(ax, px, py, r, role)
    arrow(ax, (c[0][0] + r, c[0][1]), (c[1][0] - r, c[1][1]), role)
    arrow(ax, (c[1][0], c[1][1] - r), (c[2][0], c[2][1] + r), role)
    arrow(ax, (c[2][0] - r, c[2][1]), (c[3][0] + r, c[3][1]), role)
    arrow(ax, (c[3][0], c[3][1] + r), (c[0][0], c[0][1] - r), role)
    text(ax, 26, y, ex, role, 'm', ha='left')
    arrow(ax, (46, y), (53, y), 'fixe')
    text(ax, 56, y, pol, role, 'm', ha='left')
line(ax, [(79, 56), (82, 56), (82, 36), (79, 36)], 'varie', lw=1.0)
text(ax, 85, 46, '≠', 'varie', 'l')
text(ax, 44, 4, 'en tout 3 paquets, 3 polynômes', 'encre', 'm')
save(fig, '67-186')
