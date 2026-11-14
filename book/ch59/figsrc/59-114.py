import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def mat(x, y, rows, roles, cw=11, ch=9):
    n = len(rows)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            box(ax, x + j * cw, y + (n - 1 - i) * ch, cw, ch, roles[i][j], r=0.4, label=v, size='m')
y = 32
text(ax, 44, 64, '−2 = (−1) × 2 + 0', 'encre', 'l', weight='bold')
mat(6, y, [['2', '0'], ['−2', '10']], [['fixe', 'fixe'], ['varie', 'varie']])
arrow(ax, (32, y + 4.5), (53, y + 4.5), 'varie', lw=1.2)
text(ax, 42.5, y + 9.5, 'L₂ ← L₂ + L₁', 'varie', 's')
mat(60, y, [['2', '0'], ['0', '10']], [['fixe', 'fixe'], ['resultat', 'varie']])
text(ax, 71, y - 6, '−2 + 2 = 0', 'resultat', 's')
text(ax, 71, y - 12, '10 + 0 = 10', 'varie', 's')
text(ax, 44, 8, 'résultat : diag(2, 10)', 'resultat', 'm', weight='bold')
save(fig, '59-114')
