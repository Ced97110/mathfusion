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

fig, ax = canvas(84)
D = 24
text(ax, 38, 50 + D, r'$(x+1)^2$', 'sujet', 'm'); text(ax, 72, 50 + D, r'$x^2+2x+1$', 'autre', 'm')
for y, lab, v in ((33 + D, r'$x=3$', '16'), (14 + D, r'$x=-2$', '1')):
    text(ax, 12, y, lab, 'encre', 'm')
    box(ax, 30, y - 5, 16, 10, 'sujet', label=v)
    box(ax, 64, y - 5, 16, 10, 'autre', label=v)
    text(ax, 55, y, '=', 'resultat', 'l', weight='bold')
box(ax, 4, 2, 80, 19, 'resultat')
text(ax, 44, 15, r'$(x+1)^2=x^2+2x+1$ pour tout $x$', 'resultat', 's', weight='bold')
text(ax, 44, 8, 'mêmes résultats : même application', 'resultat', 's')
save(fig, '42-182')
