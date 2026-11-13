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

fig, ax = canvas(60)
text(ax, 44, 52, r'se lit « alpha de $2$ »', 'fixe', 'm')
for x, s, r in ((18, r'$\alpha$', 'sujet'), (34, r'$(2)$', 'varie'), (48, '=', 'encre'), (62, r'$a$', 'resultat')):
    text(ax, x, 38, s, r, 'l', weight='bold')
for x, s, r in ((18, 'application', 'sujet'), (36, 'élément de départ', 'varie'), (64, 'son image', 'resultat')):
    arrow(ax, (x, 27), (x, 34), r); text(ax, x, 22, s, r, 's')
save(fig, '42-180')
