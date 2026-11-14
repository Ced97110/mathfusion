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

fig, ax = canvas(76)
box(ax, 4, 51, 20, 14, 'varie', label=r'$S$', size='l'); box(ax, 62, 51, 20, 14, 'resultat', label=r'$T$', size='l')
arrow(ax, (26, 58), (60, 58), 'sujet', lw=1.2); text(ax, 43, 63, r'$\alpha$ ou $f$', 'sujet', 'm')
text(ax, 43, 44, r'$\rightarrow$ relie deux ensembles', 'sujet', 'm')
line(ax, [(4, 34), (84, 34)], 'fixe', lw=0.5, dash=True)
disc(ax, 14, 22, 4.5, 'varie', label=r'$s$'); disc(ax, 72, 22, 4.5, 'resultat', label=r'$t$')
arrow(ax, (21, 22), (65, 22), 'sujet', lw=1.2); line(ax, [(21, 19), (21, 25)], 'sujet', lw=1.2)
text(ax, 43, 8, r'$\mapsto$ relie deux éléments', 'sujet', 'm')
save(fig, '42-192')
