import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
x0, y0, c = 14, 12, 12
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        role = 'limite' if i == 2 else 'sujet'
        box(ax, x0 + j * c, y0 + (2 - i) * c, c, c, role, label=str(v).replace('-', '\u2212'))
text(ax, x0 + 1.5 * c, y0 + 3 * c + 6, r'$b$ : tableau des $B(e_i, e_j)$', 'sujet', 'm')
text(ax, x0 + 3 * c + 6, y0 + 1.5 * c + 3, r'$\det b = 0$', 'limite', 'l', ha='left')
text(ax, x0 + 3 * c + 6, y0 + 1.5 * c - 4, 'ligne nulle', 'limite', 'm', ha='left')
text(ax, 44, 6, 'dégénérée : (0, 0, 1) est invisible', 'limite', 's')
save(fig, '72-033')
