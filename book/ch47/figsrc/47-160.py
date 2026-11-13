import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 3, 32, 82, 32, 'sujet', r=1.2); text(ax, 44, 59, r'les $n$ rotations : sous-groupe normal', 'sujet', 's')
xs = [22, 44, 66]
for x, l in zip(xs, ['1', r'$r$', r'$r^2$']): disc(ax, x, 50, 4.2, 'sujet', label=l, size='m')
arrow(ax, (xs[1] + 2, 45.8), (xs[2] - 2, 45.8), 'varie', curve=0.5, both=True)
text(ax, 44, 36, r'conjugué par $s$ : $r \leftrightarrow r^2$', 'varie', 's')
box(ax, 3, 3, 82, 22, 'varie', r=1.2); text(ax, 44, 20.5, r'les $n$ retournements', 'varie', 's')
for x, l in zip(xs, [r'$s$', r'$rs$', r'$r^2s$']): disc(ax, x, 11, 4.2, 'varie', label=l, size='s')
text(ax, 44, 28.5, r'$D_3$ : 6 symétries, 6 ÷ 3 = 2 classes', 'resultat', 's')
save(fig, '47-160')
