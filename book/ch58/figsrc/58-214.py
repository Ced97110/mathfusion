import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def mat(cx, cy, rows, role='encre', size='m', cw=6.0, rh=5.6):
    n = len(rows); w, h = 2 * cw, n * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        text(ax, cx, y0 + h - (i + 0.5) * rh, '    '.join(row), role, size)
box(ax, 6, 46, 34, 26, 'sujet')
text(ax, 23, 67.5, r'$A$ : η d’abord', 'sujet', 's')
mat(23, 55, [['2', '1'], ['1', '3']], 'sujet')
box(ax, 48, 46, 34, 26, 'autre')
text(ax, 65, 67.5, r'$C$ : puis ρ', 'autre', 's')
mat(65, 55, [['1', '0'], ['1', '1']], 'autre')
arrow(ax, (40.5, 59), (47.5, 59), 'varie')
box(ax, 6, 10, 34, 26, 'resultat')
text(ax, 23, 30.5, r'$CA$ : $\eta$ puis $\rho$' + '\nla composée', 'resultat', 's', weight='bold')
mat(23, 19, [['2', '1'], ['3', '4']], 'resultat')
box(ax, 48, 10, 34, 26, 'limite')
text(ax, 65, 30.5, r'$AC$ : $\rho$ puis $\eta$' + '\npas la composée', 'limite', 's', weight='bold')
mat(65, 19, [['3', '1'], ['4', '3']], 'limite')
text(ax, 44, 23, '≠', 'encre', 'l')
save(fig, '58-214')
