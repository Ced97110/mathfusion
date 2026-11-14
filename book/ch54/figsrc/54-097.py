import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cw, x0 = 9, 26
text(ax, 10, 53, 'position', 'fixe', 's')
for r in range(5):
    text(ax, x0 + (r + 0.5) * cw, 53, str(r), 'fixe', 's')
rows = [(0, r'$1$', 'autre', 38), (1, r'$x$', 'sujet', 24), (2, r'$x^2$', 'autre', 10)]
for pos, lab, role, y in rows:
    text(ax, 11, y + 4, lab, role, 'l')
    for r in range(5):
        if r == pos:
            box(ax, x0 + r * cw + 0.3, y, cw - 0.6, 8, role, label='1', size='m', weight='bold')
        else:
            box(ax, x0 + r * cw + 0.3, y, cw - 0.6, 8, 'fixe', label='0', size='s')
    text(ax, x0 + 5 * cw + 3, y + 4, '…', 'fixe', 'm')
save(fig, '54-097')
