import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y1, y2 = 42, 16
for c, t, wd, r in ((8, r'$-$', 8, 'fixe'), (19, '15', 12, 'sujet'), (31, r'$-$', 8, 'limite'), (40, r'$-$', 8, 'limite'), (50, '6', 10, 'sujet')):
    box(ax, c - wd / 2, y1, wd, 10, r, label=t, size='l')
brace(ax, 27, 44, y1 - 1, 'limite', 'deux traits qui se suivent')
text(ax, 72, y1 + 5, 'sans', 'limite', 's')
box(ax, 4, y2, 8, 10, 'fixe', label=r'$-$', size='l')
box(ax, 15, y2, 12, 10, 'sujet', label='15', size='l')
box(ax, 30, y2, 8, 10, 'varie', label=r'$-$', size='l')
box(ax, 41, y2 - 1, 27, 12, 'autre', fill=False, dash=True)
text(ax, 54.5, y2 + 5, r'$(-6)$', 'autre', 'l')
text(ax, 34, y2 - 4, 'opération', 'varie', 's'); text(ax, 54.5, y2 - 4, 'trait de $-6$', 'autre', 's')
text(ax, 77, y2 + 5, 'avec', 'resultat', 's')
save(fig, '13-030')
