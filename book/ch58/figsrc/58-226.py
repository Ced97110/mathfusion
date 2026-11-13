import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def mat(cx, cy, rows, role, cw=6.0, rh=5.6):
    w, h = 2 * cw, 2 * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    t = text(ax, cx, cy, '\n'.join('   '.join(r) for r in rows), role, 'm')
    t.set_linespacing(2.1)
box(ax, 6, 60, 76, 10, 'autre', label=r'$P$ a un inverse $Q$')
box(ax, 6, 32, 76, 10, 'sujet', label=r'$(f_j)$ est une base')
text(ax, 44, 51, r'$\Leftrightarrow$', 'encre', 'xl', weight='bold')
arrow(ax, (24, 59.5), (24, 42.5), 'varie')
text(ax, 21.5, 51, 'colonnes\nde $Q$', 'varie', 's', ha='right')
arrow(ax, (64, 42.5), (64, 59.5), 'varie')
text(ax, 66.5, 51, 'unicité des\nécritures', 'varie', 's', ha='left')
text(ax, 14, 24, '$P$', 'autre', 'm')
mat(14, 13, [['2', '1'], ['1', '1']], 'autre')
text(ax, 28, 13, '×', 'encre', 'l')
text(ax, 42, 24, '$Q$', 'autre', 'm')
mat(42, 13, [['1', '$-1$'], ['$-1$', '2']], 'autre')
text(ax, 56, 13, '=', 'encre', 'l')
mat(70, 13, [['1', '0'], ['0', '1']], 'resultat')
save(fig, '58-226')
