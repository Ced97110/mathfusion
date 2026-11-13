import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(106)
n, s, x0, ytop = 12, 5.5, 16.0, 86.0
rows = {9: 'sujet', 11: 'varie'}; cols = {7: 'sujet', 1: 'varie'}
for r in range(n):
    for c in range(n):
        role = 'fixe'
        if r in rows: role = rows[r]
        if c in cols: role = cols[c]
        if r in rows and c in cols and rows[r] == cols[c]: role = 'resultat'
        ax.add_patch(Rectangle((x0 + c * s, ytop - (r + 1) * s), s, s, ec=COL['fixe'], fc=FILL[role], lw=0.4, zorder=2))
cx = lambda c: x0 + (c + 0.5) * s
cy = lambda r: ytop - (r + 0.5) * s
text(ax, 8, ytop + 3.5, '+', 'encre', 'm')
for c, role in [(0, 'fixe'), (1, 'varie'), (7, 'sujet'), (11, 'fixe')]:
    text(ax, cx(c), ytop + 3.5, str(c), role, 's')
for r, role in [(0, 'fixe'), (9, 'sujet'), (11, 'varie')]:
    text(ax, 12, cy(r), str(r), role, 's')
text(ax, cx(7), cy(9), '4', 'resultat', 's', weight='bold')
text(ax, cx(1), cy(11), '0', 'resultat', 's', weight='bold')
text(ax, 44, 100, 'ℤ/12ℤ : groupe fini des 12 positions\ntable de Cayley des sommes', 'encre', 'm')
text(ax, 26, 14, r'ligne 9 + colonne 7 = 4', 'sujet', 'm')
text(ax, 66, 14, r'ligne 11 + colonne 1 = 0', 'varie', 'm')
save(fig, '43-145')
