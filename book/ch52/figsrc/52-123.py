import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$R/P$ est intègre', 'autre')
A = [r'$\bar a\bar b=\bar0$', r'$\bar a=\bar0$', r'$\bar b=\bar0$']
B = [r'$ab\in P$', r'$a\in P$', r'$b\in P$']
xs = [(3, 26), (35, 20), (63, 20)]
for (x, w_), a, b in zip(xs, A, B):
    box(ax, x, 50, w_, 10, 'autre', label=a); box(ax, x, 24, w_, 10, 'sujet', label=b)
    arrow(ax, (x + w_ / 2, 50), (x + w_ / 2, 34.5), 'varie')
for xc, s in ((32, r'$\Rightarrow$'), (59, 'ou')):
    text(ax, xc, 55, s, 'fixe'); text(ax, xc, 29, s, 'fixe')
text(ax, 44, 14, r'$P$ est premier', 'sujet')
save(fig, '52-123')
