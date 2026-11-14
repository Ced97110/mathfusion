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

fig, ax = canvas(82)
D = 14
text(ax, 20, 64 + D, r'pour $3$', 'fixe', 'm')
box(ax, 3, 44 + D, 34, 12, 'sujet', label='ajoute 1, puis carré', size='s')
text(ax, 20, 40 + D, r'$(3+1)^2$', 'sujet', 'm')
box(ax, 3, 18 + D, 34, 12, 'autre', label='carré, + double, + 1', size='s')
text(ax, 20, 14 + D, r'$9+6+1$', 'autre', 'm')
arrow(ax, (38, 50 + D), (68, 38 + D), 'sujet'); arrow(ax, (38, 24 + D), (68, 32 + D), 'autre')
disc(ax, 76, 35 + D, 6, 'resultat', label='16', size='l')
text(ax, 74, 47 + D, 'même résultat', 'resultat', 's')
box(ax, 4, 2, 80, 16, 'resultat')
text(ax, 44, 12.5, 'deux règles, même application', 'resultat', 's', weight='bold')
text(ax, 44, 6.5, 'la règle écrite ne suffit pas', 'resultat', 's')
save(fig, '42-181')
