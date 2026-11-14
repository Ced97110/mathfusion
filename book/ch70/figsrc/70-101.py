import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [18, 42, 66]
for x, h in zip(xs, [r'$y^2$', r'$y$', r'$1$']):
    text(ax, x + 10, 54, h, 'encre', 'm')
text(ax, 9, 40, r'$f$, $n=2$', 'sujet', 's')
text(ax, 9, 20, r'$g$, $m=1$', 'autre', 's')
for x, t in zip(xs, [r'$a_2=1$', r'$a_1=0$', r'$a_0=x^2-4$']):
    box(ax, x, 33, 21, 14, 'sujet', label=t, size='s')
box(ax, xs[0], 13, 21, 14, 'fixe', label='aucun', size='s')
box(ax, xs[1], 13, 21, 14, 'autre', label=r'$b_1=1$', size='s')
box(ax, xs[2], 13, 21, 14, 'autre', label=r'$b_0=2-x^2$', size='s')
text(ax, 44, 5, r'$x$ est caché dans $a_0$ et $b_0$', 'varie', 's')
save(fig, '70-101')
