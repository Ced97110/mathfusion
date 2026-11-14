import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [14, 32, 50, 68]
labs = [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$']
text(ax, 44, 57, r'conjugués par $s$ dans $D_{4}$', 'encre', 'm')
for x, l in zip(xs, labs):
    box(ax, x - 6, 38, 12, 9, 'sujet', label=l)
res = [0, 3, 2, 1]
for i, j in enumerate(res):
    fixed = i == j
    arrow(ax, (xs[i], 37.5), (xs[j], 20.5), 'fixe' if fixed else 'varie', lw=1.0)
for x, l in zip(xs, labs):
    box(ax, x - 6, 11, 12, 9, 'sujet', label=l)
text(ax, 23, 4.5, 'fixes', 'fixe', 's')
text(ax, 59, 4.5, 'échangés', 'varie', 's')
save(fig, '47-134')
