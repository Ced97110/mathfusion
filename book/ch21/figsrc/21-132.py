import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
X = lambda x: 22 + (x - 2) * 8
Y = lambda y: 40 + y * 4
line(ax, [(4, Y(0)), (42, Y(0))], 'fixe'); line(ax, [(X(2), 28), (X(2), 58)], 'limite', dash=True)
n = 20
line(ax, [(X(2.25 + i * (2.0 / n)), Y(1 / (0.25 + i * (2.0 / n)))) for i in range(n + 1)], 'sujet', lw=1.2)
line(ax, [(X(0.2 + i * (1.5 / n)), Y(1 / (-1.8 + i * (1.5 / n)))) for i in range(n + 1)], 'sujet', lw=1.2)
text(ax, 22, 63, r'$y=\frac{1}{x-2}$', 'sujet', 'm'); text(ax, X(2) + 1, 29.5, r'$x=2$', 'limite', 's', ha='left')
f = numberline(ax, 52, 82, 44, 0, 8, step=2, arrow_right=False, labels=False)
disc(ax, f(4), 44, 1.7, 'limite'); text(ax, f(4), 50, r'$a=4$', 'limite', 'm')
box(ax, 8, 6, 72, 14, 'limite', label='même fait : le bas vaut 0')
arrow(ax, (22, 27), (30, 21), 'fixe'); arrow(ax, (67, 36), (60, 21), 'fixe')
save(fig, '21-132')
