import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(x0, y0, vals, role, cw=13, ch=11):
    for i in range(2):
        for j in range(2):
            v = vals[i][j]
            box(ax, x0 + j * cw, y0 + (1 - i) * ch, cw, ch, role if v else 'fixe', label=v if v else None, size='m')
mat(4, 20, [['1/2', ''], ['', '1/2']], 'sujet')
mat(58, 20, [['0', '−1'], ['1', '1']], 'autre')
text(ax, 17, 52, r'$R_\theta$ : base habituelle', 'sujet', 's')
text(ax, 71, 52, r'$M$ : base du réseau', 'autre', 's')
arrow(ax, (33, 31), (56, 31), 'varie', lw=1.2)
text(ax, 44.5, 35, r'$P^{-1}\,\cdot\,P$', 'varie', 's')
text(ax, 17, 11, 'trace 1', 'resultat', 'm'); text(ax, 71, 11, 'trace 1', 'resultat', 'm')
text(ax, 44.5, 11, '=', 'resultat', 'l')
save(fig, '74-125')
