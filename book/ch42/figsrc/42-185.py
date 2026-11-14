import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, gx, gy, cw, ch, cols=('1','2','3'), rows=(r'$a$', r'$b$'), colroles=None, rowroles=None, labels=True):
    for i, c in enumerate(cols):
        role = colroles[i] if colroles else 'fixe'
        box(ax, gx + i * cw + 0.5, gy, cw - 1, len(rows) * ch, role=role, lw=0.6, r=0.6, dash=(role == 'limite'))
        if labels: text(ax, gx + (i + .5) * cw, gy - 3, c, 'encre', 'm')
    for j, rw in enumerate(rows):
        if j: line(ax, [(gx, gy + j * ch), (gx + len(cols) * cw, gy + j * ch)], 'fixe', lw=0.4, dash=True)
        if labels: text(ax, gx - 3, gy + (j + .5) * ch, rw, rowroles[j] if rowroles else 'encre', 'm')

def pt(ax, gx, gy, cw, ch, col, row, role='sujet'):
    disc(ax, gx + (col + .5) * cw, gy + (row + .5) * ch, 2.2, role)
    return (gx + (col + .5) * cw, gy + (row + .5) * ch)

fig, ax = canvas(66)
cw, ch, gy = 11, 10, 22
for gx, title, cr, cap, capx, pts in ((10, 'Graphe A', ['resultat', 'resultat', 'limite'], 'colonne 3 vide', 27, [(0, 0), (1, 0)]),
        (52, 'Graphe B', ['limite', 'resultat', 'resultat'], 'colonne 1 : deux points', 68, [(0, 0), (0, 1), (1, 0), (2, 1)])):
    grid(ax, gx, gy, cw, ch, colroles=cr)
    for c, r in pts: pt(ax, gx, gy, cw, ch, c, r, 'sujet')
    text(ax, gx + 1.5 * cw, gy + 2 * ch + 5, title, 'encre', 'm', weight='bold')
    text(ax, capx, 11, cap, 'limite', 's')
save(fig, '42-185')
