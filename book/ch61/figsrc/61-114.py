import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 30, 12, 12, 'sujet', label=r'$F$', size='l')
xs = [22, 38, 54, 72]
for x, n in zip(xs, [r'$u_1$', r'$u_2$', '…', r'$u_n$']):
    text(ax, x - 4, 36, '+', 'encre', 'm'); box(ax, x, 31, 10, 10, 'varie', label=n, size='m')
brace(ax, 22, 82, 29, 'varie', label=r'$n$ éléments ajoutés', size='s')
arrow(ax, (44, 44), (44, 50), 'resultat', lw=1.2)
box(ax, 14, 51, 60, 9, 'resultat', label=r'$F(u_1, \ldots, u_n)$', size='m')
text(ax, 44, 14, r'$n = 2$ :  $\mathbb{Q}(\sqrt{2},\ \sqrt{3})$', 'encre', 'm')
save(fig, '61-114')
