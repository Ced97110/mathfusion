import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(22, '(1 2 3)', ['$m=2$', "$m'=4$"], 'pairs tous deux'),
        (66, '(1 2)', ['$m=1$', "$m'=3$"], 'impairs tous deux')]
for c, name, ms, lab in cols:
    box(ax, c - 10, 56, 20, 9, 'sujet', label=name)
    for dx, m in zip((-8.5, 8.5), ms):
        arrow(ax, (c + dx * 0.6, 55), (c + dx, 44.5), 'fixe', lw=0.7)
        box(ax, c + dx - 6.5, 35, 13, 9, 'varie', label=m, size='s')
    brace(ax, c - 15, c + 15, 33, 'resultat', label=lab)
box(ax, 14, 6, 60, 10, 'limite', dash=True, label="$m$ pair, $m'$ impair : jamais", size='s')
save(fig, '46-204')
