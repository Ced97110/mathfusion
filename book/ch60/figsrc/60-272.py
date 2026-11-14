import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 77, r'colonne $j$ = image de $e_j$', 'encre', 'm')
# matrice par colonnes
x0, ytop, cw, ch = 4, 66, 12, 10
rows = [[2, 1], [0, 2]]
for r in range(2):
    for c in range(2):
        box(ax, x0 + c * cw, ytop - (r + 1) * ch, cw, ch, 'sujet' if c == 0 else 'varie', label=str(rows[r][c]), size='m')
for sgn, xx in ((-1, x0 - 1.5), (1, x0 + 2 * cw + 1.5)):
    line(ax, [(xx - sgn * 1.5, ytop + 0.5), (xx, ytop + 0.5), (xx, ytop - 2 * ch - 0.5), (xx - sgn * 1.5, ytop - 2 * ch - 0.5)], 'encre', lw=0.9)
box(ax, 4, 38, 4, 4, 'sujet'); text(ax, 10, 40, 'colonne 1 → T e₁', 'sujet', 's', ha='left')
box(ax, 4, 31, 4, 4, 'varie'); text(ax, 10, 33, 'colonne 2 → T e₂', 'varie', 's', ha='left')
# le plan
ox, oy, u = 48, 14, 12
arrow(ax, (ox - 6, oy), (ox + 38, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 6), (ox, oy + 56), 'fixe', lw=0.8)
for (px, py, lab, dx, dy) in ((1, 0, 'e₁', 0, -3.2), (0, 1, 'e₂', -4, 0)):
    disc(ax, ox + px * u, oy + py * u, 1.2, 'fixe')
    text(ax, ox + px * u + dx, oy + py * u + dy, lab, 'fixe', 's')
arrow(ax, (ox, oy), (ox + 2 * u, oy), 'sujet', lw=1.5)
arrow(ax, (ox, oy), (ox + 1 * u, oy + 2 * u), 'varie', lw=1.5)
text(ax, ox + 2 * u + 2, oy + 4, 'T e₁ = (2, 0)', 'sujet', 's')
text(ax, ox + u + 13, oy + 2 * u + 3, 'T e₂ = (1, 2)', 'varie', 's')
save(fig, '60-272')
