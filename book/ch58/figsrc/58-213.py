import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
CW, RH = 6.0, 6.4
def grid(cx, cy, rows, roles):
    w, h = 2 * CW, 2 * RH; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.8, 1), (x0 + w + 0.8, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            text(ax, x0 + (j + 0.5) * CW, y0 + h - (i + 0.5) * RH, v, roles[i][j])
    return x0, y0, w, h
cy = 34
x0, y0, w, h = 16 - CW, cy - RH, 2 * CW, 2 * RH
box(ax, x0 + 0.3, y0 + 0.3, w - 0.6, RH - 0.6, 'sujet')            # ligne 2 de C
x1, y1 = 44 - CW, cy - RH
box(ax, x1 + CW + 0.4, y1 + 0.3, CW - 0.8, 2 * RH - 0.6, 'autre')      # colonne 2 de A
grid(16, cy, [['1', '0'], ['1', '1']], [['fixe', 'fixe'], ['sujet', 'sujet']])
grid(44, cy, [['2', '1'], ['1', '3']], [['fixe', 'autre'], ['fixe', 'autre']])
text(ax, 16, 21.5, 'ligne 2 de $C$', 'sujet', 's')
text(ax, 44, 21.5, 'colonne 2 de $A$', 'autre', 's')
arrow(ax, (54, cy), (66, cy), 'varie')
box(ax, 67, cy - 5, 14, 10, 'resultat', label='4', weight='bold')
text(ax, 74, 21.5, 'case (2, 2) de $CA$', 'resultat', 's')
text(ax, 44, 10, r'$1\times1+1\times3=4$', 'encre', 'm')
save(fig, '58-213')
