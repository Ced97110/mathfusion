import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def mat(x, y, rows, roles, cw=11, ch=9):
    n = len(rows)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            box(ax, x + j * cw, y + (n - 1 - i) * ch, cw, ch, roles[i][j], r=0.4, label=v, size='m')
y = 30
mat(6, y, [['4', '6'], ['6', '4']], [['fixe', 'varie'], ['fixe', 'varie']])
text(ax, 11.5, y + 22, 'C₁', 'fixe', 's')
text(ax, 22.5, y + 22, 'C₂', 'varie', 's')
arrow(ax, (32, y + 9), (53, y + 9), 'varie', lw=1.2)
text(ax, 42.5, y + 14, 'C₂ ← C₂ − C₁', 'varie', 's')
mat(60, y, [['4', '2'], ['6', '−2']], [['fixe', 'varie'], ['fixe', 'varie']])
text(ax, 82 - 5.5, y + 22, 'C₂', 'varie', 's')
text(ax, 71, y - 6, '6 − 4 = 2', 'varie', 's')
text(ax, 71, y - 12, '4 − 6 = −2', 'varie', 's')
save(fig, '59-109')
