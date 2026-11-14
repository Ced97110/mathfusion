import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# deux images suffisent : e1 -> (2, 1), e2 -> (1, 3) donnent quatre nombres, et 2 e1 -> (4, 2)
text(ax, 44, 63, 'deux images, quatre nombres', 'encre', 'm', weight='bold')
text(ax, 38, 56, r'image de $e_1$', 'sujet', 's')
text(ax, 62, 56, r'image de $e_2$', 'autre', 's')
x0, y0, w, h, gx = 28, 27, 20, 11, 2
cells = [[2, 1], [1, 3]]
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * (w + gx), y0 + (1 - r) * (h + gx), w, h, 'sujet' if c == 0 else 'autre',
            label=str(cells[r][c]), size='l', weight='bold')
xl, xr = x0 - 2.5, x0 + 2 * w + gx + 2.5
for xx, d in [(xl, 1.8), (xr, -1.8)]:
    line(ax, [(xx + d, y0 - 1.5), (xx, y0 - 1.5), (xx, y0 + 2 * h + gx + 1.5), (xx + d, y0 + 2 * h + gx + 1.5)], 'encre', lw=1.0)
# les autres stocks se déduisent
arrow(ax, (38, y0 - 3), (38, 17), 'varie', lw=1.2)
text(ax, 38, 11.5, r'$2\,e_1 \mapsto 2\,(2,\ 1) = (4,\ 2)$', 'resultat', 's', weight='bold')
text(ax, 38, 4.5, 'les autres stocks se déduisent', 'fixe', 's')
save(fig, '58-020')
