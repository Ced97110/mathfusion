import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cw, ch = 9.0, 8.0
def cells(x, y, vals, role='sujet'):
    for i, v in enumerate(vals): box(ax, x + i * cw, y, cw, ch, role, label=v, r=0.6)
rows = [(40, r'$\mathbb{Z}^{(2)}$', ['2', '1']),
        (24, r'$\mathbb{Z}^{(3)}$', ['2', '1', '4']),
        (8, r'$R^{(n)}$', [r'$x_1$', '…', r'$x_n$'])]
for y, lab, vals in rows:
    text(ax, 14, y + ch / 2, lab, 'sujet', 'l')
    cells(30, y, vals, 'sujet' if vals[0] != r'$x_1$' else 'autre')
text(ax, 72, 40 + ch / 2, '2 cases', 'fixe', 's')
text(ax, 72, 24 + ch / 2, '3 cases', 'fixe', 's')
text(ax, 72, 8 + ch / 2, r'$n$ cases', 'fixe', 's')
text(ax, 44, 55, 'les listes de n entiers (ou de R)', 'encre', 's')
save(fig, '58-033')
