import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(cx, cy, rows, roles, cw=6.0, rh=6.4):
    n, m = len(rows), len(rows[0]); w, h = m * cw, n * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            text(ax, x0 + (j + 0.5) * cw, y0 + h - (i + 0.5) * rh, v, roles[i], 'm')
cy = 44
mat(18, cy, [['1', '0'], ['1', '1']], ['sujet', 'autre'])
text(ax, 33, cy, '×', 'encre', 'l')
mat(44, cy, [['2'], ['1']], ['varie', 'varie'])
text(ax, 55, cy, '=', 'encre', 'l')
mat(67, cy, [['2'], ['3']], ['sujet', 'autre'])
text(ax, 18, 58, '$C$', 'encre', 'm')
text(ax, 44, 58, 'colonne 1 de $A$', 'varie', 's')
text(ax, 71, 58, 'colonne 1 de $CA$', 'resultat', 's')
text(ax, 44, 26, r'$1\times2+0\times1=2$', 'sujet', 'm')
text(ax, 44, 16, r'$1\times2+1\times1=3$', 'autre', 'm')
save(fig, '58-217')
