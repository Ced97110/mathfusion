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

fig, ax = canvas(72)
text(ax, 24, 58, r'$\dfrac{1}{2}$', 'sujet', 'l'); text(ax, 64, 58, r'$\dfrac{2}{4}$', 'sujet', 'l')
text(ax, 44, 58, '=', 'sujet', 'l', weight='bold'); text(ax, 44, 70, 'même nombre', 'sujet', 's')
for x, v in ((24, '1'), (64, '2')):
    arrow(ax, (x, 49), (x, 28), 'varie'); text(ax, x + 4, 39, r'$f$', 'varie', 'm')
    box(ax, x - 8, 16, 16, 12, 'limite', label=v)
text(ax, 44, 22, r'$\neq$', 'limite', 'l', weight='bold')
text(ax, 44, 6, 'un nombre, deux résultats', 'limite', 's')
save(fig, '42-186')
