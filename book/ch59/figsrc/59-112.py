import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(x, y, rows, roles, cw=11, ch=9):
    n = len(rows)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            box(ax, x + j * cw, y + (n - 1 - i) * ch, cw, ch, roles[i][j], r=0.4, label=v, size='m')
y = 26
text(ax, 44, 60, 'le pivot baisse : 4 → 2', 'encre', 'm', weight='bold')
mat(6, y, [['4', '2'], ['6', '−2']], [['fixe', 'resultat'], ['fixe', 'fixe']])
arrow(ax, (32, y + 9), (53, y + 9), 'varie', lw=1.2)
text(ax, 42.5, y + 14, 'échange C₁ ↔ C₂', 'varie', 's')
mat(60, y, [['2', '4'], ['−2', '6']], [['resultat', 'fixe'], ['fixe', 'fixe']])
text(ax, 17, y - 6, 'plus petit : 2, en (1, 2)', 'resultat', 's')
text(ax, 71, y - 6, 'pivot : 2, en (1, 1)', 'resultat', 's')
save(fig, '59-112')
