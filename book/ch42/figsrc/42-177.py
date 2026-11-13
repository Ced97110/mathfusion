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
gx, gy, cw, ch = 30, 14, 14, 12
grid(ax, gx, gy, cw, ch, colroles=['resultat', 'resultat', 'limite'])
pt(ax, gx, gy, cw, ch, 0, 0); pt(ax, gx, gy, cw, ch, 1, 0)
text(ax, gx + cw, gy + 2 * ch + 5, r'$\geq 1$ point', 'resultat', 's')
text(ax, gx + 2.5 * cw, gy + 2 * ch + 5, 'vide', 'limite', 's')
text(ax, 44, 54, r'$\forall s\in S,\ \exists t\in T$', 'sujet', 'l')
save(fig, '42-177')
