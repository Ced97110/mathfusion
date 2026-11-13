import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$12$ et $p=2$', 'encre', 'l')
labs = [r'$2^0=1$', r'$2^1=2$', r'$2^2=4$', r'$2^3=8$']
roles = ['fixe', 'fixe', 'sujet', 'limite']
xs = [5 + i * 20.5 for i in range(4)]
for x, lb, r in zip(xs, labs, roles):
    box(ax, x, 18, 17, 10, r, label=lb, size='m')
brace(ax, xs[0], xs[2] + 17, 18, 'fixe', 'divisent 12')
brace(ax, xs[3], xs[3] + 17, 18, 'limite', 'ne divise pas 12')
text(ax, xs[2] + 8.5, 38, r'$p^m=2^2=4$', 'sujet', 'l')
text(ax, xs[2] + 8.5, 33, 'la plus grande qui divise 12', 'sujet', 's')
save(fig, '50-033')
