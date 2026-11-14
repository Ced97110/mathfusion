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
text(ax, 44, 70, 'une même transformation', 'encre', 'm', weight='bold')
text(ax, 16, 62, 'dans la base 1', 'sujet', 's')
mat(ax, 16, 52, [['2', '0'], ['0', '3']], 'sujet', cw=8)
text(ax, 16, 38, 'dans la base 2', 'sujet', 's')
mat(ax, 16, 28, [['3', '0'], ['0', '2']], 'sujet', cw=8)
arrow(ax, (30, 52), (53, 44), 'varie')
arrow(ax, (30, 28), (53, 36), 'varie')
text(ax, 70, 58, 'forme rationnelle', 'resultat', 's')
mat(ax, 70, 40, [['0', '1'], ['−6', '5']], 'resultat', cw=11)
text(ax, 70, 28, r'compagnon de $\lambda^2-5\lambda+6$', 'resultat', 's')
text(ax, 70, 23, 'coefficients 6 et −5 :', 'resultat', 's')
text(ax, 70, 19, 'dernière ligne, signes changés', 'resultat', 's')
text(ax, 44, 6, 'même transformation : même forme', 'encre', 's')
save(fig, '60-167')
