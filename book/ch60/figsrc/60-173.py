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
fig, ax = canvas(72)
cx1, cx2 = 50, 74
mat(ax, cx1, 62, [['2', '1'], ['0', '2']], 'sujet', cw=6)
mat(ax, cx2, 62, [['2', '0'], ['0', '2']], 'autre', cw=6)
text(ax, 2, 62, 'matrice', 'encre', 's', ha='left')
text(ax, 2, 44, r'degré 1 : $\lambda-2$', 'encre', 's', ha='left')
text(ax, 2, 28, r'degré 2 : $(\lambda-2)^2$', 'encre', 's', ha='left')
box(ax, cx1 - 10, 38, 20, 12, 'limite', label='✗', size='l')
box(ax, cx2 - 10, 38, 20, 12, 'resultat', label='✓', size='l', lw=1.6)
box(ax, cx1 - 10, 22, 20, 12, 'resultat', label='✓', size='l', lw=1.6)
box(ax, cx2 - 10, 22, 20, 12, 'fixe', label='✓', size='l')
text(ax, cx1, 13, r'$m=(\lambda-2)^2$', 'sujet', 's')
text(ax, cx2, 13, r'$m=\lambda-2$', 'autre', 's')
text(ax, 44, 4, 'm : le plus petit degré qui annule A', 'encre', 's')
save(fig, '60-173')
