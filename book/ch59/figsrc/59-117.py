import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(x, y, rows, roles, cw=11, ch=9):
    n = len(rows)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            box(ax, x + j * cw, y + (n - 1 - i) * ch, cw, ch, roles[i][j], r=0.4, label=v, size='m')
y = 30
text(ax, 17, y + 23, 'P : 3 opérations', 'fixe', 's')
mat(6, y, [['−1', '3'], ['1', '−2']], [['fixe', 'fixe'], ['fixe', 'fixe']])
arrow(ax, (32, y + 9), (53, y + 9), 'varie', lw=1.2)
text(ax, 42.5, y + 14, 'inverse', 'varie', 's')
text(ax, 71, y + 23, 'P⁻¹', 'varie', 's')
mat(60, y, [['2', '3'], ['1', '1']], [['varie', 'varie'], ['varie', 'varie']])
text(ax, 71, y - 6, 'ligne 1 : e′₁ = (2, 3)', 'varie', 's')
text(ax, 71, y - 12, 'ligne 2 : e′₂ = (1, 1)', 'varie', 's')
save(fig, '59-117')
