import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
panels = [(15, 'sujet', '2-groupe', 8, 4, r'$8=2^3$'), (44, 'autre', '3-groupe', 9, 3, r'$9=3^2$'),
          (73, 'limite', 'aucun $p$-groupe', 6, 3, r'$6=2\times3$')]
for cx, role, head, n, ncol, eq in panels:
    box(ax, cx - 13.5, 14, 27, 33, role)
    text(ax, cx, 51, head, role, 's', weight='bold')
    nrow = n // ncol
    for k in range(n):
        r, c = divmod(k, ncol)
        disc(ax, cx + (c - (ncol - 1) / 2) * 5.6, 33 + ((nrow - 1) / 2 - r) * 5.6 + 1, 2.1, role)
    text(ax, cx, 8, eq, 'encre', 'm')
    text(ax, cx, 18.5, f'{n} éléments', role, 's')
save(fig, '50-022')
