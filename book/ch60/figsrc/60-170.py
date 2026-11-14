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
fig, ax = canvas(74)
mat(ax, 20, 64, [['2', '0'], ['0', '2']], 'sujet', cw=8)
mat(ax, 68, 64, [['2', '1'], ['0', '2']], 'autre', cw=8)
text(ax, 44, 52, r'même $f=(\lambda-2)^2$', 'resultat', 'm')
arrow(ax, (20, 55), (20, 41), 'fixe')
arrow(ax, (68, 55), (68, 41), 'fixe')
text(ax, 44, 40.5, 'forme rationnelle de chacune', 'encre', 's')
mat(ax, 20, 31, [['2', '0'], ['0', '2']], 'sujet', cw=8)
mat(ax, 68, 31, [['0', '1'], ['−4', '4']], 'autre', cw=10)
text(ax, 44, 31, '≠', 'limite', 'xl')
text(ax, 20, 19, r'deux blocs $(2)$ et $(2)$', 'sujet', 's')
text(ax, 68, 19, r'un bloc : compagnon de $(\lambda-2)^2$', 'autre', 's')
text(ax, 44, 7, 'formes rationnelles différentes : non semblables', 'limite', 's')
save(fig, '60-170')
