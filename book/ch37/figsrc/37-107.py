import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
vals = [[1, 1, 1], [7, 1, 1], [6, 5, 1]]
cw = 9.0; gx, gy = 5, 12
for r in range(3):
    for c in range(3):
        box(ax, gx + c * cw, gy + (2 - r) * cw, cw, cw, 'fixe' if c == 2 else 'sujet', label=str(vals[r][c]), size='m')
line(ax, [(gx - 1.5, gy - 1), (gx - 3, gy - 1), (gx - 3, gy + 3 * cw + 1), (gx - 1.5, gy + 3 * cw + 1)], 'encre', lw=1.0)
line(ax, [(gx + 3 * cw + 1.5, gy - 1), (gx + 3 * cw + 3, gy - 1), (gx + 3 * cw + 3, gy + 3 * cw + 1), (gx + 3 * cw + 1.5, gy + 3 * cw + 1)], 'encre', lw=1.0)
bx, bw = 46, 40
box(ax, bx, 34, bw, 10, 'sujet', label='déterminant : 24', size='s')
box(ax, bx, 19, bw, 10, 'fixe', label='somme de 3 produits : 24', size='s')
box(ax, bx, 3, bw, 10, 'resultat', label='aire : 12', size='s')
for yy in (30.6, 32.4): line(ax, [(bx + bw / 2 - 4, yy), (bx + bw / 2 + 4, yy)], 'encre', lw=1.0)
arrow(ax, (bx + bw / 2, 19), (bx + bw / 2, 13), 'varie')
text(ax, bx + bw / 2 + 3, 16, r'$\frac{1}{2}\,|24|$', 'varie', 's', ha='left')
arrow(ax, (gx + 3 * cw + 4, 39), (bx, 39), 'sujet')
save(fig, '37-107')
