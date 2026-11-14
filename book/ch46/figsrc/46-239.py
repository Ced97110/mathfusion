import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for cx, p, n, par, r in [(16, '(1 2 3)', 2, 'paire', 'sujet'), (44, '(1 2)(3 4)', 2, 'paire', 'sujet'), (72, '(1 2 3 4)', 3, 'impaire', 'autre')]:
    text(ax, cx, 57, p, r, 's')
    for j in range(n): box(ax, cx - 10, 36 + j * 6.5, 20, 5.5, r, lw=0.6, r=0.4)
    text(ax, cx, 28, f'{n} échanges', 'encre', 's')
    text(ax, cx, 18, par, r, 'm', weight='bold')
text(ax, 44, 6, 'la forme en cycles donne la parité', 'encre', 's')
save(fig, '46-239')
