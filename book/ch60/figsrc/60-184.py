import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'bloc de Jordan de taille 3, valeur 5', 'encre', 's')
x0, ytop, cw, ch = 27, 54, 11, 9
rows = [[5, 1, 0], [0, 5, 1], [0, 0, 5]]
for r in range(3):
    for c in range(3):
        role = 'sujet' if r == c else 'varie' if c == r + 1 else 'fixe'
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, role, label=str(rows[r][c]), size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 3 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 3 * ch - 0.5), (xx - sgn * 1.5, ytop - 3 * ch - 0.5)], 'encre', lw=0.9)
for y, role, lab in ((17, 'sujet', 'diagonale : la valeur 5'), (11, 'varie', 'juste au-dessus : des 1'), (5, 'fixe', 'partout ailleurs : des 0')):
    box(ax, 14, y - 2, 4, 4, role)
    text(ax, 21, y, lab, role, 's', ha='left')
save(fig, '60-184')
