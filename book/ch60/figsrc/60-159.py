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
text(ax, 24, 58, 'forme normale', 'sujet', 's')
mat(ax, 24, 48, [[r'$\lambda-2$', '0'], ['0', r'$\lambda-2$']], 'sujet', cw=17)
text(ax, 66, 48, 'déterminant =\nproduit des cases\nde la diagonale', 'encre', 's')
arrow(ax, (15.5, 39), (13, 31), 'varie')
arrow(ax, (32.5, 39), (40, 31), 'varie')
box(ax, 2, 20, 22, 10, 'sujet', label=r'$d_1=\lambda-2$', size='s')
text(ax, 27, 25, r'$\times$', 'encre', 'l')
box(ax, 29, 20, 22, 10, 'sujet', label=r'$d_2=\lambda-2$', size='s')
text(ax, 55, 25, '=', 'encre', 'l')
box(ax, 58, 20, 28, 10, 'resultat', label=r'$f=(\lambda-2)^2$', size='s')
text(ax, 44, 8, r'$f=d_1\,d_2$ : les deux côtés valent $(\lambda-2)^2$', 'resultat', 's')
save(fig, '60-159')
