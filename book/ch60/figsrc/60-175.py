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
fig, ax = canvas(64)
text(ax, 44, 59, r'$A$ de lignes (2, 1) et (0, 2) : $f=(\lambda-2)^2$', 'encre', 's')
box(ax, 2, 38, 26, 11, 'limite', label=r'un facteur $\lambda-2$', size='s')
text(ax, 44, 43.5, r'$A-2\cdot1=$', 'limite', 's')
mat(ax, 64, 43.5, [['0', '1'], ['0', '0']], 'limite', cw=8)
text(ax, 82, 43.5, r'$\neq0$', 'limite', 'm')
box(ax, 2, 14, 26, 11, 'resultat', label=r'$f$ entier', size='s')
text(ax, 44, 19.5, r'$(A-2\cdot1)^2=$', 'resultat', 's')
mat(ax, 64, 19.5, [['0', '0'], ['0', '0']], 'resultat', cw=8)
text(ax, 82, 19.5, r'$=0$', 'resultat', 'm')
text(ax, 44, 4, 'il faut le polynôme entier', 'resultat', 's')
save(fig, '60-175')
