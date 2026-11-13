import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def mat(cx, cy, rows, role, cw=7.0, rh=6.4):
    w, h = 2 * cw, 2 * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.8, 1), (x0 + w + 0.8, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            text(ax, x0 + (j + 0.5) * cw, y0 + h - (i + 0.5) * rh, v, role, 'm')
text(ax, 18, 46, 'matrice de passage $P$', 'sujet', 's')
mat(18, 33, [['2', '1'], ['1', '1']], 'sujet')
text(ax, 68, 46, '$Q$ : inverse de $P$', 'resultat', 's')
mat(68, 33, [['1', '$-1$'], ['$-1$', '2']], 'resultat')
arrow(ax, (30, 33), (55, 33), 'varie')
text(ax, 42.5, 39, 'déterminant 1', 'varie', 's')
text(ax, 42.5, 27, r'$2\times1-1\times1=1$', 'varie', 's')
text(ax, 44, 10, r'$(1,0)=(2,1)-(1,1)$', 'resultat', 'm')
save(fig, '58-232')
