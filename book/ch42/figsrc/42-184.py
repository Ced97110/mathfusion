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

fig, ax = canvas(62)
gx, gy, cw, ch = 22, 20, 14, 12
text(ax, 44, 55, r'$\{(1,a),(2,a),(3,b)\}$', 'sujet', 'l')
grid(ax, gx, gy, cw, ch, colroles=['resultat'] * 3)
for c, r in ((0, 0), (1, 0), (2, 1)): pt(ax, gx, gy, cw, ch, c, r)
brace(ax, gx + 0.5, gx + 3 * cw - 0.5, gy - 7, 'resultat', label='un point par colonne')
save(fig, '42-184')
