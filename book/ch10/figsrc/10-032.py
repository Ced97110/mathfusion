import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [5.5 + i * 20 for i in range(4)]
for x, n, e, r in zip(xs, ['48', '49', '51', '52'], [r'$-2$', r'$-1$', r'$+1$', r'$+2$'], ['autre', 'autre', 'varie', 'varie']):
    box(ax, x, 56, 17, 9, 'fixe', label=n); arrow(ax, (x + 8.5, 56), (x + 8.5, 50), r)
    text(ax, x + 8.5, 46, e, r, 'm')
brace(ax, xs[0], xs[-1] + 17, 41, 'resultat', 'somme des écarts = 0', depth=1.6)
box(ax, 4, 10, 80, 14, 'resultat', label=r'$\tilde{V} = 4 \times 50 = 200 = V$', size='m')
text(ax, 44, 29, 'chaque nombre devient 50', 'varie', 's')
save(fig, '10-032')
