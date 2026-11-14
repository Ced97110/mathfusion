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
text(ax, 44, 56, r"$A' = S\,A\,S^{-1}$", 'resultat', 'xl', weight='bold')
mat(ax, 11, 38, [['3', '0'], ['0', '2']], 'autre', cw=7)
text(ax, 24, 38, '=', 'encre', 'l')
mat(ax, 37, 38, [['0', '1'], ['1', '0']], 'varie', cw=7)
mat(ax, 57, 38, [['2', '0'], ['0', '3']], 'sujet', cw=7)
mat(ax, 77, 38, [['0', '1'], ['1', '0']], 'varie', cw=7)
text(ax, 11, 24, r"$A'$", 'autre', 'm')
text(ax, 37, 24, r'$S$', 'varie', 'm')
text(ax, 57, 24, r'$A$', 'sujet', 'm')
text(ax, 77, 24, r'$S^{-1}$', 'varie', 'm')
text(ax, 44, 15, "$A$ et $A'$ : même transformation, deux bases", 'encre', 's')
text(ax, 44, 8, 'S : changement de base (échange les vecteurs)', 'varie', 's')
save(fig, '60-169')
