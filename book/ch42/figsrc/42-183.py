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

fig, ax = canvas(78)
for x, s in ((14, 'domaine'), (44, 'graphe'), (73, 'codomaine')): text(ax, x, 74, s, 'encre', 'm', weight='bold')
for y, r in ((58, 'sujet'), (22, 'sujet')):
    box(ax, 4, y - 6, 20, 12, 'sujet', label=r'$\mathbb{N}$', size='l')
    arrow(ax, (26, y), (60, y), 'fixe'); text(ax, 43, y + 3.5, 'doubler', 'fixe', 's')
box(ax, 63, 52, 20, 12, 'sujet', label=r'$\mathbb{N}$', size='l')
box(ax, 63, 16, 20, 12, 'autre', label=r'$\mathbb{R}$', size='l')
text(ax, 14, 40, '=', 'resultat', 'l', weight='bold'); text(ax, 43, 40, '=', 'resultat', 'l', weight='bold')
text(ax, 73, 40, r'$\neq$', 'limite', 'l', weight='bold')
save(fig, '42-183')
