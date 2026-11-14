import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$d = A\,\sin(B\,(t - C)) + D$', 'encre', 'l')
text(ax, 44, 5, r'$d = 13\,\sin(9{,}42\,(t - 0)) + 0$', 'encre', 'm')
cols = [(11, 'A', 'sujet', '13 = a'), (33, 'B', 'varie', r'9,42 = $\omega$'),
        (55, 'C', 'fixe', '0'), (77, 'D', 'fixe', '0')]
for x, L, r, v in cols:
    box(ax, x - 7, 36, 14, 10, r, label=L, size='l')
    arrow(ax, (x, 36), (x, 25), r)
    box(ax, x - 10, 14, 20, 10, r, label=v)
save(fig, '30-162')
