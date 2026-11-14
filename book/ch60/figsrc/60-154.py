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
text(ax, 24, 68, 'départ', 'sujet', 's')
mat(ax, 24, 58, [[r'$\lambda-2$', '0'], ['0', r'$\lambda-3$']], 'sujet', cw=17)
text(ax, 66, 63, 'premiers entre eux :', 'encre', 's')
text(ax, 66, 57, r'$(\lambda-2)-(\lambda-3)=1$', 'resultat', 's')
arrow(ax, (24, 49), (24, 36), 'varie')
text(ax, 44, 42.5, 'opérations sur lignes et colonnes', 'varie', 's', ha='left')
text(ax, 32, 28, 'forme normale', 'sujet', 's')
mat(ax, 32, 19, [['1', '0'], ['0', r'$(\lambda-2)(\lambda-3)$']], 'sujet', cw=28)
text(ax, 44, 4, r'$d_1=(\lambda-2)(\lambda-3)$', 'resultat', 'm')
save(fig, '60-154')
