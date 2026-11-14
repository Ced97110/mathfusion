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
line(ax, [(44, 8), (44, 70)], 'fixe', lw=0.5, dash=True)
text(ax, 22, 73, 'bien définie', 'resultat', 'm', weight='bold'); text(ax, 66, 73, 'pas bien définie', 'limite', 'm', weight='bold')
text(ax, 22, 64, r'$p/q\mapsto 2p/q$', 'encre', 'm'); text(ax, 66, 64, r'$p/q\mapsto p$', 'encre', 'm')
for x in (12, 32, 56, 76): pass
for x, s in ((12, r'$\dfrac{1}{2}$'), (32, r'$\dfrac{2}{4}$'), (56, r'$\dfrac{1}{2}$'), (76, r'$\dfrac{2}{4}$')):
    text(ax, x, 50, s, 'sujet', 'l')
arrow(ax, (12, 44), (20, 27), 'resultat'); arrow(ax, (32, 44), (24, 27), 'resultat')
box(ax, 16, 14, 12, 12, 'resultat', label='1')
arrow(ax, (56, 44), (56, 27), 'limite'); arrow(ax, (76, 44), (76, 27), 'limite')
box(ax, 50, 14, 12, 12, 'limite', label='1'); box(ax, 70, 14, 12, 12, 'limite', label='2')
save(fig, '42-188')
