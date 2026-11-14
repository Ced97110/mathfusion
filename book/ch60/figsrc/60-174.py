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
fig, ax = canvas(62)
box(ax, 4, 46, 34, 10, 'sujet', label=r'$f=(\lambda-2)^2$', size='s')
text(ax, 44, 51, r'$=1\times$', 'encre', 's')
box(ax, 50, 46, 34, 10, 'autre', label=r'$m=(\lambda-2)^2$', size='s')
text(ax, 44, 38, r'$f$ est un multiple de $m$ ; $m(A)=0$', 'encre', 's')
mat(ax, 14, 20, [['0', '1'], ['0', '0']], 'autre', cw=8)
text(ax, 29, 20, r'$\times$', 'encre', 'l')
mat(ax, 44, 20, [['0', '1'], ['0', '0']], 'autre', cw=8)
text(ax, 59, 20, '=', 'encre', 'l')
mat(ax, 74, 20, [['0', '0'], ['0', '0']], 'resultat', cw=8)
text(ax, 29, 8, r'$A-2\cdot1$ , deux fois', 'autre', 's')
text(ax, 74, 8, r'$f(A)=0$', 'resultat', 's')
save(fig, '60-174')
