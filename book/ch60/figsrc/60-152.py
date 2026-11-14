import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role='encre', size='m', cw=7.0, P=6.0, lw=0.9):
    r = len(rows); c = len(rows[0]); fs = SIZE[size]
    ls = ((P / (0.3387 * fs)) - 0.2) / 0.8
    for j in range(c):
        t = text(ax, cx + (j - (c - 1) / 2) * cw, cy, '\n'.join(rows[i][j] for i in range(r)), role, size); t.set_linespacing(ls)
    hw = c * cw / 2; hh = r * P / 2 + 0.4
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.2, cy - hh)], role, lw=lw)
fig, ax = canvas(42)
L = r'$\lambda$'; M1 = '−1'
mat(ax, 12, 26, [[L, '0'], ['0', L]], 'varie', cw=8)
text(ax, 25, 26, '−', 'encre', 'l')
mat(ax, 38, 26, [['0', '1'], ['1', '0']], 'fixe', cw=8)
text(ax, 52, 26, '=', 'encre', 'l')
mat(ax, 69, 26, [[L, M1], [M1, L]], 'sujet', cw=10)
text(ax, 12, 12, r'$\lambda 1$', 'varie', 'm')
text(ax, 38, 12, r'$A$ : l’échange', 'fixe', 'm')
text(ax, 69, 12, 'matrice des relations', 'sujet', 's')
save(fig, '60-152')
