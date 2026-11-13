import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def mat(cx, cy, rows, role, cw=6.0, rh=5.6):
    n = len(rows); w, h = 2 * cw, n * rh; x0, y0 = cx - w / 2, cy - h / 2
    for sx, d in ((x0 - 0.6, 1), (x0 + w + 0.6, -1)):
        line(ax, [(sx + 1.3 * d, y0 - 0.4), (sx, y0 - 0.4), (sx, y0 + h + 0.4), (sx + 1.3 * d, y0 + h + 0.4)], 'fixe', lw=0.9)
    for i, row in enumerate(rows):
        text(ax, cx, y0 + h - (i + 0.5) * rh, '    '.join(row), role, 'm')
box(ax, 1, 3, 41, 44, 'fixe', fill=False, dash=True, lw=0.7)
text(ax, 21.5, 43, 'cases séparées', 'fixe', 's', weight='bold')
text(ax, 21.5, 33, 'η puis ρ : ×10 et ×21', 'sujet', 's')
text(ax, 21.5, 13, 'ρ puis η : ×10 et ×21', 'autre', 's')
text(ax, 21.5, 23, '=', 'resultat', 'xl', weight='bold')
box(ax, 45, 3, 42, 44, 'fixe', fill=False, dash=True, lw=0.7)
text(ax, 66, 43, 'cases mélangées', 'fixe', 's', weight='bold')
text(ax, 55.5, 32, '$CA$', 'sujet', 'm')
text(ax, 76.5, 32, '$AC$', 'autre', 'm')
mat(55.5, 21, [['2', '1'], ['3', '4']], 'sujet')
mat(76.5, 21, [['3', '1'], ['4', '3']], 'autre')
text(ax, 66, 21, '≠', 'resultat', 'xl', weight='bold')
save(fig, '58-220')
