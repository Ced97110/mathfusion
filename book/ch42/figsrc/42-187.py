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
text(ax, 44, 70, 'trois écritures', 'encre', 'm')
text(ax, 8, 59, r'$p$', 'varie', 'm'); text(ax, 8, 53, r'$q$', 'fixe', 'm')
def frac(x, y, p, q):
    text(ax, x, y + 3.4, p, 'varie', 'l'); line(ax, [(x - 3, y), (x + 3, y)], 'fixe', lw=0.8); text(ax, x, y - 3.4, q, 'fixe', 'l')
for x, p, q in ((22, '1', '2'), (44, '2', '4'), (66, '3', '6')):
    frac(x, 56, p, q)
f = numberline(ax, 20, 68, 22, 0, 1, arrow_right=False)
for x0, x1 in ((22, 42), (44, 44), (66, 46)):
    arrow(ax, (x0, 46), (x1, 26), 'resultat')
disc(ax, f(0.5), 22, 2, 'resultat')
text(ax, 44, 9, 'un seul nombre', 'resultat', 'm')
save(fig, '42-187')
