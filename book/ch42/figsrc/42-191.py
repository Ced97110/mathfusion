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

fig, ax = canvas(56)
disc(ax, 18, 34, 5, 'varie', label='1', size='l'); disc(ax, 64, 34, 5, 'resultat', label=r'$a$', size='l')
arrow(ax, (25, 34), (58, 34), 'sujet', lw=1.2); line(ax, [(25, 31), (25, 37)], 'sujet', lw=1.2)
text(ax, 41.5, 38, 'a pour image', 'sujet', 's')
text(ax, 18, 43, r'$s$', 'varie', 'm'); text(ax, 64, 43, r'$t$', 'resultat', 'm')
text(ax, 18, 24, 'élément de départ', 'varie', 's'); text(ax, 64, 24, 'son image', 'resultat', 's')
text(ax, 41, 9, r'$s\mapsto t$', 'sujet', 'l')
save(fig, '42-191')
