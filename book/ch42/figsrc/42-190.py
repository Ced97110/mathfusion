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

fig, ax = canvas(54)
text(ax, 14, 34, r'$\alpha$', 'sujet', 'l', weight='bold'); text(ax, 24, 34, ':', 'encre', 'l', weight='bold')
box(ax, 30, 28, 12, 12, 'varie', label=r'$S$', size='l'); box(ax, 58, 28, 12, 12, 'resultat', label=r'$T$', size='l')
arrow(ax, (44, 34), (56, 34), 'fixe', lw=1.2)
brace(ax, 30, 70, 43, 'fixe', label=r'$\rightarrow$ se lit « vers »', down=False)
for x, s, r, y1 in ((14, 'nom', 'sujet', 31), (36, 'ensemble de départ', 'varie', 27), (64, "ensemble d'arrivée", 'resultat', 27)):
    arrow(ax, (x, 23), (x, y1), r); text(ax, x, 19, s, r, 's')
save(fig, '42-190')
