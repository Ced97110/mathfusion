import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
names = [(r'$F$', 'fixe'), (r'$F(v)$', 'autre'), (r'$F(u)$', 'sujet')]
xs = [3, 33, 63]
for (n, r), x in zip(names, xs): box(ax, x, 26, 22, 12, r, label=n, size='l')
for i, d in enumerate(['2', '2']):
    arrow(ax, (xs[i] + 22.5, 32), (xs[i + 1] - 0.5, 32), 'varie', lw=1.2)
    text(ax, xs[i] + 26, 36.5, d, 'varie', 'm')
brace(ax, 14, 44, 41, 'autre', label=r'degré de $v$ : 2', down=False, size='s')
text(ax, 44, 52, 'la tour', 'encre', 'm')
brace(ax, 14, 74, 23, 'resultat', label=r'degré de $u$ : $2 \times 2 = 4$', size='m')
text(ax, 44, 9, r'2 divise 4 : le degré de $v$', 'autre', 's')
text(ax, 44, 4.5, r'divise celui de $u$', 'autre', 's')
save(fig, '61-111')
