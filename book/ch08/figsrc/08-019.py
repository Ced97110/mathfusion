import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cols = [(16, '35', '100', 'sujet', 'fraction décimale', '1 suivi de zéros'),
        (44, '1', '3', 'limite', 'pas décimale', 'pas 10, 100…'),
        (72, '1', '2', 'limite', 'pas décimale', 'pas 10, 100…')]
for x, n, d, r, head, cap in cols:
    text(ax, x, 46, head, r, 's')
    text(ax, x, 36, n, 'encre', 'l', weight='bold')
    line(ax, [(x - 6, 31.5), (x + 6, 31.5)], 'encre', lw=1.0)
    box(ax, x - 7, 17, 14, 9, r, label=d, size='l', weight='bold')
    text(ax, x, 11, cap, r, 's')
fig_ = save(fig, '08-019')
