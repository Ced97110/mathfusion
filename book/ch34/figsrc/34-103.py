import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0 = 8; Wb = 44
box(ax, 8, 48, 6, 4, 'autre'); text(ax, 16, 50, '$\\cos^2(\\theta/2)$', 'autre', 's', ha='left')
box(ax, 44, 48, 6, 4, 'sujet'); text(ax, 52, 50, '$\\sin^2(\\theta/2)$', 'sujet', 's', ha='left')
rows = [(30, '$\\theta$ = 60°', 0.75, '0,75', '0,25', '0,75 + 0,25 = 1'), (12, '$\\theta$ = 180°', 0.0, '0', '1', '0 + 1 = 1')]
for y, name, c, lc, ls, tot in rows:
    text(ax, x0, y + 13, name, 'encre', 's', ha='left')
    wc = c * Wb
    if wc > 0: box(ax, x0, y, wc, 8, 'autre', label=lc, size='s')
    else: text(ax, x0 - 2.5, y + 4, lc, 'autre', 's')
    box(ax, x0 + wc, y, Wb - wc, 8, 'sujet', label=ls, size='s')
    text(ax, x0 + Wb + 4, y + 4, tot, 'resultat', 's', ha='left')
save(fig, '34-103')
