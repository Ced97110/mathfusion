import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
text(ax, 44, 55, r'$\mathbb{R}^{*}$', 'sujet', 'xl')
text(ax, 44, 48, 'réels non nuls, avec la multiplication', 'encre', 's')
f = numberline(ax, 12, 70, 28, -4, 4, 1, labels=False, arrow_right=True)
for v in range(-4, 5):
    if v == 0: continue
    disc(ax, f(v), 28, 1.3, 'sujet')
disc(ax, f(0), 28, 1.5, 'limite', fill=False, lw=1.0)
brace(ax, f(-4), f(-1) + 3, 33, 'sujet', r'$\mathbb{R}$ : tous les réels', False)
arrow(ax, (f(0), 14), (f(0), 24), 'limite')
text(ax, f(0), 10, r'$*$ : on retire 0', 'limite', 's')
text(ax, f(0), 33, '0', 'limite', 's')
save(fig, '46-036')
