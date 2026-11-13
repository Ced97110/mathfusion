import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
T = lambda s: r'$x-1$' if s else r'$x+3$'
rows = [(48, r'$D_1$', [(0, 1), (1, 1)]), (36, r'$D_2$', [(0, 1), (2, 0)]), (18, 'PPCM', [(0, 1), (1, 1), (2, 0)])]
for y, n, items in rows:
    text(ax, 8, y + 4.5, n, 'encre', 'm')
    for c, m in items:
        box(ax, 16 + 18 * c, y, 16, 9, 'sujet' if m else 'autre', label=T(m))
brace(ax, 16, 50, 18, 'sujet', r'pris dans $D_1$'); brace(ax, 52, 68, 18, 'autre', r'pris dans $D_2$')
save(fig, '21-069')
