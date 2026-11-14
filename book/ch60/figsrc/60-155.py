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
fig, ax = canvas(80)
text(ax, 22, 76, 'matrice 1', 'sujet', 's')
text(ax, 66, 76, 'matrice 2', 'autre', 's')
mat(ax, 22, 64, [['2', '0'], ['0', '2']], 'sujet', cw=8)
mat(ax, 66, 64, [['2', '1'], ['0', '2']], 'autre', cw=8)
text(ax, 44, 51, r'même $f=(\lambda-2)^2$', 'resultat', 'm')
arrow(ax, (22, 56), (22, 47), 'fixe')
arrow(ax, (66, 56), (66, 47), 'fixe')
box(ax, 2, 30, 19, 9, 'sujet', label=r'$d_1=\lambda-2$', size='s')
box(ax, 23, 30, 19, 9, 'sujet', label=r'$d_2=\lambda-2$', size='s')
box(ax, 46, 30, 12, 9, 'autre', label=r'$d_1=1$', size='s')
box(ax, 60, 30, 26, 9, 'autre', label=r'$d_2=(\lambda-2)^2$', size='s')
text(ax, 44, 34.5, '≠', 'encre', 'l')
text(ax, 22, 24, r'produit $=(\lambda-2)^2$', 'resultat', 's')
text(ax, 66, 24, r'produit $=(\lambda-2)^2$', 'resultat', 's')
text(ax, 44, 12, 'même produit, listes des $d_i$ différentes', 'encre', 's')
save(fig, '60-155')
